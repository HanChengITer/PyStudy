# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re

class HTMLParser(object):
	def __get_useful_data_dict(self, html_url, html_content, html_encode):
		data_dict = {}
		data_dict['url'] = html_url
		soup = BeautifulSoup(html_content,'html.parser',from_encoding=html_encode)
		data_dict['title'] = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title").find('h1').get_text()
		
		data_dict['content'] = soup.find('div',attrs={"class" : "lemma-summary","label-module" : "lemmaSummary"}).get_text()
		return data_dict
		
	def __get_new_urls_list(self, html_content, html_encode):
		url_list = []
		soup = BeautifulSoup(html_content,'html.parser')
		new_urls_list_nodes_list = soup.find_all('a',target="_blank",href=re.compile(r'/item/.*'))
		for new_urls_list_node in new_urls_list_nodes_list:
			url_list.append(''.join(['https://baike.baidu.com',new_urls_list_node['href']]))
		return url_list

	def parse(self, html_url, html_content, html_encode):
		useful_data_dict = self.__get_useful_data_dict(html_url, html_content, html_encode)
		urls_list = self.__get_new_urls_list(html_content, html_encode)
		return useful_data_dict,urls_list