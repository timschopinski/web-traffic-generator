from enum import Enum


class Browser(Enum):
    TOR = "TOR"
    CHROME = "CHROME"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
