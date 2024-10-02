import os
file_name = open(r"E:\study\python\myTest\demos\_import this.txt")
answer = file_name.readable()

def encodings(example):
	'''装饰器外层,有一个English用于参考'''
	s1 = ''
	s2 = ''
	sum2 = []
	English = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
	def inner_encode():
		nonlocal s1, s2
		'''装饰器内层,提取汉字'''
		sum1 = example()
		sum1 = list(sum1)
		i = 0
		while i < len(sum1):			
			if sum1[i] not in English:
				sum2.append(sum1.pop(i))
				continue
			i += 1
		for i in sum1:
			s1 = s1 + i
		for i in sum2:
			s2 = s2 + i
		return s1, s2
	return inner_encode

@encodings
def work():
	'''这是一个用于更改文件内容的程序'''
	file_info = file_name.readlines()
	sum = ''
	for index, i in enumerate(file_info):
		if '\n' in i:
			file_info[index] = file_info[index].replace('\n', '')
		file_info[index] = file_info[index].replace(' ', '')
		sum += file_info[index]
	return sum

if answer == True:
	last_answer = work()
	for i in last_answer:
		print(i)
else:
	print('FBI WORNING: 您的文件无法更改其内容')
os.system('pause')