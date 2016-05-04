def isOdd(list):
    if list==[]:
        return False
    elif (list[0]%2)==1:
        return True
    else:
        return isOdd(list[1:])

def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

print(isOdd([6,52,4,6,23,90,6,5,73]))

# Step 1: know when to stop.
# Step 2: Decides how to take one (small) step.
# Step 3: Break the journey down into that step plus a smaller journey.

def loafLength(loaf):
    if loaf ==[]:
        return 0
    loaf.pop()
    return 1+loafLength(loaf)

print(loafLength([1,1,1,1,1,1,1]))

def laugh(n):
    if n==0:
        return ''
    return "HA "+ laugh(n-1)

print(laugh(7))

def sum(n):
    if len(n)==0:
        return 0
    return n[0]+sum(n[1:])

print(sum([1,2,3,4,5,6,7]))

def allEqual(x):
    if len(x)==1:
        return True
    return x[0] == x[1] and allEqual(x[1:])


def countDown(n):
    if n==0:
        return 1
    print (n)
    countDown(n-1)

countDown(5)

def countUp(n):
    if n>0:
        countUp(n-1)
        print(n)

countUp(5)


import os
root = r'C:\Users\RUNE\pycharmProjects\ICS4U'
files = os.listdir(root)

print(files)
print(files[0])

filePath = os.path.join(root,files[0])
print(filePath)