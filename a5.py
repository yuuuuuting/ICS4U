'''
Program:    a5.py
Name:       John Zhang
Date:       6/9/2016
Desc:       assignment five
'''

import os

### PROGRAM YOUR FUNCTIONS HERE! ###
def power(x,n):
    '''
    This function computes the power of x^n
    '''
    if n==0:
        #Return if that n=0
        return 1
    # Return function
    return x*power(x,n-1)

def morePower(x,n):
    '''
    This function computes the power of x^n, using the following rules
    '''
    if n==0:
        #Return if that n=0
        return 1
    #Return if n is even
    if n%2==0:
        return power(x,n//2)*power(x,n//2)
    #Return if n is odd
    return x*power(x,n//2)*power(x,n//2)

def GCF(a,b):
    '''
    This function finds the greatest common factor of and two numbers. The greatest common factor is the largest number
    that divides evenly into both numbers
    '''
    if b==0:
        #Return if that n=0
        return a
    #Return the function
    return GCF(b,a%b)

def isPalindrome(string):
    '''
    This function checks whether a string is palindrome -  a word that is the same forwards and backwards
    '''
    if string=='':
        # Return if there is nothing in the string
        return None
    elif string[0]!=string[-1]:
        # Return is the string are not same forwards and backwards
        return False
    elif len(string)<2:
        # Return if the letters string are less than 2
        return True
    # Return the function
    return isPalindrome(string[1:-1])

#def printFiles(root):

if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    pass

print(power(2,7))
print(morePower(5,4))
print(GCF(12,8))
print(isPalindrome('civsdic'))