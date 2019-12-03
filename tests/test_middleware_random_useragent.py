from unittest import TestCase

from scrapy.spiders import Spider
from scrapy.http import Request

from scrapy.utils.test import get_crawler

from middleware import RandomUserAgentMiddleware


class RandomUserAgentMiddlewareTest(TestCase):

    def get_spider_and_mw(self, enabled, default=None, overwrite=False):
        crawler = get_crawler(Spider, {'RANDOM_UA_ENABLED': enabled, 'RANDOM_UA_DEFAULT_TYPE': default,
                                       'RANDOM_UA_OVERWRITE': overwrite})
        spider = crawler._create_spider('foo')
        return spider, RandomUserAgentMiddleware.from_crawler(crawler)

    def test_default_agent(self):
        spider, mw = self.get_spider_and_mw(True)
        req = Request('http://scrapytest.org/')
        mw.spider_opened(spider)
        assert mw.process_request(req, spider) is None
        self.assertTrue(req.headers['User-Agent'].decode("utf-8") in mw.ua.get('desktop'))

    def test_default_bot_agent(self):
        spider, mw = self.get_spider_and_mw(True, 'bot')
        req = Request('http://scrapytest.org/')
        mw.spider_opened(spider)
        assert mw.process_request(req, spider) is None
        self.assertTrue(req.headers['User-Agent'].decode("utf-8") in mw.ua.get('bot'))

    def test_mobile_agent(self):
        spider, mw = self.get_spider_and_mw(True)
        req = Request('http://scrapytest.org/', meta={'ua': 'mobile'})
        mw.spider_opened(spider)
        assert mw.process_request(req, spider) is None
        self.assertTrue(req.headers['User-Agent'].decode("utf-8") in mw.ua.get('mobile'))

    def test_bot_agent(self):
        spider, mw = self.get_spider_and_mw(True)
        req = Request('http://scrapytest.org/', meta={'ua': 'bot'})
        mw.spider_opened(spider)
        assert mw.process_request(req, spider) is None
        self.assertTrue(req.headers['User-Agent'].decode("utf-8") in mw.ua.get('bot'))

    def test_force(self):
        spider, mw = self.get_spider_and_mw(True, None, True)
        req = Request('http://scrapytest.org/', headers={'User-Agent': "test"})
        mw.spider_opened(spider)
        assert mw.process_request(req, spider) is None
        self.assertTrue(req.headers['User-Agent'].decode("utf-8") in mw.ua.get('desktop'))

    def test_no_agent(self):
        spider, mw = self.get_spider_and_mw(False)
        spider.user_agent = None
        mw.spider_opened(spider)
        req = Request('http://scrapytest.org/')
        assert mw.process_request(req, spider) is None
        assert 'User-Agent' not in req.headers
