import time
import random
import logging
from abc import ABC, abstractmethod
from typing import List
from urllib.parse import urlparse
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


class Crawler(ABC):

    def __init__(self, wd: webdriver, url: str, seconds: int = 120):
        self._wd = wd
        self._url = url
        self._seconds = seconds

    @abstractmethod
    def start(self):
        ...


class RandomCrawler(Crawler):
    def __init__(self, wd: webdriver, url: str, seconds: int = 120):
        super().__init__(wd, url, seconds)
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)
        self._logger.info(f"{self} created.")

    def start(self):
        self._wd.get(self._url)
        self._wait()
        start_time = time.time()
        while True:
            self._wait()
            if not self._validate_time(start_time):
                self._logger.info(f"Finished crawling after {self._seconds}s.")
                break
            random_button = random.choice(self._get_clickable_buttons())
            self._scroll_to(random_button)
            try:
                random_button.click()
            except Exception as e:
                self._logger.error(e)
                continue
            self._wait()
            time.sleep(random.random() * 10)
            self._logger.info(f"Current url: {self._wd.current_url}")

    def _wait(self):
        wait = WebDriverWait(self._wd, 20)
        wait.until(
            lambda wd: wd.execute_script("return document.readyState") == "complete"
        )

    def _scroll_to(self, element: WebElement):
        self._wd.execute_script("arguments[0].scrollIntoView();", element)

    def _validate_time(self, start_time):
        return time.time() - start_time < self._seconds

    def _get_clickable_buttons(self) -> List[WebElement]:
        wait = WebDriverWait(self._wd, 10)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@onclick or @href]")))
        try:
            buttons: List[WebElement] = self._wd.find_elements(By.XPATH, "//*[@onclick or @href]")
            buttons = [button for button in buttons if self._is_internal_link(button.get_attribute('href'))]
        except Exception as e:
            raise e
        self._logger.debug(f"get_clickable_buttons returns: {buttons}")
        return buttons

    def _is_internal_link(self, link: str) -> bool:
        if not link:
            return False
        parsed_url = urlparse(link)
        return parsed_url.netloc == urlparse(self._url).netloc and parsed_url.scheme == urlparse(self._url).scheme

    def __str__(self):
        return f"{self.__class__.__name__}(url={self._url}, time={self._seconds})"
