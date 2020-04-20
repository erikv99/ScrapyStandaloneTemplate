import scrapy
from items import scrapyStandaloneTestItem

class bookSpider(scrapy.Spider):

    # name of our spider (used later to start it)
    name = "bookSpider"
    custom_settings = {
        "FEED_URI" : "resultFile.csv",
        "FEED_FORMAT" : "csv",
        "FEED_EXPORT_FIELDS" : ["title", "price"]
    }
    start_urls = [
        "http://books.toscrape.com/"
    ]

    def parse(self, response):

        # Getting an instance of our item class
        item = scrapyStandaloneTestItem()

        # Getting all the article's with product pod class
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