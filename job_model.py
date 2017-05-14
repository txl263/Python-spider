# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from peewee import *

db = SqliteDatabase('jobs.db')

class Job(Model):
	company_id = IntegerField()
	position_id = IntegerField(unique=True)
	position_name = CharField() #职位描述
	salary_min = IntegerField() #薪水下限
	salary_max = IntegerField() #薪水上线
	company_name = CharField()	#公司名称
	exp = CharField()	#经验
	tags = CharField()	#标签
	industry = CharField()	#行业信息 公司信息
	summary = CharField()	#简介
	city = CharField()	#城市
	location = CharField()	#位置
	education = CharField()	#学历

	class Meta:
		database = db
