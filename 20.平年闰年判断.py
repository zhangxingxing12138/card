date = int(input('输入的年份:'))
if date%4 == 0 and date%100 != 0 or date%400 == 0:
    print('这年是闰年')
else:
    print('这年不是闰年')
