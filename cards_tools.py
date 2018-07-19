card_list=[]
def show_menu():
    print("*"*60)
    print("欢迎使用【菜单管理系统】v1.0\n")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 60)

def new_card():
    print("-" * 60)
    print("功能：新建名片")
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入qq号码:")
    email = input("请输入邮箱:")
    card_dict = {"name": name,"phone": phone,"qq": qq,"email": email}
    card_list.append(card_dict)
    print(card_list)
    print("成功添加%s的名片"%card_dict["name"])

def show_all():
    print("="*60)
    print("功能:显示全部")
    if len(card_list)==0:
        print("提示:没有任何名片纪录")
        return
    for name in ["姓名","电话","qq","邮箱"]:
        print(name,end="\t\t")
    print()
    print("=" * 60)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))

def search_card():
    print("-"*50)
    print("功能:搜索名片")
    find_name = input("请输入要搜索的内容:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("-" * 40)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
            print("-" * 40)
            break
        else:
            print("没有找到 %s" % find_name)
    
    def input_card_info(dict_value,tip_message):
        result_str = input(tip_message)
        if len(result_str)>0:
            return result_str
        else:
            return dict_value

    def deal_card(find_dict):
        print(find_dict)
        action_str = input("请选择要执行的操作""[1] 修改 [2]删除[0]返回上级菜单")
        action = int(action_str)    
        if action == 1:
            find_dict["name"] = input_card_info(find_dict['name'],"请输入姓名：")
            find_dict["phone"] = input_card_info(find_dict['phone'],"请输入电话：")
            find_dict["qq"] = input_card_info(find_dict['qq'],"请输入QQ：")
            find_dict["email"] = input_card_info(find_dict['email'],"请输入邮件：")

            print("%s 的名片修改成功" % find_dict["name"])
        elif action == 2:
            card_list.remove(find_dict)
            print("删除成功")
    deal_card(card_dict)
 
    
