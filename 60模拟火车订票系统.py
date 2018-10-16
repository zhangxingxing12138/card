list_train1=['车次\t\t','出发站-到达站\t\t\t','出发时间\t\t','到达时间\t\t','历时\n']
list_train2=['T40\t\t','长春-北京\t\t\t','00:20\t\t\t','12:20\t\t\t','12:08\n']
list_train3=['T298\t\t','长春-北京\t\t\t','00:06\t\t\t','10:50\t\t\t','10:44\n']
list_train4=['T158\t\t','长春-北京\t\t\t','12:48\t\t\t','21:06\t\t\t','08:18\n']
list_train5=['Z62\t\t','长春-北京\t\t\t','21:58\t\t\t','06:08\t\t\t','8:20\n']
for i in list_train1:
    print(i,end='') 
for i in list_train2:
    print(i,end='') 
for i in list_train3:
    print(i,end='') 
for i in list_train4:
    print(i,end='') 
for i in list_train5:
    print(i,end='')
a=input('请输入要购买的车次：')
b = input('请输入乘车人(用逗号分隔)：')
def list_train():
    c = str()
    if a == 'T40':
        c='00:20'
    elif a == 'T298':
        c='00:06'
    elif a == 'T158':
        c='12:48'
    elif a == 'Z2':
        c='21:58'
    print('你已购%s次列车  长春-北京 %s开，请%s尽快换取纸质车票。【铁路服务】'%(a,c,b)) 
list_train()
