file = open('/home/zxx/桌面/72.docx','r')
for eachLine in file.readlines():
    if str(eachLine)[0] == '#':
        continue
    else:
        print (eachLine,end='')
file.close()
