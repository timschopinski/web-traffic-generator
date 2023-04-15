from typing import Type

from web.crawlers import Crawler
from webdrivers.utils import Browser
from webdrivers.factory import WebDriverFactory


class CrawlerManager:
    def __init__(
        self,
        crawler: Type[Crawler],
        num_of_instances: int,
        seconds: int,
        url: str,
        browser: Browser,
    ):
        self.Crawler = crawler
        self._num_of_instances = num_of_instances
        self._seconds = seconds
        self._url = url
        self._browser = browser

    def crawl(self):
        for _ in range(self._num_of_instances):
            wd = WebDriverFactory.get_webdriver(self._browser)
            crawler = self.Crawler(wd, self._url, self._seconds)
            crawler.start()
