#!/usr/bin/env python3
# -*- conding: UTF-8 -*-

def DictRules3Generate():
	lis = []
	f = open('dicts/top200.txt')
	lis = f.readlines()
	f.close()
	for i in range(len(lis)):
		lis[i] = lis[i].strip()
	return lis