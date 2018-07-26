# -*- coding: utf-8 -*-
import scrapy


class InfinityknowSpider(scrapy.Spider):
    name = 'infinity'
    allowed_domains = ['infinityknow.com']
    start_urls = ['http://infinityknow.com']
                  #'http://infinityknow.com/page/1/?s=vuejs']

    @staticmethod
    def _get_url(s):
        return s.css('h2 a::attr(href)').extract_first()

    @staticmethod
    def _get_title(s):
        return s.css('.entry-title ::text').extract_first()

    @staticmethod
    def _get_view_count(s):
        return s.css('span.post-views-count ::text').extract_first()

    @staticmethod
    def _get_id(s):
        return s.css('article ::attr(id)').extract_first()

    @staticmethod
    def _get_category(s):
        return s.css('.cat-links a::text').extract()

    def parse_article(self, response):
        yield {'id': self._get_id(response), 'total_view': self._get_view_count(response),
               'category': self._get_category(response), 'url': response.url,  'title': self._get_title(response), }

    def parse(self, response):
        for card in response.css('article.post-item'):
            yield scrapy.Request(url=self._get_url(card), callback=self.parse_article)

        next_page = response.css('.next ::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
