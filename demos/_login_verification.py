#登陆验证
from random import randint as r_t
from time import sleep as s_p
islogin = False
def login():
    '''鉴定验证码和账户密码是否正确'''
    log_string = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    while True:
        sum_ran = ''
        for i in range(6):
            ran = r_t(0, len(log_string)-1)
            sum_ran = sum_ran + log_string[ran]    
        username = input('请输入您的账户: ')
        password = input('请输入您的密码: ')
        user_sum_ran = input(f'您的验证码是:{sum_ran}\n请输入验证码: ') 
        if user_sum_ran.lower() == sum_ran.lower():
            if username == 'admin' and password == '5201314LYX':
                return True
                break
            else:
                print('账户或密码错误,请重新输入!')
                continue
        else:
            print('验证码错误,请重新输入!')
            continue

def login_required(func):
    '''
    此装饰器判断用户是否登录,若未登录,则跳转至登陆界
    面,登录成功后,则运行目标函数;需要携带一个支付金额的
    参数
    '''
    def inner_login_required(number):
        global islogin
        while True:
            if islogin:
                func(number)
                break
            elif islogin == False:
                islogin = login()
    return inner_login_required

@login_required
def pay_money(num):
    '''用户支付'''
    print('正在支付中')
    sum_pt = ''
    for i in range(50):
        print(sum_pt)
        s_p(0.1)
        sum_pt += '■'
    print('\n成功支付了{0}元'.format(num))

pay_money(10)
pay_money(100)
pay_money(1000)