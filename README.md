# Black Widow - Blackbox Data-driven Web Scanning

## Installation

1. Install dependencies

```sh
uv sync
```

[Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/) will automatically download the appropriate version of chromedriver for your system, so you don't need to worry about it. Make sure to have a good network connection for the first run, as it will download the driver.

## Running Black Widow

Run the scanner

```sh
uv run crawl.py --url http://testphp.vulnweb.com
```

Or

```sh
uv run crawl.py --url http://testphp.vulnweb.com --remote "http://localhost:4444/wd/hub"
```
