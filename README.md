# Black Widow - Blackbox Data-driven Web Scanning

## Running Black Widow

1. Install dependencies

```sh
uv sync
```

1. Add chromedriver to your path

Example for current directory on linux:

PATH=$PATH:.

2. Run the scanner

```sh
uv run crawl.py --url http://example.com
```

Or

```sh
uv run crawl.py --url http://example.com --remote "http://localhost:4444/wd/hub"
```
