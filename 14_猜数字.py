# 产生随机数的工具
import random

# 需要人输入的数字player
player = int(input('请输入数字:'))

#  电脑输入的数字
computer = random.randint(1,10)

if player == computer:
   print('胜利了,今天晚上栋栋陪你')
else:
   print('栋栋说:你是一个loser')


