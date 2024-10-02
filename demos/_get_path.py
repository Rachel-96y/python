import os
import getpass
import socket
first_name = getpass.getuser()
last_name = socket.gethostname()
full_name = f'{first_name}.{last_name}'

#os.mkdir(r"c:\users\%s\desktop\news" %(full_name))