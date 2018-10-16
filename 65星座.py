month=int(input('请输入月份(例如：5):'))
date= int(input('请输入日期(例如：17):'))
list_date=[(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22),(1,20),(2,19)]
zodic=['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']
in_date=(month,date)
for n,i in enumerate(list_date):
    if i<=in_date<list_date[n+1]:
        print('%d月%d日星座为：'%(month,date),zodic[n])
        break

