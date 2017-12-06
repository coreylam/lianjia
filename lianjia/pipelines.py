# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
# import codecs

class LianjiaPipeline(object):
    # def __init__(self):
        # self.file = codecs.open('data_cn.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        # self.file.write(line)

        with open('data_cn1.json', 'a') as f:
            json.dump(dict(item), f, ensure_ascii=False)
            f.write(',\n')
        return item

    def process_item(self, item, spider):
        return item