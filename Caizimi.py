import random as ran

number = ran.randint(0,100)

print(number)

def shuru():
    print("please you number")
    number=input()
    return int(number)


def  caishuzi(xitong,wode):
    if xitong==wode:
        print("yes")
    elif xitong>wode:
        print(">")
        return caishuzi(xitong,shuru())
    else:
        print("<")
        return caishuzi(xitong,shuru())


if __name__ == '__main__':
    caishuzi(number,shuru())
