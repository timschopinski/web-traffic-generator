from webdrivers.chromedriver import ChromeWebdriver
from webdrivers.tordriver import TorWebDriver
from webdrivers.utils import Browser


class WebDriverFactory:

    @staticmethod
    def get_webdriver(browser: Browser):
        drivers = {
            Browser.CHROME: ChromeWebdriver,
            Browser.TOR: TorWebDriver
        }
        return drivers[browser].get()
