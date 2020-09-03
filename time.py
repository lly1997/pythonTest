import time

print(time.time())
print(time.monotonic())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d",time.localtime()))

yuanzhu=time.strptime("Sep 2 2020","%b %d %Y")
it=iter(yuanzhu)
for i in it:
    print(i)
print(time.strptime("Sep 2 2020","%b %d %Y")[0:5])
tuple=(5,6,9)
dictste={1,2,3,4}

print(sum(tuple))
print(sum(dictste))
print(dictste)
print(tuple)

liststrarray=["hello","word"]
print(liststrarray.copy())
liststrarray.append("2020")
newliset= liststrarray.copy()
print(newliset)
liststrarray.insert(2,"lianliyong")
print(newliset)
print(liststrarray)
liststrarray.pop(0)
print(liststrarray)
liststrarray.pop(2)
print(liststrarray)
liststrarray.extend(newliset)
print(liststrarray)
liststrarray.count("2020")
print(liststrarray.index("2020"))
print(liststrarray.count("2020"))
print("=======================")
liststrarray.sort()
print(liststrarray)
liststrarray.sort(reverse=True)
print(liststrarray)



testlist = list()

print(testlist)



