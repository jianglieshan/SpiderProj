from pydal import DAL, Field
#from items import *

class DbHelper(object):
	"""docstring for DbHelper"""
	def __init__(self, arg):
		super(DbHelper, self).__init__()
		self.arg = arg
		self.db = DAL('mongodb://140.143.247.178:27099/spider')
		self.define_table()
		'''
		self.db.thing.insert(name='Chair')
		query = self.db.thing.name.startswith('C')
		rows = self.db(query).select()
		print(rows[0].name)
		self.db.commit()
		'''

	def define_table(self):
		print(self.db._dbname)
		self.db.define_table('douban_topic',Field('title'),Field('title_url'),Field('people'),Field('people_url')
                             ,Field('replay_num'),Field('post_time'))

	def insert_models(self,table_name='',items=[]):
		a = list(map(dict,items))
		self.db.douban_topic.bulk_insert(a)
		self.db.commit()

	# def test_insert(self):
	# 	model = DoubanTopic({"title":"test"})
	# 	self.insert_models("",[model])


douban_db = DbHelper('')
#douban_db.test_insert()

# if __name__ == '__main__':
# 	db = DbHelper('')
# 	db.test_insert()
	# db.create_table()
	# db.insert_models()