import scrapy

from mlprod.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):      
        quotes = response.css(".quote")
        for quote in quotes:
            text = quote.css(".text::text").get()
            author = quote.css(".author::text").get()
            yield QuoteItem(text=text, author=author)
