def Zodiac(month,day):
    n=('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座')
    d=(20,19,21,20,21,22,23,23,23,24,23,22)
    if day<d[month-1]:
        return n[month - 1]
    else:
        return n[month]
month = input('请输入月份（例如：5）：')
day = input('请输入日期（例如：17）：')
print(str(month)+'月'+str(day)+'日'+'星座为：'+Zodiac(int(month), int(day)))

