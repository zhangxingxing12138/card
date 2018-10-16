print('为了您和他人的安全，严禁酒后驾车！')
number=float(input('请输入每100毫升血液的酒精含量'))
if number > 20:
    if number >=20 and number < 80:
        print('已经达到酒后驾驶标准，请不要开车')
    else:
        print('已经达到醉酒驾驶的标准，请千万不要开车！')
else:
    print('您还不构成饮酒行为，可以开车，但要注意安全')
