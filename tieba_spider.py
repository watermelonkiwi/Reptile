#-*- coding:utf-8 -*-
# 识别中文注释
import urllib2

def load_page(url):
	'''
		发送URL请求
		返回url请求的静态html页面
	'''

	user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0"
	headers = {"User-Agent":user_agent}

	req = urllib2.Request(url, headers = headers)

	response = urllib2.urlopen(req)
	
	html = response.read()
	
	return html

def write_to_file(file_name, txt):
	'''
		  将txt文本，存入到file_name文件中
	'''
	# 1 打开文件
	f = open(file_name,'w')
	# 2 读写文件
	f.write(txt)
	# 3 关闭文件
	f.close()


def tieba_spider(url, begin_page, end_page):

	'''
		贴吧小爬虫	
	'''
	# i = 1, pn = 0
	# i = 2, pn = 100
	# i = 3, pn =150
	#...

	for i in range(begin_page, end_page+1): 
		pn = 50 * (i - 1)

		#组成一个完整的url
		my_Url = url + str(pn)
		#print "请求的地址"
		#print my_Url

		html = load_page(my_Url)
		
		print "=================== 第 %d============"%(i)
		print html
		print "====================================="
		file_name = str(i) + ".html"
		write_to_file(file_name, html)

#main
if __name__ == "__main__":
	url = raw_input("请输入贴吧的url地址")
	#print url
	begin_page  = int(raw_input("请输入起始页码："))
	end_page = int(raw_input("请输入终止页码："))

	#print begin_page
	#print end_page

	tieba_spider(url, begin_page,end_page)

