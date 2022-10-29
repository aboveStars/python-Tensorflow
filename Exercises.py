
# Example 1
print("Twinkle, twinkle, little star, \n    How I Wonder what you are! \n       Up Above the world so high \n       Like a diamondin the sky. \nTwinkle, twinkle, little star, \n       How I Wonder what you are")

# Example 2
print(sys.version)

# Example 3
import datetime

datetime.datetime.now()
# Example 4
import math

x = float(input("Radius: "))
print(f"Area of circle: {x**2 * math.pi}")


# Example 5
fN = input("İlk İsim: ")
lN = input("Son İsim: ")

print(f"{lN} {fN}")


# Example 6
x = input("Giriniz: ")

y = []

xE = x.split(",")

y = xE
z = tuple(y)

print(y)
print(z)

# Example 7
fullName = input("Say my name: ")
extensionName= fullName.split(".")[-1]
print(extensionName)


# Example 8
color_list = ["Red","Green","White" ,"Black"]
print(f"First: {color_list[0]} \nSecond: {color_list[-1]}")


# Example 9
deadLine = (16,5,2003)
print("%i/%i/%i"%deadLine)


# Example 10
# x = input("Say A Number: ")

firstNumber = int(x)
secondNumber = int(x + x)
thirdNumber = int(x+x+x)

print(firstNumber+secondNumber+thirdNumber)

# Example 11
print(abs.__doc__)

# Example 12
import calendar
y = int(input("Year: "))
m = int(input("Month: "))

print(calendar.month(y,m))

# Example 13
print("""
Uzun ince bir yoldayım
    Gidiyorum gündüz gece
Bilmiyorum ne haldeyim
    Gidiyorum gündüz gece
""")
# Example 14
import datetime as dt
firstDate = dt.date(2003,5,16)
secondDate = dt.date(2022,10,23)

print(f"My Living Days: {secondDate-firstDate} ")


# Example 15
import math as mt
print(mt.pi * 6**3)


# Example 16
def weirdFunction(n):
    if n<=17:
        return 17-n
    else:
        return (n-17)*2

print(weirdFunction(10))
print(weirdFunction(30))


# Example 17
def otherFunc(n):
    if n in list(range(100,1001)):
        return True

print(otherFunc(500))

# Example 18
def three_sisters(a,b,c):
    sum = a + b + c

    if(a==b==c):
        return sum * 3
    else:
        return sum

three_sisters(10,20,30)


# Example 19
def stringFunc(s):
    if len(s) <= 2:
        return "Not Interested"
    
    else:
        firstTwo = s[:2]
        if firstTwo == "Is":
            return s
        else:
            return f"Is{s}"


print(stringFunc("Isildur"))
print(stringFunc("yunus"))
print(stringFunc("Is"))


# Example 20
def stringCopier(s,n):
    return s*n

#stringCopier("Yunus",5)

def largeString(s,n):

    if n <= 0:
        return False
    

    x = ""

    for i in range(n):
        x = x + s
    
    return x


print(largeString("Yunus",5))
print(largeString("yunus",-1))

# Example 21
x = int(input("Please give a number: "))


if x%2 == 0:
    print("This Number is even") 
else:
    print("This Number is odd") 


# Example 22
def four_finder(i):
    tempList = list(i)
    return tempList.count(4)

print(four_finder([12,13,14,4,4]))

def foru_finder_new(i):

    count = 0
    
    for v in i:
        if v==4:
            count = count + 1

    return count 

print(foru_finder_new([4,0,4,3,4,2]))


# Example 23
def weirdStringFuntion(s,n):
    if len(s) < 2:
        emptyString = ""
        for i in range(n):
            emptyString = emptyString + s
        return emptyString

    else:
        neededPart = s[:2]
        emptyString = ""
        for i in range(n):
            emptyString = emptyString + s
        
        return emptyString

print(weirdStringFuntion("yunus",10))
print(weirdStringFuntion("a",4))

# Example 24

def vowelOrNot(l):
    vowelS = ["A","E","I","O","U"]
    vowelSC = list()

    for e in vowelS:
        vowelSC.append(e.lower())

    if l in vowelS or l in vowelSC:
        return "It is NOWEL"
    else:
        return "It is NOT NOWEL"

print(vowelOrNot("a"))
print(vowelOrNot("I"))
print(vowelOrNot("x"))

# Example 25
def magicFunc(e,l):
    if e in l:
        return True
    else:
        return False

print(magicFunc(5,[5,10,15]))
print(magicFunc(1,[2,3,4,5,6]))

# Example 26
def histogram_creator(ob,hT):
    for n in hT:
        print(ob*n)

histogram_creator("@",[1,2,3,4,5,4,3,2,1])

# Example 27
def concatenateFunc(l):
    sum = ""
    for e in l:
        sum = sum + str(e)
    return sum

print(concatenateFunc([1,2,1,"yunus","elon",14,13,-1,]))

