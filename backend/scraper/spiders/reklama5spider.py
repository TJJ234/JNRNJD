import scrapy
from ..models import WEBSITES, Car
from ..data_preprocess import ExtractAndStoreCarInfo
import asyncio

class Reklama5Spider(scrapy.Spider):
    name = "reklama5"
    allowed_domains = [WEBSITES["reklama5"]["domain"]]
    start_urls = [WEBSITES["reklama5"]["listings"]]

    def parse(self, response):
        for car in response.css(".ad-desc-div.col-lg-6.text-left"):
            link = car.css("h3 a").attrib["href"]
            yield response.follow(link, self.parse_car)
    
        # Go to the next page until there is no next page and start scraping
        pages_str = response.css(".number-of-pages::text").get()
        if pages_str:
            pages_str = pages_str.split()
            page_number = int(pages_str[1])
            total_pages = int(pages_str[3])

            #if page_number < total_pages:
            #    #next_page = WEBSITES["reklama5"]["listings"][:-1] + str(page_number + 1)
            #    #yield scrapy.Request(next_page, callback=self.parse)
            #else:
            #    self.log("Done scraping reklama5!")

    def parse_car(self, response):
        title = "title: " + response.css(".card-title::text").get().strip()
        price = "price: " + response.css(".mb-0.defaultBlue::text").get().strip()
        tags = response.css(".mb-1::text").getall()
        tags_string = "tags: " + '\n'.join([f'{tags[i]} {tags[i+1]}' for i in range(0, len(tags), 2)])
        description = "description: " + response.css("p.mt-3::text").get().strip()
        image_link = "https:" + response.css(".ad-image img::attr(src)").get()
        full_text = "\n".join([title, price, tags_string, description])
        asyncio.run(ExtractAndStoreCarInfo(full_text, {
            "website": "reklama5",
            "image_link": image_link,
            "link": response.url
        }))