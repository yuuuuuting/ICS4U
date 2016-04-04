import random

#questions
#1
def helloWorld():
    print ("Hello world!")
#2
def greet(x):
    print("Hello",x,"!")
#3
def greet2():
    x=input("what is your name?")
    print ("Hello",x,"!")
#4
def plus1(num):
    return num+1
#5
def max3(a,b,c):
   return max(a,b,c)
#6
"""def printN(n):
   while n>x:
       x=x+1
       print(x)"""
#7
def sumN(n):
    return sum(range(1,n))
#8
def strFirst(str):
    return str[0]
#9
def strHalf(str):
    return str[:len(str)//2]
#10
def guessingGame():
    guesses=0
    number = random.randint(1, 7)
    a=input("pls guess a number between 1 to 7. ")
    while True:
        guesses=guesses+1
        a=input("pls guess a number between 1 to 7. ")
        if int(a) <number:
            print("too low")

        if int(a) >number:
            print("too high")

        if int(a) == number:
            print ("you are right!")
            break
    return guesses



#text cases
#1
helloWorld()
#2
greet("bob")
#3
greet2()
#4
print(plus1(0))
#5
print(max3(3,6,7))
#6
#printN(3)
#7
print(sumN(4))
#8
print (strFirst("John"))
#9
print (strHalf("Luffy"))
#10
guessingGame()


