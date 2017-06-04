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

    def is_element_exist(self,css):
        css_selector = css
        s = self.driver.find_elements_by_css_selector(css_selector)
        if len(s) == 0:
            print "元素未找到:%s"%css_selector
            return False
        elif len(s) == 1:
            return True
        else:
            print "找到%s个元素：%s"%(len(S),css_selector)
            return False

    def search(self,keyword=u'软件测试工程师'):
        self.driver.find_element_by_xpath("//input[@id='kwdselectid']").send_keys(keyword)
        self.driver.find_element_by_xpath("//*[@id='work_position_click']").click()
        self.driver.find_element_by_xpath('//*[@id="work_position_click_multiple_selected_each_010000"]').click()
        self.driver.find_element_by_xpath('//*[@id="work_position_click_center_right_list_category_000000_010000"]').click()
        self.driver.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()
        self.driver.find_element_by_xpath("//button[contains(.,'搜索')]").click()
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
        print self.end_page + "页"
        return self.end_page

    def goto_netxt_page(self):
        driver.find_element_by_xpath("//a[@id='rtNext']").click() #点击下一页
        time.sleep(5)

    def get_job_info_per_page(self):
        jobs_of_current_page = self.driver.find_elements_by_css_selector('div.el')
        print '每页' + str(len(jobs_of_current_page) - 10) + '个'
        job_count = len(jobs_of_current_page) - 10
        #//*[@id="resultList"]/div[3]
        #//*[@id="resultList"]/div[3]/span[1]/a
        #print dir(jobs_of_current_page)
        #print len(jobs_of_current_page)
        currentWin = self.driver.current_window_handle
        #print currentWin
        for x in xrange(1,job_count+1):
            print '第' + str(x) + '个职位'
            xpath = ".//*[@id='resultList']/div[" + str(x+2) + "]/p/span/a"
            position_name = self.driver.find_element_by_xpath(xpath).text
            print position_name

            xpath = ".//*[@id='resultList']/div[" + str(x+2) + "]/span[1]/a"
            company_name = self.driver.find_element_by_xpath(xpath).text
            print company_name

            xpath = ".//*[@id='resultList']/div[" + str(x+2) + "]/span[2]"
            District = self.driver.find_element_by_xpath(xpath).text         #区县
            print District

            xpath = ".//*[@id='resultList']/div[" + str(x+2) + "]/span[3]"
            salary = self.driver.find_element_by_xpath(xpath).text  
            print salary
            if salary.find('/') != -1 :
                #print '/的位置在' + str(salary.find('/'))
                if salary[salary.find('/')-1] == '千' :
                    #print '-的位置在' + str(salary.find('-'))
                    if salary[0:salary.find('-')-1] :
                        salary_min = salary[0:salary.find('-')] + 'K'
                        salary_max = salary[salary.find('-')+1:salary.find('千')] + 'K'
                    else:
                        salary_min = salary[0] + 'K'
                        salary_max = salary[salary.find('-')+1:salary.find('千')] + 'K'
                    print salary_min
                    print salary_max
                else: #如果薪水单位是万
                    #print '-的位置在' + str(salary.find('-'))
                    if salary[0:salary.find('-')-1] :
                        salary_min = str(float(salary[0:salary.find('-')])*10) + 'K'
                        salary_max = str(float(salary[salary.find('-')+1:salary.find('万')])*10) + 'K'
                    else:
                        salary_min = str(float(salary[0])*10) + 'K'
                        salary_max = str(float(salary[salary.find('-')+1:salary.find('万')])*10) + 'K'
                    print salary_min
                    print salary_max                    
            else:
                print ''
            self.driver.find_element_by_xpath(xpath).click()
            xpath = ".//*[@id='resultList']/div[" + str(x+2) + "]/p/span/a"
            self.driver.find_element_by_xpath(xpath).click()   #点击职位名称，打开新窗口显示职位详情
            time.sleep(2)
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != currentWin:
                    #print handle
                    self.driver.switch_to_window(handle)
                    try:
                        location = self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div[3]/div[5]/div/p').text
                        print location
                    except:
                        location = ''

                    count = len(self.driver.find_elements_by_xpath('html/body/div[2]/div[2]/div[3]/div[1]/div/div/span'))
                    print '一共' + str(count) + '个标签'
                    for x in xrange(1,count+1):
                        #print x
                        em_xpath = '/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[' + str(x) + ']/em'
                        lable_xpath = 'html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[' + str(x) + ']'
                        if self.driver.find_element_by_xpath(em_xpath).get_attribute('class') == 'i1':
                            exp_text = self.driver.find_element_by_xpath(lable_xpath).text                    #经验
                            print exp_text
                        elif self.driver.find_element_by_xpath(em_xpath).get_attribute('class') == 'i2':
                            education = self.driver.find_element_by_xpath(lable_xpath).text                   #学历
                            print education
                        elif self.driver.find_element_by_xpath(em_xpath).get_attribute('class') == 'i3':
                             Number_of_Recruitment = self.driver.find_element_by_xpath(lable_xpath).text      #招聘人数
                             print Number_of_Recruitment
                        elif self.driver.find_element_by_xpath(em_xpath).get_attribute('class') == 'i4':
                            pubdate = self.driver.find_element_by_xpath(lable_xpath).text                      #发布日期
                            print pubdate
                        elif self.driver.find_element_by_xpath(em_xpath).get_attribute('class') == 'i5':
                            language = self.driver.find_element_by_xpath(lable_xpath).text                     #外语要求
                            print language
                        elif self.driver.find_element_by_xpath(em_xpath).get_attribute('class') == 'i6':
                            speciality = self.driver.find_element_by_xpath(lable_xpath).text                   #学科要求
                            print speciality
                    #获取福利    
                    self.driver.close()

            self.driver.switch_to_window(currentWin)

        try:
            Job.create(company_id=company_id,District=District,position_name=position_name,
                salary_min=salary_min,salary_max=salary_max,company_name=company_name,
                exp=exp_text,education=education,tags=tags,industry=industry,summary=summary,
                city=self.city_name,location=location)
        except peewee.IntegrityError:
            print 'position %s, id = %s, already exists' %(position_name,position_id)


    def start(self):
        self.search(u'软件测试工程师')
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