print('2017~2018赛季NBA西部联盟前8名:')
name_list=['火箭','勇士','开拓者','爵士','鹈鹕','马刺','雷霆','森林狼']
for index ,name in enumerate(name_list):
    if index%2==0:
        print()
        print(name,end='\t')
    else:
        print(name)
