from web.crawlers import RandomCrawler
from managers.crawler_manager import CrawlerManager
from parser import get_parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    manager = CrawlerManager(
        RandomCrawler,
        args.instances,
        args.time,
        args.url,
        args.browser,
    )
    manager.crawl()


if __name__ == "__main__":
    main()
