import random
list_num = []
def num(b):
    for i in range(b):
        a = random.randint(0, 100)
        list_num.append(a)
    print(list_num)
    for i in range(b//2):
        list_num[b-1-i],list_num[i]=list_num[i],list_num[b-1-i]
    print(list_num)
num(5)

