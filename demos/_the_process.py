import multiprocessing  #3个python 2个c md
import time
def dog(a):
	for i in range(a):
		time.sleep(2)
		print('111')

def cat(b):
	for i in range(b):
		time.sleep(2)
		print('喵喵喵')


def cats(c):
	for i in range(c):
		time.sleep(2)
		print('333')

def first(d):
	for i in range(d):
		time.sleep(2)
		print('最开始')

if __name__ == '__main__':
	dog_process = multiprocessing.Process(target = dog, args = (3,))
	cat_process = multiprocessing.Process(target = cat, kwargs = {'b': 5})
	cats_process = multiprocessing.Process(target = cats, args = (4,))
	dog_process.start()
	first(5)
	cat_process.start()
	cats_process.start()