
try:
    score = int(input('请输入学生成绩'))
    assert (score<=100)&(score>=0),'分数不合理'
    if score >= 90:
        print('A 优秀')
    elif score >=80:
        print('B')
    elif score>=60:
        print('C')
            
    else:
        print('D')
           
except ValueError:
    print('请输入正确的数')

