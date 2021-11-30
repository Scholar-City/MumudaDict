#!/usr/bin/env python3
# -*- conding: UTF-8 -*-

import datetime

'''
生成年份，默认从1900年生成到今年
'''
def CalendarYear(Year):
	year = datetime.datetime.now().year
	lis = [i for i in range(Year,year+1)]
	return lis