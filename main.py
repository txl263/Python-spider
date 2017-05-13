# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
import time
#from job_model import Job
import peewee
import sys

class JobSpider:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseUrl = 'http://www.baidu.com'
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#
        op=Options()
        op.add_argument('user-data-dir=/Volumes/MAC_DATA_USB/Eric/Library/Application Support/Google/Chrome/Default')
        dr=webdriver.Chrome(chrome_options=op)
	def __int__(self):
		self.city_map ={}
		driver = self.driver

		driver.get(self.baseUrl)
		time.sleep(0.5)






if __name__=="__main__":
    spider=JobSpider()
    