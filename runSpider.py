# In this file we will run the spider(s)
from scrapy.crawler import CrawlerProcess
from myBookSpider import bookSpider
from scrapy.utils.project import get_project_settings

def runSpider():

    # Running scraper
    process = CrawlerProcess(get_project_settings())
    process.crawl(bookSpider)
    process.start()

if (__name__ == "__main__"):

    runSpider()