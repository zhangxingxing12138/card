class Credit:
    def __init__(self,cardNum,password = "123456"):
        self.cardNum=cardNum
        if password =="123456":
            print("信用卡" + cardNum + "的默认密码为" + password)
        else:
            print("重置信用卡" + cardNum + "的密码为" + password)
card=Credit("4013735633800642",'598611')

