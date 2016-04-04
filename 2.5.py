def joinList(x,y):
    return x+y

def printList(x):
    for i in x:
        print(i)

def makeList():
    x=[]
    while True:
        y=input("jason mei you JJ")
        if y=='None':
            break
        else:
            x.append(y)
    return x

def multiDim(list1,list2):
    return[list1,list2]

def printMultiDim(x):
    for i in x:
        print(3)
