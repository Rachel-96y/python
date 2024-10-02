from random import randint as rt
class ShuZi:
	'''取随机数(start到stop)'''

	def __init__(self, start, stop, what, how):
		'''初始化start,stop,what和how的值'''
		self.start = start	#这是...
		self.stop = stop	#这是...
		self.what = what	#...
		self.how = how		#....

	def how_much(self):
		'''方法how_much()用于给出所选值重复次数'''
		list_suiji = []
		for i in range(self.how):
			list_suiji.append(rt(self.start, self.stop))
		print(tuple(list_suiji))
		ok = list_suiji.count(self.what)
		return ok 




