import time
from webdrivers.tordriver import TorWebDriver, click_connect_button


binary_path = "/Applications/Tor Browser.app/Contents/MacOS/firefox"
wd = TorWebDriver.get(binary_path)

time.sleep(3)
click_connect_button(wd)
time.sleep(3)
# check my IP address
url = "https://carsinfo.pl"
wd.get(url)
time.sleep(5)
