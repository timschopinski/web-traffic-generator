from web.crawlers import RandomCrawler
from managers.crawler_manager import CrawlerManager
from parser import get_parser


def main():
    parser = get_parser()
    tor_executable_path = "/Applications/Tor Browser.app/Contents/MacOS/firefox"
    chrome_executable_path = "/Users/timschopinski/PycharmProjects/web-traffic-generator/drivers/chromedriver"
    args = parser.parse_args()
    manager = CrawlerManager(
        RandomCrawler,
        args.instances,
        args.time,
        args.url,
        args.browser,
        chrome_executable_path,
    )
    manager.crawl()


if __name__ == "__main__":
    main()
