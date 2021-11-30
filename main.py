#!/usr/bin/env python3
# -*- conding: UTF-8 -*-

from libs import CompanyName
from libs import Chinese
from libs import Rules1
from libs import Rules2
from libs import Rules3
import datetime
import sys


if __name__ == '__main__':
	Str = sys.argv[1]
	if '.' in Str:
		if Str.count('.') >= 2:
			Str = Str[Str.index('.')+1:Str.index('.',Str.index('.')+1)]
		else:
			Str = Str[0:Str.index('.')]
	names = []
	if Chinese.is_chinese(Str):
		names = CompanyName.Company_name(Str)
	else:
		if '-' in Str:
			s = Str.split('-')
			for i in range(int(len(s)/2)):
				names.append(s[i].lower() + '-' + s[i+1].lower())
				names.append(s[i].upper() + '-' + s[i+1].upper())
				names.append(s[i].capitalize() + '-' + s[i+1].capitalize())
		else:
			names = [Str.lower(),Str.upper(),Str.capitalize()]
	dicts1 = Rules1.DictRules1Generate(names)
	dicts2 = Rules2.DictRules2Generate(names)
	dicts3 = Rules3.DictRules3Generate()
	dicts = dicts1 + dicts2 + dicts3
	filename = names[0] + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	for s in dicts:
		with open('%s.txt' % (filename),'a') as f:
			f.write(s + '\n')
	print('FileName: %s.txt' % (filename))