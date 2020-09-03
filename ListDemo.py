print(" 输入字母，当字符为q 时 保存所有的字符")
liststr = list()

while (True):
    char = input()
    if char=='q':
        break
    liststr.append(char)
print(liststr)

print("  [5,4,3,2,1] -> [1,2,3,4,5]->[5,4,3,2,1]")
liststr=[5,4,3,2,1]
liststr.sort()
print(liststr)
liststr.sort(reverse=True)
print(liststr)

print("篮球计分系统")
qiudui1=["火箭队",0]
qiudui2=['湖人队',0]
print("请输入球队名称 以及分数 具体格式为 ‘球队名-分数’,输入 ’game over‘ 结束")
while True:
    print("目前的两只队伍为 火箭队  和 湖人队")
    inputstr=input()
    if inputstr=='game over':
        break
    inputstrs=inputstr.split("-")
    if len(inputstrs) !=2:
        print("请输入正确的格式")
        continue

    try:
        int(inputstrs[1])
    except ValueError:
        print("请输入正确的分数，分数为数字")
        continue

    if inputstrs[0]==qiudui1[0]:
        qiudui1[1]+=int(inputstrs[1])
    elif inputstrs[0]==qiudui2[0]:
        qiudui2[1]+=int(inputstrs[1])
    else:
        print("请输入正确的队伍名字")
        continue

    print('继续输入比分')


if qiudui1[1]>qiudui2[1]:
    print("winer is "+ qiudui1[0])
else:
    print("winner is "+ qiudui2[0])
