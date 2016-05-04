import random
def swap(array,a,b):
    '''
    Swap two elements in an array.
    There is no return - this function modifies the input array directly.
    '''

    x=array[a]  # Makes a value called x and store the array[a] into it.
    array[a]=array[b]  # Makes a array[a] equals to array[b].
    array[b]=x  # Makes array[b]equals to x.
    return array  # returns the array

def sort(array):
    for i in range(1, len(array)):  # Start looping at index 1 in the array
        v = array[i]  # Get the value
        j = i - 1
        while j >= 0 and array[j] > v:
            array[j + 1] = array[j]
            j = j - 1
        array[j+1] = v
    return array



if __name__=="__main__":
    array = [random.randint(0,100) for i in range(10)]
    print(sort(array))