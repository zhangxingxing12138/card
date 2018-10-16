list_jishu =input('请输入一个列表:')

def list_jishuquzhi():
    n= len(list_jishu)
    
    if n%2!=0:
        
        m=int((n-1)/2)
        num = list_jishu[m]
        print(num)          
list_jishuquzhi()
            
