# -*- coding:utf-8 -*-
import requests

class HTMLDownloader(object):
	def download(self,url):
		response = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})
		if int(response.status_code) == 200:
			return response.content