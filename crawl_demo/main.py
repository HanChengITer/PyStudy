# -*- coding:utf-8 -*-
from spiderManager import SpiderManager

if __name__ == "__main__":
	'''
	爬取百度百科关于五险一金的相关词条100条
	环境：
		python 3
	必备库：
		requests
		BeautifulSoup
	'''
	root_url = r'https://baike.baidu.com/item/%E4%BA%94%E9%99%A9%E4%B8%80%E9%87%91/637098?fr=aladdin'
	spider_manager = SpiderManager()
	spider_manager.crawl(root_url,100)