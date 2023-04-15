import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdrivers.base_webdriver import BaseWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
import psutil
from selenium.webdriver.firefox.options import Options
from settings import TOR_BINARY_PATH


def click_connect_button(wd: webdriver) -> None:
    time.sleep(5)
    delay = 60
    try:
        connect_button = WebDriverWait(wd, delay).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='connectButton']"))
        )
        connect_button.click()

    except TimeoutException:
        raise Exception("Connect button failed to load")
    time.sleep(5)


class TorWebDriver(BaseWebDriver):
    TOR_BROWSER_NAME = "firefox"

    @classmethod
    def get(
        cls, *args, **kwargs
    ) -> webdriver:
        cls.kill_all_tor_browsers()
        firefox_binary = FirefoxBinary(TOR_BINARY_PATH)
        profile = cls.get_profile()
        options = Options()
        options = cls._get_options(options)
        wd = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=firefox_binary,
            options=options,
        )
        click_connect_button(wd)
        return wd

    @staticmethod
    def kill_all_tor_browsers():
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                if process_name == TorWebDriver.TOR_BROWSER_NAME:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    @staticmethod
    def get_profile():
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference(
            "intl.accept_languages", "en-US, en"
        )
        firefox_profile.update_preferences()
        return firefox_profile
