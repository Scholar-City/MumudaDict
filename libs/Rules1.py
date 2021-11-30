#!/usr/bin/env python3
# -*- conding: UTF-8 -*-

from libs import Character
from libs import Calendar

"""
PassWord Rules1:
公司名 + 年份 / 公司名 + 年份 + 特殊符号 / 公司名 + 特殊符号 + 年份
"""
def DictRules1Generate(names ,year = 2000 ,level = 0):
	years = Calendar.CalendarYear(year)
	Specials = Character.SpecialCharacter(level)
	dicts = []
	# 公司名 + 年份
	for name in names:
		for year in years:
			dicts.append(name + str(year))

	# 公司名 + 年份 + 特殊符号
	for name in names:
		for year in years:
			for specials in Specials:
				dicts.append(name + str(year) + specials)

	# 公司名 + 特殊符号 + 年份
	for name in names:
		for specials in Specials:
			for year in years:
				dicts.append(name + specials + str(year))
	return dicts