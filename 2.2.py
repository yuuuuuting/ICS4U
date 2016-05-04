def real():
    a=input("give me a  with any kind of number type")
    return float(a)

print(real())

def price():
    print("$",round(x,2))

print(price(5.119277386),sep="")

def encode(x):
    y=""
    for i in range (len(x)):
        y=y+chr(ord(x(i))+1)
    return y

print(encode("da huang ji"))

def encode(x):
    y=""
    for i in range (len(x)):
        y=y+chr(ord(x(i))-1)
    return y

print(encode("da huang ji"))


