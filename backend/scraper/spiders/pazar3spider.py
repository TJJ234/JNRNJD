import scrapy
from ..models import WEBSITES
from ..data_download import WriteAuctionToSiteCSV
from ..data_preprocess import ExtractAndStoreCarInfo, IsCarValid
import asyncio
import re

class Pazar3Spider(scrapy.Spider):
    name = "pazar3"
    allowed_domains = [WEBSITES["pazar3"]["domain"]]
    start_urls = [WEBSITES["pazar3"]["listings"]]

    def parse(self, response):
        for car in response.css(".goodssearch-item-content"):
            link = car.css(".Link_vis").attrib["href"]

            yield response.follow(link, self.parse_car)

    def parse_car(self, response):
            title = response.css("h1.ci-text-base::text").get()

            price_css = response.css(".new-price")
            price = 0
            currency = "ЕУР"
            if price_css:
                price = price_css[0].css("span.format-money-int::attr(value)").get()
                currency = price_css[0].css("span:not(.format-money-int)::text").get()
            price = "price: " + price + " " + currency

            image_link = response.css(".custom-photo-link::attr(href)").get()

            tags = response.css(".tag-item")
            tags_list = []
            for tag in tags:
                tags_list.append(tag.css("span::text").get())
                tags_list.append(re.sub(r"\s+", " ", tag.css("bdi::text").get()).strip())

            tags_list = " ".join(tags_list)
            description = response.css(".description-area span::text").get()
            
            date = "date: " + response.css(".published-date::text").get()

            full_text = "\n".join([title, price, tags_list, description, date])

            asyncio.run(ExtractAndStoreCarInfo(full_text, {
                "website": "pazar3",
                "image_link": image_link,
                "link": response.url
            }))