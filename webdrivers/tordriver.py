import os
from typing import Optional

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from webdrivers.base_webdriver import BaseWebDriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By

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

class TorWebDriver(BaseWebDriver):

    @classmethod
    def get(cls, executable_path: str, options=None, locale="en-US, en", *args, **kwargs) -> webdriver:
        if not os.path.exists(executable_path):
            raise ValueError("The binary path to Tor firefox does not exist.")

        firefox_binary = FirefoxBinary(executable_path)

        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", locale)
        firefox_profile.update_preferences()
        wd = webdriver.Firefox(
            firefox_profile=firefox_profile, firefox_binary=firefox_binary, options=options
        )
        return wd
