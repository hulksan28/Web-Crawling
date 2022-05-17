import scrapy

class CloudSigmaCrawler(scrapy.Spider):
    name = "cloudsigma_crawler"
    start_urls = [
        'https://blog.scrapinghub.com/page/1/',
    ]

    def parse(self, response):
        SET_SELECTOR = '.post'
        for tutorial in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.entry-wrap .entry-header > h2 > a ::text'
            URL_SELECTOR = '.entry-featured > a ::attr(href)'
            IMG_SELECTOR = 'img ::attr(data-lazy-src)'
            CAPTION_SELECTOR = '.entry-content > p::text'
            yield {
                'title': tutorial.css(NAME_SELECTOR).extract_first(),
                'image': tutorial.css(IMG_SELECTOR).extract_first(),
                'url': tutorial.css(URL_SELECTOR).extract_first(),
                'caption': tutorial.css(CAPTION_SELECTOR).extract_first(),
            }