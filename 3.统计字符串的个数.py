while True :
    string = input('请输入一串字符')
    count = 0
    for i in range(len(string)):
        if string[i] in ['0','1','2','3','4','5','6','7','8','9']:
            count+=1
    print(count)
    break
