from abc import ABC, abstractmethod
from selenium import webdriver


class BaseWebDriver(ABC):

    @classmethod
    @abstractmethod
    def get(cls, executable_path: str, *args, **kwargs) -> webdriver:
        ...
