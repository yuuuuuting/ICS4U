def linearSearch(array, value):
    for i in range(len(array)):
        if array[i]==value:
            return 1
    return None

def binarySearch(array,value):
    L=0
    R=len(array)-1
    while L <=R:
        m=(L+R)//2
        if array[m]==value:
            return m
        if array[m]<=value:
            L=m-1
        if array[m]>=value:
            R=m-1
    return None



array=[1,5,7,22,35,58,109]
print(linearSearch(array,7))
print(binarySearch(array,35))