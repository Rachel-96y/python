import os
import time
import random

class Test_1:
	"""用于测试的类"""
	name = '其实这是一个用于搞笑的测试O(∩_∩)O'
	def __init__(self, flag_1='▇', flag_2='▇'):
		"""初始化实例的属性"""
		self.flag_1 = flag_1
		self.flag_2 = flag_2
	def progress(self):
		"""用于测试的进度条"""
		for i in range(50):
			K = random.random()
			print(self.flag_1, end='')
			self.flag_1 = self.flag_1 + self.flag_2
			time.sleep(K)
			os.system('cls')
			print('\n\t\t   已完成:%d%s' %(i*2+2, '%'))

def main():
	"""主函数"""
	new_test = Test_1()
	new_test.progress()
	print('\n%s' %(new_test.name))
	os.system('pause')
	
if __name__ == '__main__':
	main()
	
