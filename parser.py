import argparse
from webdrivers.utils import Browser


def get_parser() -> argparse.ArgumentParser:

    def browser_type(arg_value):
        try:
            browser = Browser[arg_value.upper()]
        except KeyError:
            raise argparse.ArgumentTypeError(f"{arg_value} is not a valid browser")
        return browser

    parser = argparse.ArgumentParser(description="Generate Web Traffic")
    parser.add_argument(
        "--url",
        type=str,
        help="The URL of the website to generate traffic for",
        required=True,
    )
    parser.add_argument(
        "--browser",
        type=browser_type,
        choices=list(Browser),
        default=Browser.TOR,
        help="specify which browser to use (default: TOR)",
    )
    parser.add_argument(
        "--time",
        type=int,
        help="The time that each bot will spend on the website (in seconds), default: 120",
        default=120,
    )
    parser.add_argument(
        "--bots",
        type=int,
        help="The number of bots/website visitors to generate traffic for (default: 1)",
        default=1,
    )
    return parser
