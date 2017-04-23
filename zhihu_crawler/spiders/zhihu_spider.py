# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data[*].answer_count,'
                  'articles_count,gender,follower_count,badge[?(type=best_answerer)].topics&offset=0&limit=20']

    def parse(self, response):
        print(response)
        pass
