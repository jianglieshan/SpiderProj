#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

class MongoHelper(object):
	"""docstring for MongoHelper"""
	def __init__(self, arg):
		super(MongoHelper, self).__init__()
		self.arg = arg
		

if __name__ == '__main__':
	main()


# conn = MongoClient('192.168.0.113', 27099)
# db = conn.mydb  #连接mydb数据库，没有则自动创建
# my_set = db.test_set　　#使用test_set集合，没有则自动创建

# my_set.insert({"name":"zhangsan","age":18})
# #或
# my_set.save({"name":"zhangsan","age":18})