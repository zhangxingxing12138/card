def input_weight():
    height=float(input('请输入你的身高：'))
    if height<130 or height>250:
         
    
        ex=Exception('身高输入异常')
        raise ex
    weight=float(input('请输入你的体重'))
    weight_new=height-100
    if abs((weight_new-weight)/weight_new)<=0.05:
        print('体重正常')
    elif weight_new>weight:
        print('体重不达标')
    else:
        print('体重超标')
try:
    input_weight()
except ValueError:
    print('请输入正确的数字')
except Exception as ex :
    print('异常：{}'.format(ex))
    
