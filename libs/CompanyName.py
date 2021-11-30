#!/usr/bin/env python3
# -*- conding: UTF-8 -*-

import pypinyin

'''
取出公司名五种组合,如下五种类型组合
ZhongShiHua
zhongshihua
ZHONGSHIHUA
ZSH
zsh
'''
def Company_name(Name):
	lis = []
	li = []
	s = ''
	'''
	公司名转变为拼音
	'''
	for s1 in Name:
		s2 = ''
		for i in pypinyin.pinyin(s1, style=pypinyin.NORMAL):
			s2 += ''.join(i)
			li.append(s2)

	#公司名头字母大写
	for i in range(len(li)):
		li[i] = li[i].capitalize()
		s += li[i]
	lis.append(s)
	s = ''

	#公司名全小写
	for i in range(len(li)):
		s += li[i].lower()
	lis.append(s)
	s = ''

	#公司名全大写
	for i in range(len(li)):
		s += li[i].upper()
	lis.append(s)
	s = ''

	#公司名首字母大写
	for i in range(len(li)):
		s += li[i][0:1].upper()
	lis.append(s)
	s = ''

	#公司名首字母小写
	for i in range(len(li)):
		s += li[i][0:1].lower()
	lis.append(s)


	return lis