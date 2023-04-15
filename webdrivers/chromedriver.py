from selenium.webdriver.chrome.options import Options
from webdrivers.base_webdriver import BaseWebDriver
from selenium import webdriver
from settings import CHROMEDRIVER_PATH


class ChromeWebdriver(BaseWebDriver):

    @classmethod
    def get(cls, *args, **kwargs) -> webdriver:
        """
        This method returns the chrome webdriver instance.
        """
        options = Options()
        options = cls._get_options(options)

        wd = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)
        cls._set_plugins_property(wd)
        cls._set_chrome_property(wd)
        cls._set_webdriver_property(wd)
        cls._set_navigator_langauge(wd)
        cls._set_navigator_proto(wd)
        return wd
