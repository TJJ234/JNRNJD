from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from .spiders import Pazar3Spider, Reklama5Spider, VoziSpider
import os

CAR_DATA_URL = "NO HOSTED URL AS OF NOW"

# Django likes to run stuff twice
if os.environ.get('RUN_MAIN') == 'true':
    # Scraper runs asynchronously and gets the data from all websites #
    def start_scraper():
        runner = CrawlerRunner(get_project_settings())

        spiders = [Pazar3Spider, Reklama5Spider]#, VoziSpider]

        @defer.inlineCallbacks
        def crawl():
            for spider in spiders:
                yield runner.crawl(spider)
            reactor.stop()
        crawl()
        reactor.run()
    start_scraper()

    #from .neo4j_db import graph