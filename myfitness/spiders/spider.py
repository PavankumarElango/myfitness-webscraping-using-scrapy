import scrapy
from scrapy import Selector
import re

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['myfitnesspal.com/']
    start_urls = ['https://www.myfitnesspal.com/food/search?page=1&search=https://www.myfitnesspal.com/food/search?page=1&search=parle-g%20biscuits']
    page_number = 2

    def parse(self, response):
        name =response.xpath("//div[@class = 'jss64']//text()").extract()
        description = response.xpath("//div[@class = 'jss65']").extract()
        nutrition = response.xpath('//div[contains(@class, "jss70")]').extract()
        print(name)
        print(description)
        print(nutrition)
        
        
        for item in zip(name,description,nutrition):
            scraped_info = {
                'name' : item[0],
                'description' : item[1],
                'nutrition' : item[2],
                
            }

            yield scraped_info
        #url =https://www.myfitnesspal.com/food/search?page=1&search=nestle   
        next_page = "https://www.myfitnesspal.com/food/search?page="+ str(SpiderSpider.page_number) +'&search=https://www.myfitnesspal.com/food/search?page=1&search=https://www.myfitnesspal.com/food/search?page=1&search=parle-g%20biscuits'
        if SpiderSpider.page_number <   10:
            SpiderSpider.page_number += 1
            
            yield response.follow(next_page,callback = self.parse,dont_filter=True)