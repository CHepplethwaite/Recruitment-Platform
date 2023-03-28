import scrapy

class jobSpider(scrapy.Spider):
    name = "airtel.co.zm"

    def start_requests(self):
        urls = [
            "https://www.airtel.co.zm/career_position",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        page = response.url.split("/")[-2]