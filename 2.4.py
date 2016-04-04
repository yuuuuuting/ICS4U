def printChars(string):
    print ('\n'.join(string))
printChars('lll')

def emailDomain(string):
    a=string.find('@')
    return string[a+1:]
print (emailDomain('abc@domain.com'))

def printSorted(string1,string2):
    if string1>string2:
        print(string1)
        print(string2)
    else:
        print(string2)
        print(string1)
printSorted('PLUS','tap')

def compareLenfth(string1,string2):
    return len(string1)==len(string2)
