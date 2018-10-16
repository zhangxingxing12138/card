a=float(input('请输入收入金额'))
i=a-3500
if i<0:
    print('不需要缴纳个人所得税，实际收入为%d'%a)
elif 0<i<1500:
    j=i*0.03
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
elif 1500<i<4500:
    j=i*0.1
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
elif 4500<i<9000:
    j=i*0.2
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
elif 9000<i<35000:
    j=i*0.25
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
elif 35000<i<55000:
    j=i*0.3
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
elif 55000<i<80000:
    j=i*0.35
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
elif i>80000:
    j=i*0.45
    m=a-j
    print('缴纳个人所得税%d,实际收入%d'%(j,m))
