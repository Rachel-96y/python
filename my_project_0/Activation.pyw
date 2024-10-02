#序列号生成激活码
import os
import hashlib
answer = input('输入序列号： ')
class Finally_Value:
    """根据用户的序列号,生成对应的激活码"""
    @staticmethod
    def finally_value(result):
        """得到激活码的唯一值"""
        flag = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOASDFGHJKLZXCVBNM'
        value = 0
        length = len(result)
        for i in result:
            if i not in flag:
                value = 1
        if length != 128 or value == 1:
            return 'None'
        else:
            key = 'encryption_1024.HELLO_WORD' * 1024
            result = result + key
            finally_password = hashlib.sha512(result.encode('utf-8')).hexdigest()
            return finally_password

if __name__ == '__main__':
    activation_code = Finally_Value().finally_value(answer)
    print('激活码是：', activation_code)


