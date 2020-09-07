
import copy
import random

zhanghao='login'
name='玩家一'
paw='login'
jues=None
xueliang=100
fangyv=50
gongji=3
info=[name,jues,xueliang,fangyv,]
localtion={"x":20,"y":20}
zuobian=(0,1,2,3,4,5,6,7,8,11)
ditu=[zuobian for i in range(10)]
boss_exit=0
bossxylist=[0,0]
login_suo=3

def creatBoss():
    global bossxylist
    global boss_exit
    boss_exit=1
    bossxylist[0]=random.randint(0,9)
    bossxylist[1]=random.randint(0,9)


def PRINGWEIZHI(x,y):
    zuobian = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    weizhi=[copy.deepcopy(zuobian) for i in range(10)]
    weizhi[x][y] = '♥'
    weizhi[bossxylist[0]][bossxylist[1]]='boss'
    for i in weizhi:
        print(i)

def PRINTINFO():
    print("=============你的个人信息================")
    print("你的账号：" +zhanghao)
    print("你的密码："+paw)
    print('名字 :' +name)
    print(' 角色:' + str(jues))
    print('血量' + str(xueliang))
    print("防御："+str(fangyv))
    print("当前位置( %s , %s ）" % (localtion.get("x"), localtion.get("y")))

def login():
    creatBoss()
    print("+++++++++++login++++++++++++'")
    global login_suo
    if login_suo==0:
        print("你不能登陆了，您的机会已经用完了")
        return main()
    liststr=redLogin()
    print(liststr)
    print("输入你的账号")
    # PRINTINFO(
    name2=input()
    print("请输入你的密码")
    paw2=input()
    if liststr[0]==name2 and liststr[1]==paw2:
        RunStart()
    else:
        login_suo-=1
        print("输入账号密码错误，你还有 %d 次机会"%(login_suo))
        return login()



def zhuce():
    print("+++++++++++注册账号++++++++++++'")
    print("请输入你想要注册的账号")
    global zhanghao
    zhanghao=input()
    print("你的密码")
    global paw
    paw=input()
    print("请确认你的密码")
    paw2=input()
    if paw!=paw2:
        print("请保证两次密码一致")
        return zhuce()
    writeLogin(zhanghao,paw)
    print("-------------注册成功===============")
    print(redLogin())
    return main()

def redLogin():
    filestr=open("login.txt","r+")
    return filestr.readline().split()



def writeLogin(name,pwd):
    filterstr=open("login.txt","w+")
    filterstr.write(name + " " +pwd)
    filterstr.flush()
    filterstr.close()

def main():
   print("""
  --------- start  login   GAME ....
    1  登录 
    2 注册账号
    3 解除登录限制
   """)
   flag=input()
   if int(flag)==1:
       login()
   elif int(flag)==2:
        zhuce()
   elif int(flag)==3:
       global login_suo
       login_suo=3
       return main()
   else:
       main()


def joinGame():
    print("选择你的下一步   1 起名字  2 直接战斗")
    flag=input()
    if flag=='1':
        print("请输入你的名字：  ====")
        global name
        name=input()
        PRINTINFO()
        joinGame()

    elif flag=='2':
        zhandaou()
    else:
        joinGame()


def zhandaou():
    if (localtion['x']%11 )==bossxylist[0] and (localtion['y']%11 )==bossxylist[1]:
        creatBoss()
    print("============start war=============")
    print("""
        a  向左移动  w  向上移动   s  向下移动   d  向右移动  1 个人信息展示 2 战斗
    """)
    PRINGWEIZHI(localtion['x']%11,localtion['y']%11)
    flag=input()
    if flag=='w':
        localtion['x']=localtion['x']-1
        zhandaou()
    elif flag=='d' :
        localtion['y']=localtion['y']+1
        zhandaou()
    elif flag=='a' :
        localtion['y']=localtion['y']-1
        zhandaou()
    elif flag=='s' :
        localtion['x']=localtion['x']+1
        zhandaou()
    elif flag=='1':
        PRINTINFO()
        zhandaou()
    else: zhandaou()

def RunStart():
    print("=============successful  login===================")
    joinGame()

if __name__ == '__main__':
    main()



