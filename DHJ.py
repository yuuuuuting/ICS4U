def odd(x):
    return x%2
print(odd(7))

def div(y):
    return y%3==0 and y%7==0
print(div(21))

def getDigit(x,n):
   return x//(10**n) % 10
print(getDigit(12345,0))

def fourDigit(z):
    a=getDigit(z,3)
    b=getDigit(z,2)
    c=getDigit(z,1)
    d=getDigit(z,0)
    print(a+b+c+d)
    print(d,c,b,a,sep="")
    print(d,a,b,c,sep="")
    print(a,c,b,d,sep="")
fourDigit(5488)