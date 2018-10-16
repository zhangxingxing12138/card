number = 1234567890123456#定义的银行账号
passwd = 123456#定义的密码
money = 1000#定义的金额
n =int(input('输入账号'))
p =int(input('输入密码'))
if n == number and p == passwd:
    print('密码正确，请输入取款金额')
    in_money=int(input())
    balance=money-in_money
    if balance >= 0:
        print('您已支取%d元，剩余%d元'%(in_money,balance))
    else:
        print('金额不足')
else:
    print('非法账户')


