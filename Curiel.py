
x=range(4)
x=range(0,11,5)

print(x)
print(list(x))
name=str("lainliyong")

def pinfencanfei(jine,xioafei,num):
    return jine/num+xioafei/num

def  conputermianji(withe,hight):
    return withe*hight
def cmpputerchouchang(withe,hight):
    return withe*2+hight*2


def xiaofei():
    print("请输入金额")
    jine = input()
    print("请输入小费")
    xiaofei = input()
    print("请输入分摊人数")
    num = input()
    print(pinfencanfei(float(jine), float(xiaofei), int(num)))




def choose():
    print("选择你的程序  1 计算 小费 2 计算面积 3 计算周长")
    chooseint= input()

    if int(chooseint) == 1:
        xiaofei()
        choose()
    else:
        print("未开发")
        choose()







if __name__ == '__main__':
    choose()








