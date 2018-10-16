s=str(input('请输入一段字符:'))
def string_xiaoxie_num():
    
    for i in s:
        if s.islower()==True and s.isalnum()== True:
            print(True)
        else:
            print(False)
        break     
    
string_xiaoxie_num()
