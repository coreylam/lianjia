import scrapy
from lianjia.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["lianjia.com"]
    start_urls = [
        "http://bj.lianjia.com/ershoufang/pg1tt2/",
    ]

    def parse(self, response):
        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
        #     url = response.urljoin(response.url, href.extract())
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)
        for hinfo in response.css('ul.sellListContent li.clear div.info.clear div.address div.houseInfo'):
            item = LianjiaItem()
            item['title'] = ''
            item['location'] = hinfo.xpath('a/text()').extract()[0]
            item['house_info'] = hinfo.xpath('text()').extract()[0]
            # self.log("title = %s" % str(item['title']))
            # self.log("location = %s" % str(item['location']))
            # self.log("house_info = %s" % str(item['house_info']))
            yield item
    # def parse_dir_contents(self, response):
        # for sel in response.xpath('//ul/li'):
        #     item = DmozItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item