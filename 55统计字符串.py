
a = str(input('请输入字符串:'))
def fun1_2(x): 

    x = x.lower()

    num = []

    dic = {}

    for i in x:

        if i.isdigit(): 

            num.append(i)

        else:   
            if i in dic:

                continue

            else:

                dic[i] = x.count(i)  

    new = ''.join(num)


    print ("the new numbers string is: " + new)

    print ("the dictionary is: %s" % dic)

fun1_2(a)
