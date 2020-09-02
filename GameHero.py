import math
zhanghao='loginlogin'
name='玩家一'
paw='pwd'

jues=None
xueliang=100


def PRINTINFO():
    print('名字' +name)
    print(' 角色' + str(jues))
    print('血量' + str(xueliang))



def login():
    print("+++++++++++login++++++++++++'")
    print("你的账号")
    PRINTINFO()
    name2=input()
    if (name is None) or (name2 != str(name)):
        print("请输入正确的账号,或者注册账号")
        return main()

    print("你的密码")
    if (name is None) or (name2 != name):
        print("请输入正确的密码")
        return main()
    PRINTINFO()
    RunStart()

def zhuce():
    print("+++++++++++zhuce++++++++++++'")
    print("请输入你想要注册的账号")
    global zhanghao

    zhanghao=input()
    print("你的密码")
    global paw
    paw=input()

    print("请确认你的密码")
    paw2=input()
    if paw!=paw2:
        return zhuce()
    return main()




def main():
   print("""
   start  login ....
    1  登录 
    2 注册账号
   """)
   flag=input()
   if int(flag)==1 :
       login()
   elif int(flag)==2 :
        zhuce()
   else:
       main()





def RunStart():
    print("successful  login")




if __name__ == '__main__':
    main()



