print('定制自己的手机套餐:')
def phone_time():
    print('A.请设置通话时长:')
    list_time = ['1.0分钟','2.50分钟','3.100分钟','4.300分钟','5.不限量']
    for i in list_time:
        print(i)    
    a=int(input('输入选择的通话时间编号:'))
    if a == 1:
        d= '0分钟'
    elif a == 2:
        d='50分钟'
    elif a == 3:
        d= '100分钟'
    elif a == 4:
        d='300分钟'
    elif a == 5:
        d='不限量'
    print('B.请设置流量:')
    list_liuliang=['1.0M','2.500M','3.1G','4.5G','5.不限量']
    for i in list_liuliang:
        print(i)
    b=int(input('输入选择的通话时间编号:'))
    if b == 1:
        e='0M'
    elif b == 2:
        e='500M'
    elif b == 3:
        e='1G'
    elif b == 4:
        e='5G'
    elif b == 5:
        e='不限量'
    print('C.请设置短信条数:')
    list_message=['1.0条','2.50条','3.100条']
    for i in list_message:
        f=print(i)
    c=int(input('输入选择的通话时间编号:'))
    if c == 1:
        f='0条'
    elif c == 2:
        f='50条'
    elif c == 3:
        f='100条'
    print('您的手机套餐定制成功：免费通话时长为%s/月，流量为%s/月，短信条数为%s/月'%(d,e,f)) 
phone_time()    
