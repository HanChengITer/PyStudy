# -*- coding:utf-8 -*-
from spiderManager import SpiderManager

if __name__ == "__main__":
	root_url = r'https://baike.baidu.com/item/%E4%BA%94%E9%99%A9%E4%B8%80%E9%87%91/637098?fr=aladdin'
	# root_url = r'https://baike.baidu.com/item/Python/407313'
	spider_manager = SpiderManager()
	spider_manager.crawl(root_url)