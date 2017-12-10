# -*- coding:utf-8 -*-
from urlManager import URLManager
from htmlDownloader import HTMLDownloader
from htmlParser import HTMLParser
from resultManager import ResultManager

class SpiderManager(object):
	def __init__(self):
		self.url_manager = URLManager()
		self.html_downloader = HTMLDownloader()
		self.html_parser = HTMLParser()
		self.result_manager = ResultManager()
	
	
	def crawl(self,url):
		count = 1
		self.url_manager.add_new_url(url)
		while self.url_manager.has_new_url():
			try:
				new_url = self.url_manager.get_new_url()
				html_content = self.html_downloader.download(new_url)
				des_data, new_urls = self.html_parser.parse(new_url, html_content, 'utf-8')
				self.url_manager.add_new_urls(new_urls)
				self.result_manager.add_data(des_data)
				print("crawl %s html successed" % count)
			except:
				print("crawl %s html failed" % count)
				continue
			finally:
				count += 1
				if count > 50:
					break
			
		self.result_manager.output_result()