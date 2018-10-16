import random
list1=[random.randint(1,1000) for i in range(10)]
print(list1)
num = 0
for i in list1:
    num+=i
    a = num / len(list1)

print(a)