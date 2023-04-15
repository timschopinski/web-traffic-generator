from selenium.webdriver.chrome.options import Options
from webdrivers.base_webdriver import BaseWebDriver
from selenium import webdriver


class ChromeWebdriver(BaseWebDriver):

    @classmethod
    def get(cls, executable_path: str, *args, **kwargs) -> webdriver:
        """
        This method returns the chrome webdriver instance. You can specify additional options using args
        """
        super().get(executable_path, *args, **kwargs)
        options = Options()
        options = cls._get_options(options)

        wd = webdriver.Chrome(options=options, executable_path=executable_path)
        cls._set_plugins_property(wd)
        cls._set_chrome_property(wd)
        cls._set_webdriver_property(wd)
        cls._set_navigator_langauge(wd)
        cls._set_navigator_proto(wd)
        return wd
