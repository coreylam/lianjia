import scrapy
from lianjia.items import LianjiaSzItem
import time

class LianjiaSpider(scrapy.Spider):
    name = "lianjiasz"
    allowed_domains = ["lianjia.com"]
    start_urls = [
        "https://sz.fang.lianjia.com/loupan/",
        "https://gz.fang.lianjia.com/loupan/",
    ]
    total_page = [72, 75]
    def start_requests(self):
        # url = "https://sz.fang.lianjia.com/loupan/"
        idx = 1
        url = LianjiaSpider.start_urls[idx]
        for i in range(LianjiaSpider.total_page[idx]):
            url_page = url+'pg'+str(i+1)
            time.sleep(2)
            yield scrapy.Request(url=url_page, callback=self.parse)

    def parse(self, response):
        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
        #     url = response.urljoin(response.url, href.extract())
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)
        for hinfo in response.css('div.info-panel'):

            item = LianjiaSzItem()
            item['name'] = hinfo.css('div.col-1 h2 a').xpath('text()').extract()[0]
            item['region'] = hinfo.css('div.where span.region').xpath('text()').extract()[0]

            area_list = hinfo.css('div.area').xpath('text()').extract()[0].split()
            tmp = hinfo.css('div.area span').xpath('text()').extract()
            if bool(tmp):
                area_list.append(tmp[0])
            else:
                area_list.append("")
            astr = ""
            for i in area_list:
                astr += i
            item['area'] = astr
            item['other'] = hinfo.css('div.other span').xpath('text()').extract()
            item['type'] = hinfo.css('div.type span').xpath('text()').extract()

            alist = hinfo.css('div.price div.average').xpath('text()').extract()
            tmp = hinfo.css('div.price div.average span.num').xpath('text()').extract()
            if bool(tmp):
                num = tmp[0]
                item['price'] = alist[0].split() + num.split() + alist[1].split()
            else:
                item['price'] = alist[0].split()
            yield item
    # def parse_dir_contents(self, response):
        # for sel in response.xpath('//ul/li'):
        #     item = DmozItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item