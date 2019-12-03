# scrapy-random-useragent-pro

Random UserAgent middleware for Scrapy.

You can chose your preferred ua in request.meta[desktop,mobile,bot].

## Install

```bash
pip install scrapy-random-useragent-pro
```

## Usage

settings.py

```python
RANDOM_UA_ENABLED = True
RANDOM_UA_DEFAULT_TYPE = 'mobile'
# always change user-agent
RANDOM_UA_OVERWRITE = False


DOWNLOADER_MIDDLEWARES = {
    'scrapy_random_useragent_pro.middleware.RandomUserAgentMiddleware': 100,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,# important
}

```

In your code

```python
yield Request('http://scrapytest.org/', meta={'ua': 'mobile'})
```