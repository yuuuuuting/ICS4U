'''
Program:    a4.py
Name:       John Zhang
Date:       2016/04/29
Desc:       This is an sorting algorithm call Insertion Sort
'''

# Import required libraries.
import copy, random, timeit

def funcTimer(func):
    '''
    Time the specified function, running it 100 times with a random array.
    '''
    
    # Create the strings to be run.
    arrayStr = 'array = [random.randint(0,1000) for i in range(200)]'
    funcStr = '{}; a4.{}(array)'.format(arrayStr, func.__name__)

    # Run the test and return the result.
    return timeit.timeit(funcStr, setup='import random, a4', number=100)

def swap(array,a,b):
    '''
    Swap two elements in an array.
    There is no return - this function modifies the input array directly.
    '''

    x=array[a]  # Makes a value called x and store the array[a] into it.
    array[a]=array[b]  # Makes a array[a] equals to array[b].
    array[b]=x  # Makes array[b]equals to x.
    return array  # returns the array

def findMin(array):
    '''
    Return the index of the minimum value in the array.
    '''

    for i in range(len(array)):  # loop through the index of the array.
        if min(array)==array[i]:  # search the minimum value in array.
            return i  # Returns the searching result.


def sort(array):
    '''
    Sort an array from lowest to highest using Insertion Sort.
    '''

    # Make a copy of array, so that the input array isn't modified.
    array = copy.deepcopy(array)

    ### PROGRAM THE REST OF YOUR SORTING FUNCTION HERE ###
    for i in range(1, len(array)):  # Start looping at index 1 in the array.
    # Create a value 'v' and it is storing the item in the list at each of those indexes except the leftest one.
        v = array[i]
        j = i - 1
        while j >= 0 and array[j] > v:  # Check if the 'j' are under the right conditional.
            swap(array,j+1,j)  # Swap the two values and keep swapping to the left until it is at the right position.
            j = j - 1
        array[j+1] = v
    return array




    # Return the sorted array.


if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    # Create an array of random numbers.
    array = [random.randint(0,100) for i in range(10)]

    # Print the array, the sorted array, and the elapsed time for 100 tests.
    print(array)
    print(sort(array))
    print(funcTimer(sort))
