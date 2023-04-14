from webdrivers.tordriver import TorWebDriver, click_connect_button
import argparse
from crawlers.random_crawler import RandomCrawler


def main():
    parser = argparse.ArgumentParser(description="Generate Web Traffic")
    parser.add_argument(
        "--url",
        type=str,
        help="The URL of the website to generate traffic for",
        required=True,
    )
    parser.add_argument(
        "--time",
        type=int,
        help="The time that each bot will spend on the website (in seconds)",
        default=120,
    )
    parser.add_argument(
        "--bots",
        type=int,
        help="The number of bots/website visitors to generate traffic for (default: 1)",
        default=1,
    )
    binary_path = "/Applications/Tor Browser.app/Contents/MacOS/firefox"

    args = parser.parse_args()
    for _ in range(args.bots):
        wd = TorWebDriver.get(binary_path)
        crawler = RandomCrawler(wd, args.url, args.time)
        crawler.start()


if __name__ == "__main__":
    main()
