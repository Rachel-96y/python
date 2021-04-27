import os
class fib_all:
	"""斐波那契数列第n项的值以及前n项和"""
	def __init__(self, n):
		"""得到需要计算到多少项"""
		self.n = n
		if self.n <= 0 or self.n >= 101:
			raise Exception
	
	def fib(self):
		"""得到各项的值"""
		a = 0
		b = 1
		x = 0
		while x < self.n:  
			yield a
			a, b = b, a + b
			x += 1

	def set_list(self):
		"""创建的数列"""
		answer = self.fib()
		list_1 = []
		for i in range(self.n):
			list_1.append(answer.__next__())
		return list_1

	def result_sum(self):
		"""求前n项和"""
		answer = self.set_list()
		result = sum(answer)
		return result

	def value(self):
		"""求第n项的值"""
		answer = self.set_list()
		return answer[-1]
	
	def all(self):
		"""显示所有数列"""
		result = ''
		answer = self.set_list()
		for i in answer:
			i = str(i)
			result = result + ',' + i
		result = result.lstrip(',')
		return result

def main():
	"""主函数"""
	try:
		answer = int(input('斐波那契数列的项数: '))
		new_project = fib_all(answer)
	except Exception:
		print('输入的值必须是大于\'0\'的正整数!并且项数不能超过100!!')
	else:
		answer_1 = new_project.result_sum()
		answer_2 = new_project.value()
		answer_3 = new_project.all()
		print('前%d项和是:%d,第%d项值是:%d' %(answer, answer_1, answer, answer_2))
		print('斐波那契数列的前%d项: %s' %(answer, answer_3))
	os.system('pause')

if __name__ == '__main__':
	main()