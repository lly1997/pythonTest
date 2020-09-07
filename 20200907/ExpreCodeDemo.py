# l1=[i for i in range(20) if i%3==0 and i!=0]
# print(l1)
# print(sum((i for i in range(2000000000) if i%3==0 and i!=0)))

print("9++++++++++++++++++++++++++++++++++++++++++")
fileobj=open("../../lianxi.txt","r+")

strcode='add add aaaioio'
# fileobj.write(strcode)

# fileobj.flush()

strcode=fileobj.read()

strdict={}
strlist=strcode.split()

for i in strlist:
    if strdict.get(i) is None:
        strdict[i]=1
    else:
        strdict[i]+=1

for key in strdict:
    print(key,strdict[key])

print(strdict)