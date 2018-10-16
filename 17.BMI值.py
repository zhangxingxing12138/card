height = 1.75#小明的身高/米
weight = 80.5#小明的体重/千克
BMI = weight/(height*height)
B = float(BMI)
if B < 18.5:
    print('过轻')
elif B >= 18.5 and B < 25:
    print('正常')
elif B >= 25 and B < 28:
    print('过重')
elif B >= 28 and B < 32:
    print('肥胖')
else:
    print('严重肥胖')
