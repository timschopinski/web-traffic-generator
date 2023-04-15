
<a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/l/vue.svg?sanitize=true" alt="License"></a>



# Web Traffic Generator


This project is a command-line tool for generating web traffic using Selenium and Python. 
This tool currently supports Tor and Chrome browsers, and allows you to specify the number of instances, time duration, and target URL.

### Installation
To install the Web Traffic Generator, you need to have Python 3.10 or higher installed on your system. You can then install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Extra Installation steps for Chrome

1) Install Chrome browser
2) install chromedriver
3) Add the path to your chrome driver in settings.py

```python
# settings.py

CHROMEDRIVER_PATH = "/path/to/chromedriver"
```


### Extra Installation steps for Tor

1) Install Tor browser
2) Add the path to your firefox binary in settings.py

```python
# settings.py

TOR_BINARY_PATH = "/Users/XXX/Applications/TorBrowser.app/Contents/MacOS/firefox"
```

/Users/XXX/Applications/TorBrowser.app/Contents/MacOS/firefox’ applies to my local environment.
You need to provide your custom path.

### Usage
To use the Web Traffic Generator, you can run the main.py script with the following command-line arguments:

usage: main.py [-h] --url URL [--browser {TOR,CHROME}] [--time TIME] [--instances INSTANCES]

Generate Web Traffic

options:

  -h, --help            show this help message and exit

  --url URL             The URL of the website to generate traffic for

  --browser {TOR,CHROME}
                        specify which browser to use (default: TOR)

  --time TIME           The time that each bot will spend on the website (in seconds), default: 120

  --instances INSTANCES
                        The number of instances/website visitors that will generate traffic (default: 1)
### Usage

```bash
main.py [-h] --url URL [--browser {TOR,CHROME}] [--time TIME] [--instances INSTANCES]
```

| Options                | description                                                                      |
|------------------------|----------------------------------------------------------------------------------|
| -h, --help             | show this help message and exit                                                  |
| --url URL              | The URL of the website to generate traffic for                                   |
| --browser {TOR,CHROME} | specify which browser to use (default: TOR)                                      |
| --time TIME            | The time that each bot will spend on the website (in seconds), default: 120      |
| --instances INSTANCES  | The number of instances/website visitors that will generate traffic (default: 1) |

