height =float(input('请输入身高:'))
price = float(input('请输入身价:'))
face =float(input('请输入颜值分:'))
if height > 180 and price > 1000000 and face > 99:
    print('高富帅')
if height < 180 and price > 1000000 and face > 99:
    print('富帅')
if height < 180 and  price < 1000000 and face > 99:
    print('帅')
if height < 160 and price < 100 and face < 60:
    print('矮穷矬')


