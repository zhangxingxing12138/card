import random
player = int(input('玩家输入的数字'))
computer = random.randint(1,10)
if player == computer:
    print('胜利')
else:
    print('失败，你是一个loser')
