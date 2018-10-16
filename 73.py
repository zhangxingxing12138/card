file = open('/home/zxx/桌面/73.docx')
test=file.read()
test2=list(test)
test2.sort()#对列表进行排序
for i in test2:
    print(i)
file.close()
    
