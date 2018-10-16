student_infos=[]
def print_menu():
    print('*'*20)
    print('学生管理系统V1.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示学生信息')
    print('0.退出系统')
    print('*'*20)
def add_info():
    new_name = input('请输入学生姓名')
    new_sex = input('请输入学生性别')
    new_phone=input('请输入学生电话')
    new_infos={}
    new_infos['name']=new_name
    new_infos['sex']=new_sex
    new_infos['phone']=new_phone
    student_infos.append(new_infos)
def del_info(student):
    del_number = int(input('请输入要删除的序列号')) - 1
    del student[del_number]

def modify_info():
    student_id = int(input('请输入要修改的学生的序号:'))
    new_name = input('请输入新学生的名字:')
    new_sex = input('请输入新学生性别:(男/女)')
    new_phone = input('请输入新学 生的手机号:')
    student_infos[student_id-1]['name'] = new_name
    student_infos[student_id-1]['sex'] = new_sex
    student_infos[student_id-1]['phone'] = new_phone
def show_infos():
    print('='*30)
    print('学生信息如下:')
    print('='*30)
    print('序号 姓名  性别   手机号')
    i=1
    for temp in student_infos:
        print(' %d    %s   %s    %s  '%(i,temp['name'],temp['sex'],temp['phone']))
        i+=1    

def main():
    while True:
        print_menu()
        key = input('请输入对应的数字:')
        if key == '1':
            add_info()
        elif key == '2':
            del_info(student_infos)
        elif key == '3':
            modify_info()
        elif key == '4': 
            show_infos()
        elif key == '0':
            quit_confirm = input('请,真的要退出么?(Yes or No):')
            if quit_confirm == 'Yes':
                break 
            else:
                print('输入有误,请重新输入')

main()
