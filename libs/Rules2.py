#!/usr/bin/env python3
# -*- conding: UTF-8 -*-

from libs import Character

"""
PassWord Rules2:
公司名 + ABC / ABCD / ABCDE / ABCDEF / @ABC / @ABCD / @ABCDE / AAA / @AAA / @AAAA / @AAAAA
"""
def DictRules2Generate(names ,level = 0):
	Specials = Character.SpecialCharacter(level)
	numbers = [123 ,1234 ,12345 ,123456 ,456 ,4567 ,45678 ,654 , 7654, 87654 ,789 ,987 ,321]
	dicts = []
	#公司名 + ABC / ABCD / ABCDE / ABCDEF
	for name in names:
		for num in numbers:
			dicts.append(name + str(num))

	#公司名 + 特殊字符 + ABC / ABCD / ABCDE / ABCDEF
	for name in names:
		for specials in Specials:
			for num in numbers:
				dicts.append(name + specials + str(num))
	#公司名 + AAA
	for name in names:
		for num in range(10):
			AAA = '{0}{0}{0}'.format(str(num))
			dicts.append(name + specials + AAA)

	#公司名 + 特殊字符 + AAA
	for name in names:
		for specials in Specials:
			for num in range(10):
				AAA = '{0}{0}{0}'.format(str(num))
				dicts.append(name + specials + AAA)

	#公司名 + 特殊字符 + AAAA
	for name in names:
		for specials in Specials:
			for num in range(10):
				AAA = '{0}{0}{0}{0}'.format(str(num))
				dicts.append(name + specials + AAA)

	#公司名 + 特殊字符 + AAAAA
	for name in names:
		for specials in Specials:
			for num in range(10):
				AAA = '{0}{0}{0}{0}{0}'.format(str(num))
				dicts.append(name + specials + AAA)

	return dicts