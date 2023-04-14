import psutil

from webdrivers.tordriver import TorWebDriver


class TestTorWebDriver:
    binary_path = "/Applications/Tor Browser.app/Contents/MacOS/firefox"

    def test_only_one_tor_browser_can_be_open(self):
        TorWebDriver.kill_all_tor_browsers()
        driver = TorWebDriver.get(executable_path=self.binary_path)
        assert driver is not None

        tor_browsers_count = sum(
            [1 for proc in psutil.process_iter() if proc.name() == TorWebDriver.TOR_BROWSER_NAME]
        )
        assert tor_browsers_count == 1
        driver.quit()

        tor_browsers_count = sum(
            [1 for proc in psutil.process_iter() if proc.name() == TorWebDriver.TOR_BROWSER_NAME]
        )
        assert tor_browsers_count == 0
