# -*- coding:utf-8 -*-

class ResultManager(object):
	def __init__(self):
		self.data_dict_list = []
	
	def add_data(self,des_data):
		self.data_dict_list.append(des_data)
	
	def output_result(self):
		with open('result.html','w',encoding='utf-8') as fout:
			fout.write('<html>\n')
			
			fout.write('<head>\n')
			fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
			fout.write('</head>\n')
			
			fout.write('<body>\n')
			fout.write('<table>\n')
			
			for data_dict in self.data_dict_list:
				fout.write('<tr>\n')
				fout.write('<td>%s</td>\n' % data_dict['title'])
				# fout.write('<td>%s</td>\n' % data_dict['url'])
				fout.write('<td>%s</td>\n' % data_dict['content'])
				fout.write('</tr>\n')
			
			fout.write('</table>\n')
			fout.write('</body>\n')
			
			fout.write('</html>')