import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class bookScrapingPracticeItem(scrapy.Item):

    # define the fields for your item here
    title = scrapy.Field()
    price = scrapy.Field()

class bookSpider(scrapy.Spider):

    # name of our spider (used later to start it)
    name = "bookSpider"
    custom_settings = {
        "FEED_URI" : "resultFile.csv",
        "FEED_FORMAT" : "csv",
    }
    start_urls = [
        "http://books.toscrape.com/"
    ]

    def parse(self, response):

        # Getting an instance of our item class
        item = bookScrapingPracticeItem()

        # Getting all the article's with prouduct pod class
        articles = response.css("article.product_pod")

        # Looping thru all the article elements we got earlier
        for article in articles:

            # Getting the needed values from the site and putting them in variables
            title = article.css("a::attr(title)").extract()
            price = article.css("p.price_color::text").extract()

            # Setting the title / price variables in our items class equal to the variables that we just extracted data in to
            item["title"] = title
            item["price"] = price
            yield item

def runSpider():

    # Running scraper
    process = CrawlerProcess(get_project_settings())
    process.crawl(bookSpider)
    process.start()

if (__name__ == "__main__"):

    runSpider()