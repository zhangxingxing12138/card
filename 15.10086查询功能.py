print('您好，欢迎致电中国移动')
number = int(input('输入的号码为：'))
if number == 1:
    print('显示您当前余额为：19元')
elif number == 2:
    print('显示您当前流量为：10G') 
elif number == 3:
    print('显示您当前剩余通话分钟数为：50分钟')
else:
    print('请尝试输入1,2,3进行查询')
