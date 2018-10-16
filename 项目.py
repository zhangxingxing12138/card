import re
import mysql.connector as c
import random
def u_passwd():
    while True:
        username = input('username:')
        passwd = input('passwd:')

        if passwd == 'www59861188' and username == 'zxx':
            print('密码输入正确,登陆成功')
            break
        else:
            print('用户输入错误')

def studentMenu():
    print("=" * 60)
    print("学生管理系统")
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、查询学生信息")
    print("4、修改学生信息")
    print("5、全部学生信息")
    print("6、退出")
    print("=" * 60)

def idinput(string):
    ID = input(string)
    pattern = re.compile("^\d{1,3}$")
    while not re.match(pattern, ID):
        ID = input("请输入1-3位整数:")
    return ID


def appendStudentInfo():
    ID = idinput("请输入学生学号：")
    db = c.connect(user="root", passwd="www59861188", db="stu_220")
    cursor = db.cursor()
    while cursor.rowcount > 0:
        ID = idinput("该学号已存在，请重新输入:")
        sql = "select * from stusys where ID = '%d'" % int(ID)
        cursor.execute(sql)
    name = input("请输入学生姓名：")
    exam_number = input('请输入准考证号')
    id_number = input('请输入身份证号')
    sex = input('请输入学生性别(男/女)')
    phone = input('请输入手机号')
    chinese = input("请输入语文成绩：")
    while not chinese.isdigit() or int(chinese) > 100 or int(chinese) < 0:
        chinese = input("输入错误，请重新输入：")
    math = input("请输入数学成绩：")
    while not math.isdigit() or int(math) > 100 or int(math) < 0:
        math = input("输入错误，请重新输入：")
    english = input("请输入英语成绩：")
    while not english.isdigit() or int(english) > 100 or int(english) < 0:
        english = input("输入错误，请重新输入：")
    total = int(chinese) + int(math) + int(english)
    grade_avg = total/3
    sql = """INSERT INTO stusys(ID,name,exam_number,id_number,sex,phone,chinese,english,math,total,grade_avg)
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (ID,name,exam_number,id_number,sex,phone,chinese,english,math,total,grade_avg))
    db.commit()


def delstudent():
    delstudentid = input("请输入要删除的学生学号：")
    if querystudent(delstudentid):
        select = input("是否删除：是(Y)/否（N）")
        if select == "Y" or select == "y":
            db = c.connect(user="root", passwd="www59861188", db="stu_220")
            cursor = db.cursor()
            sql = "delete from stusys where ID =%s" % delstudentid
            cursor.execute(sql)
            db.commit()
            db.close()
            print("删除成功")
        elif select == "N" or select == "n":
            print("取消删除")
        else:
            print("输入错误")


def querystudent(querystudentid):
    db = c.connect(user="root", passwd="www59861188", db="stu_220")
    cursor = db.cursor()
    sql = "select * from stusys where ID=%s" % querystudentid
    cursor.execute(sql)
    if cursor.rowcount == 0:
        print("不存在该学生信息")
        return False
    else:
        print("该学生信息如下：")
        results = cursor.fetchall()
        print("ID=%d,NAME=%s,Exam_number=%d,ID_number=%d,SEX=%s,PHONE=%d,CHINESE=%d,ENGLISH=%d,MATH=%d,TOTAL=%d,GRADE_AVG=%d" % \
              (results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5],results[0][6],results[0][7],results[0][8],results[0][9],results[0][10]))
        return True


def modifystudentifo():
    modifyid = input("请输入要修改的学生学号：")
    if querystudent(modifyid):
        name = input("请重新输入学生姓名：")
        exam_number = input('请输入准考证号')
        id_number = input('请输入身份证号')
        sex = input('请输入学生性别(男/女)')
        phone = input('请输入手机号')
        chinese = input("请重新输入语文成绩：")
        while not chinese.isdigit() or int(chinese) > 100 or int(chinese) < 0:
            chinese = input("输入错误，请重新输入：")

        math = input("请重新输入数学成绩：")
        while not math.isdigit() or int(math) > 100 or int(math) < 0:
            math = input("输入错误，请重新输入：")

        english = input("请重新输入英语成绩：")
        while not english.isdigit() or int(english) > 100 or int(english) < 0:
            english = input("输入错误，请重新输入：")

        total = int(chinese) + int(math) + int(english)
        grade_avg = total/3
        db = c.connect(user="root", passwd="www59861188", db="stu_220")
        cursor = db.cursor()
        sql1 = "update stusys set name ='%s' where id = %s" % (name, modifyid)
        cursor.execute(sql1)
        sql2 = "update stusys set exam_number ='%s' where id = %s" % (exam_number, modifyid)
        cursor.execute(sql2)
        sql3 = "update stusys set id_number ='%s' where id = %s" % (id_number, modifyid)
        cursor.execute(sql3)
        sql4 = "update stusys set sex ='%s' where id = %s" % (sex, modifyid)
        cursor.execute(sql4)
        sql5 = "update stusys set phone ='%s' where id = %s" % (phone, modifyid)
        cursor.execute(sql5)
        sql6 = "update stusys set math = %s where id = %s" % (math, modifyid)
        cursor.execute(sql6)
        sql7 = "update stusys set english = %s where id =%s" % (english, modifyid)
        cursor.execute(sql7)
        sql8 = "update stusys set total = %s where id = %s" % (total, modifyid)
        cursor.execute(sql8)
        sql9 = "update stusys set grade_avg ='%s' where id = %s" % (grade_avg, modifyid)
        cursor.execute(sql9)
        sql10 = "update stusys set chinese = %s where id = %s" % (chinese, modifyid)
        cursor.execute(sql10)
        db.commit()
        db.close()


def allinfo():
    db = c.connect(user="root", passwd="www59861188", db="stu_220")
    cursor = db.cursor()
    sql = "select * from stusys"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        ID = row[0]
        NAME = row[1]
        Exam_number = row[2]
        ID_number = row[3]
        SEX = row[4]
        PHONE = row[5]
        CHINESE = row[6]
        ENGLISH = row[7]
        MATH = row[8]
        TOTAL = row[9]
        GRADE_AVG = row[10]
        # 打印结果
        print("ID=%d,NAME=%s,Exam_number=%s,ID_number=%s,SEX=%s,PHONE=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,TOTAL=%s,GRADE_AVG=%s" % \
              (ID, NAME,Exam_number,ID_number,SEX,PHONE, CHINESE, ENGLISH, MATH, TOTAL, GRADE_AVG))




if __name__ == '__main__':
    u_passwd()
    while True:
        # yanzheng()
        studentMenu()
        menuindex = input("请输入选项序号：")
        while not menuindex.isdigit():
            menuindex = input("输入错误，请重新输入：")
        if int(menuindex) == 1:
            appendStudentInfo()
        elif int(menuindex) == 2:
            delstudent()
        elif int(menuindex) == 3:
            querystudentid = idinput("请输入要查询的学生学号：")
            querystudent(querystudentid)
        elif int(menuindex) == 4:
            modifystudentifo()
        elif int(menuindex) == 5:
            allinfo()
        elif int(menuindex) == 6:
            break
        else:
            print("输入序号无效")