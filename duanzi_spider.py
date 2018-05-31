#-*- coding:utf-8 -*-
import urllib2
import re

class Spider:

	'''
		这是一个内涵段子吧的一个爬虫类
	'''

	def __init__(self):
		self.enable = True
		self.page = 1 #当前要爬去的页数 

	def load_page(self, page):
		'''
			发送内涵段子url请求，得到html源码
		'''
	
		url = "http://www.neihan8.com/article/list_5_"+str(page)+".html" 
		user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:21.0) Geco/20130331 Firefox/21.0"
		headers = {"User-Agent":user_agent}

		req = urllib2.Request(url, headers = headers)

		response = urllib2.urlopen(req)

		html = response.read()
	 
	 	new_html = html.decode("gbk").encode("utf-8")

		#用正则表达式进行过滤，得到所有的段子
		#所有段子在<div class="f18 mb20">--------------- </div>

	#创建正则表达式对象
		pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S) 
		item_list = pattern.findall(new_html)


		return item_list

		#gbk_html = html.decode('gbk').encode('utf-8')
		#这个意识是现将网站的源码根据gbk进行解析，然后根据utf-8进行解析

	def deal_one_page(self, item_list, page):


		print "正在储存第%d页的段子。。" %(page)
		for item in item_list:
			print item.replace("<p>","").replace("</p>","").replace("<br />","").replace("&ldquo;","").replace("&rdquo;","").replace("&hellip","") 
	
			self.write_to_file(item)
		print " 第 %d 页的段子存储完毕。。" %(page)


	def write_to_file(self, txt):
		f = open('./myStory.txt', 'a')
		f.write(txt)
		f.write('-------------------------------------')
		f.close()


	def do_work(self):
		'''
			提供跟用户交互的过程
			让爬虫	去工作
		'''
		while self.enable:
			print "按回车继续"
			print "输出quit退出"
			command = raw_input()
			if(command == "quit"):
				self.enable = False
				break;
#			self.load_page(self.page)
			item_list = self.load_page(self.page)
			self.deal_one_page(item_list, self.page)
			self.page += 1


#main
if __name__ == "__main__":

#	begin_page = int(raw_input("起始页码："))
#	end_page = int(raw_input("终止页码："))
#创建一个spider对象
	mySpider = Spider()
	mySpider.do_work()

#	for i in range(begin_page, end_page):
#		n = i + 1


#	item_list = mySpider.load_page(1)
		

 	#	printem.replace("<p>","").replace("</p>","").replace("<b    r />","").replace("&ldquo;","").replace("&rdquo;","").replace("&hellip","")
	
	#	print item
