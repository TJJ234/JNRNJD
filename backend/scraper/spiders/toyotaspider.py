import scrapy
from ..models import WEBSITES
from ..data_download import WriteAuctionToSiteCSV
from ..data_preprocess import ExtractAndStoreCarInfo, IsCarValid

# Needs work #
class ToyotaSpider(scrapy.Spider):
    name = "toyota"
    allowed_domains = [WEBSITES["toyota"]["domain"]]
    start_urls = [WEBSITES["toyota"]["listings"]]

    def parse(self, response):
        for car in response.css(".ad-desc-div.col-lg-6.text-left"):
            title = car.css("h3 a::text").get().strip()
            link = car.css("h3 a").attrib["href"]
            tags = " ".join(
                text.strip() for text in car.css("p::text").getall() if text.strip() and text.strip() != "•"
            )
            description = car.css(".searchAdDesc::text").get().strip()
            price = car.css(".search-ad-price::text").get().strip()

            full_text = title + " " + tags + " " + description + " " + price

            CarData = ExtractAndStoreCarInfo(full_text)
            CarData["link"] = WEBSITES["toyota"]["domain"] + link
            
            if IsCarValid(CarData):
                WriteAuctionToSiteCSV("toyota", CarData)

        pages_str = response.css(".number-of-pages::text").get()
        if pages_str:
            pages_str = pages_str.split()
            page_number = int(pages_str[1])
            total_pages = int(pages_str[3])

            #if page_number < total_pages:
            #    #next_page = WEBSITES["toyota"]["listings"][:-1] + str(page_number + 1)
            #    #yield scrapy.Request(next_page, callback=self.parse)
            #else:
            #    self.log("Done scraping toyota!")

