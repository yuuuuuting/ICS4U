'''
Program:    a5.py
Name:       
Date:       
Desc:       
'''

import os

### PROGRAM YOUR FUNCTIONS HERE! ###
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

def morePower(x,n):
    if n==0:
        return 1
    if n%2==0:
        return power(x,n//2)*power(x,n//2)
    return x*power(x,n//2)*power(x,n//2)

def GCF(a,b):
    if b==0:
        return a
    return GCF(b,a%b)

def isPalindrome(string):
    if string=='':
        return None
    elif string[0]==string[-1]:
        return isPalindrome(string[1:-2])
    elif len(string)==0 or 1:
        return True
    return False


#def printFiles(root):

if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    pass

print(power(2,7))
print(morePower(5,4))
print(GCF(12,8))
print(isPalindrome('civic'))