# Example 28
def listEvener(l):
    for e in l:
        if e != 237:
            if e %2 == 0:
                print(e)
        else:
            print(237)
            break
        

listEvener([386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527])


# Example 29
color_list_1 = set(["White","Black","Red"])
color_list_2 = set(["Red","Green"])

finalList = []

for c in color_list_1:
    if c not in color_list_2:
        finalList.append(c)
print(finalList)


print(color_list_1.difference(color_list_2))
print(color_list_2.difference(color_list_1))


# Example 30
def calculateAreOfTriangle(b,h):
    return b*h/2

print(calculateAreOfTriangle(10,6))

# Example 31
def gcdCalculater(n1,n2):
    gcd = 0

    for i in range(min(n1,n2) + 1):
        if i != 0:
            if n1%i == 0 and n2%i == 0:
                gcd = i

    return gcd

print(gcdCalculater(1,5))

# Example 32
def lcmCalculater(n1,n2):
    
    bigNumber = max(n1,n2)
    lcm = bigNumber

    while lcm%n1 != 0 or lcm%n2 !=0:
        lcm += 1
    return lcm

print(lcmCalculater(13,91))

#  Example 33
def weirdSumFunciton(a,b,c):
    if a == b or a == c or b == c:
        return 0
    else:
        return a + b + c
print(weirdSumFunciton(3,3,2))

# Example 34

def strangeSumFunc(a,b):
    sum = a + b

    if sum in range(15,21):
        return 20

    else:
        return sum

print (strangeSumFunc(3,4))
print(strangeSumFunc(8,9))


# Example 35

def fiveOrEqualFunc(a,b):
    if a == b or abs(a-b) == 5:
        return True
    else :
        return False

print(fiveOrEqualFunc(10,5))
print(fiveOrEqualFunc(10,10))
print(fiveOrEqualFunc(10,32))


# Example 36

def sumFunc(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        return "give integer values only"
print(sumFunc(3,4))
print(sumFunc(5,5.1))
print(sumFunc(2.1,2.1))
print(sumFunc("c","y"))


# Example 37
def personal_details():
    name, age, adress = "Yunus",19,"Istanbul/Ümraniye"
    return "Name: {} \nAge: {} \nAdress: {}".format(name,age,adress)

print(personal_details())

# Example 38

def strangeFunc(a,b):
    sum = a + b
    return sum **2

print(strangeFunc(10,5))


# Example 39

def interestRateCalculater(p,r,n,t):
    return round(((1+r/n)*p)**t)

interestRateCalculater(1,2,3,4)


#Example 40

from math import sqrt


def twoPointDistance(p1,p2):
    xDistance = abs(p1[0]-p2[0])
    yDistance = abs(p1[1]-p2[1])

    return sqrt(xDistance**2 + yDistance**2)

print(twoPointDistance((5,0),(5,8)))


#Example 41

import os

print(os.path.exists("/Users/yunusmerve/Documents/MerveninFelsefeÖdevi.docx"))


#Example 42


import platform

print(platform.architecture()[0])


#Example 43

import os
import platform

print(f"""
Name of the Operating System: {os.name}
Name of the OS System: {platform.system()}
Version of the Operating System: {platform.release()}
""")


#Example 44

import site
print(site.getsitepackages())


#Example 45

import os
print(os.system('ls'))


#Example 46

import os
print(f"Current File Name: {os.path.realpath(__file__)}")


#Example 47

import multiprocessing

print(multiprocessing.cpu_count())


#Example 48

x = "1453.12"

y = float(x)
z = int(y)

print(f"""
{x}
{y}
{z}
""")


# Example 49

import os

path = "/Users/yunusmerve/Desktop/GitGenel"
dir_list = os.listdir(path)

print(dir_list)


#Example 50

for i in range(5):
    print("*", end="")

print("\nyunus",end=" korkmaz")
print("c")


#Example 51

import cProfile
def sumFunc():
    for e in range(5):
        print("x",end="")
cProfile.run('sumFunc()')


# Example 52

import sys
print("Very big error", file=sys.stderr)


#Example 53

import os
print(os.environ)


#Example 54

import getpass
print(getpass.getuser())


#Example 55

import socket
hostname = socket.gethostname()
IPadress = socket.gethostbyname(hostname)

print(f"Our IP Adress: {IPadress}")


# RNA Question

a = "yunus"
listOfa = list(a)
listOfa[4] =  "ş"

aN = ''.join(listOfa)
aN

def rnaConverter(DNA):
    tempList = list(DNA)
    editingList = tempList
    index = -1
    for l in tempList:
        index += 1
        if l == "G":
            editingList[index] = "C"
        elif l == "C":
            editingList[index] = "G"
        elif l == "T":
            editingList[index] = "A"
        elif l == "A":
            editingList[index] = "U"
    return ''.join(editingList)

print(rnaConverter("AGGT TAAA AGCT TGCA ADGC ADGC TAAA GCAA TAAA GCAA AGGG"))