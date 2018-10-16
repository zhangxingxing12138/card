string = str(input('请输入字符串:'))
def string_pinjiezifuchuan():
    for i in string:
        s1= string[::2]
        s2=string[1::2]
        s=s1+s2
        break
    print(s)
string_pinjiezifuchuan()

