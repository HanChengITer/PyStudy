# -*- coding:utf-8 -*-
'''
官网
	https://xlsxwriter.readthedocs.io/
'''
import xlsxwriter

def get_data_dict():
	return {
		"title": [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期天'],
		"buname": [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道',],
		"data": [
			[1,2,3,4,5,6,7],
			[2,3,4,5,6,7,8],
			[3,4,5,6,7,8,9],
			[4,5,6,7,8,9,10],
			[5,6,7,8,9,10,11],
		],
		"addition_data_dict": {
			"title": u'平均流量',
			"direction": "column",
			"formula": "AVERAGE"
		}
	}

def get_format_dict(workbook):
	# 单元格格式
	# https://xlsxwriter.readthedocs.io/format.html
	
	# 设置标题单元格格式
	title_cell_format = workbook.add_format()
	title_cell_format.set_border(1)
	title_cell_format.set_bg_color('#cccccc')
	title_cell_format.set_align('center')
	title_cell_format.set_bold()
	
	# 设置内容单元格格式
	content_cell_format = workbook.add_format()
	content_cell_format.set_border(1)
	
	# 设置平均值单元格格式
	avg_cell_format = workbook.add_format()
	avg_cell_format.set_border(1)
	avg_cell_format.set_num_format('0.00')
	
	return {
		"title_cell_format": title_cell_format,
		"content_cell_format": content_cell_format,
		"avg_cell_format": avg_cell_format
	}
	
def write_content_data(worksheet, data_dict, format_dict):
	worksheet.write_row('A1', data_dict['title'], format_dict['title_cell_format'])
	worksheet.write_column('A2', data_dict['buname'], format_dict['content_cell_format'])
	for index in range(0, len(data_dict['data'])):
		data_list = data_dict['data'][index]
		worksheet.write_row('B'+str(index+2), data_list, format_dict['content_cell_format'])

def write_additional_data(worksheet, data_dict):
	# 公式大全
	# 	https://xlsxwriter.readthedocs.io/working_with_formulas.html
	# 	https://en.excel-translator.de/functions/
	# 	https://msdn.microsoft.com/en-us/library/dd907480(v=office.12).aspx
	addition_data_dict = data_dict["addition_data_dict"]
	add_title_cell_position = 123
	if addition_data_dict["direction"] == "column":
		# >>> chr(65)
		# 'A'
		# >>> ord('A')
		# 65
		pass

def get_chart(workbook, worksheet, data_dict):
	# 图表相关
	# https://xlsxwriter.readthedocs.io/chart.html
	chart = workbook.add_chart({'type':'column'})
	for index in range(2, len(data_dict['buname'])+2):
		chart.add_series({
			"categories": '=' + worksheet.name + '!$B$1:$H$1', # X轴标签名
			"values": '=' + worksheet.name + '!$B$' + str(index) + ':$' + chr(65+len(data_dict["title"])-1) + '$' + str(index), # 值的区间
			"line": {'color':'black'}, # 线条颜色
			"name": '=' + worksheet.name + '!$A$' + str(index) # 设置图例项
		})
	# chart.set_table() # 设置X轴表格格式
	# chart.set_style(30) # 设置图标样式
	chart.set_size({"width": 577, "height": 287}) # 设置图表大小
	chart.set_title({"name": u"业务流量周报图表"}) # 设置图表大标题（上方）
	chart.set_y_axis({"name": "Mb/s"}) # 设置Y轴小标题（左侧）
	return chart

if __name__ == "__main__":
	xlsx_demo = r'E:\yc_study\github\PyStudy\xlsx_demo\demo.xlsx'
	workbook = xlsxwriter.Workbook(xlsx_demo)
	test_sheet = workbook.add_worksheet('Test')
	# print(test_sheet.name) # 'Test'
	data_dict = get_data_dict()
	format_dict = get_format_dict(workbook)
	write_content_data(test_sheet, data_dict, format_dict)
	test_sheet.insert_chart('A'+str(len(data_dict['buname'])+3), get_chart(workbook, test_sheet, data_dict))
	workbook.close()