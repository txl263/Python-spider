# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from job_model import Job
import peewee
import sys
op = Options()
op.add_argument('user-data-dir=/Volumes/MAC_DATA_USB/Eric/Library/Application Support/Google/Chrome/Default')

class JobSpider:
    def __init__(self):
        
        #driver = self.driver
        self.driver = webdriver.Chrome(chrome_options=op)
        #self.city_map = {}
        #self.driver = webdriver.chrome()
        #self.driver.implicitly_wait(30)
        self.baseUrl = 'http://www.51job.com/'
        self.driver.get(self.baseUrl)
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@id='kwdselectid']").send_keys("软件测试工程师")
        self.driver.find_element_by_xpath("//*[@id='work_position_click']").click()
        self.driver.find_element_by_xpath('//*[@id="work_position_click_multiple_selected_each_010000"]').click()
        self.driver.find_element_by_xpath('//*[@id="work_position_click_center_right_list_category_000000_010000"]').click()
        self.driver.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()
        self.driver.find_element_by_xpath("//button[contains(.,'搜索')]").click()

    def search(self,keyword=u'软件测试工程师'):
        #打开首页，输入搜索内容，然后点击按钮
        time.sleep(5)

    def select_city(self,city='beijing'):
        #selector = 'a[data-id=%s' %(self.city_map[city])
        #js = '$("$s").click()' %selector
        #self.dr.excute_scripts(js)
        self.set_city_name(city)
        self.city_name='beijing'
        time.sleep(5)

    def set_city_name(self,city='beijing'):
        city_name_map = {'beijing':'北京'}
        #self.city_name = city_name_map[city]
        self.city_name = 'beijing'

    def get_current_page(self):
        self.current_page = int(self.dr.find_element_by_xpath("").text)
        print('current page is %d' %self.current_page)
        return self.current_page

    def get_netxt_page(self):
        self.next_page = self.get_current_page + 1
        print ('next page is %d' %self.next_page)
        return self.next_page

    def has_next_page(self):
        next_page_btn = self.dr.find_element_by_xpath('.pager_next')
        disabled = 'pager netxt disabled' in next_page_btn.get_attribute('class')
        return not disabled

    def get_end_page(self):
        self.end_page = self.driver.find_element_by_xpath("//*[@id='resultList']/div[1]/div[4]").text
        self.end_page = self.end_page[-2:]
        print self.end_page
        return self.end_page

    def goto_netxt_page(self):
        self.dr.find_element_by_xpath('.pager_next').click()
        time.sleep(5)

    def get_job_info_per_page(self):
        jobs_of_current_page = self.dr.find_element_by_xpath('')
        for job in jobs_of_current_page:
            company_id = job.get_attribute('data-companyid')
            position_name = job.get_attribute('')
            position_id = job.get_attribute('')
            salary = job.get_attribute('')

        try:
            salary_min = int(salary[0].replace('k','').replace('K',''))
        except:
            salary_min = 0

        try:
            salary_max = int(salary[-1].replace('k','').replace('K',''))
        except:
            salary_max = 0
        company_name = job.get_attribute('')
        exp = job.find_element_by_xpath('')
        education = exp[-1]
        exp_text = exp[0]
        tags = job.find_element_by_xpath('')
        industry = job.find_element_by_xpath('')
        summary = job.find_element_by_xpath('')
        location = job.find_element_by_xpath('')

        try:
            Job.create(company_id=company_id,position_id=position_id,position_name=position_name,
                salary_min=salary_min,salary_max=salary_max,company_name=company_name,
                exp=exp_text,education=education,tags=tags,industry=industry,summary=summary,
                city=self.city_name,location=location)
        except peewee.IntegrityError:
            print 'position %s, id = %s, already exists' %(position_name,position_id)


    def start(self):
        self.search(u'测试')
        # self.select_city(city_name)
        # print city_name
        end_page = self.get_end_page()
        self.get_job_info_per_page()
        while sef.has_next_page:
            self.goto_netxt_page()
            self.get_job_info_per_page()
            print 'current page is %s' %(self.get_current_page())
            if self.get_current_page() == end_page:
                break

    def end(self):
        print 'stoping'
        self.driver.quit()


if __name__=="__main__":
    spider = JobSpider()
    spider.start()
    spider.end()