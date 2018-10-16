class Game(object):
    num=0
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod
    def show_help():
        print('=======帮助信息：让僵尸走进房间======')
    @classmethod
    def show_top_score(cls):
        print('********游戏最高分是%d*******'%cls.top_score)
    def start_game(self):
        print('%s开始游戏。。。哒哒哒哒'%self.player_name)
        Game.top_score=987
        Game.num+=1
Game.show_help()
Game.show_top_score()
game1 = Game('小明')

game1.start_game()
game2=Game('小红')
game2.start_game()
game3=Game('小白')
game3.start_game()
Game.show_top_score()
print(Game.num)
