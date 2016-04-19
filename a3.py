'''
Program:    a3.py
Name:       John Zhang
Date:       2016 4 17
Desc:       be able to makes change for files in pycharm
'''

# An array created for array2TSV
array = [['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+'],['ICS4U', 'Assignment 1', 'Han Solo', '4-']]

# 1
def writeString(filename,string):
    '''
   This is a function that is able to opens a file and write string in to that file
    '''
    # Open/create a file
    f = open(filename,'w')
    # Writes the given string to the file
    f.write(string)
    # Closes the file
    f.close()

# 2
def readString(filename):
    '''
    This is a function that allows user to read through the entire file they have opened
    '''
    # Opens a file
    f = open(filename,'r')
    # Reads the entire file to a string
    string= f.read()
    # Closes the file
    f.close()
    # Returns the string
    return string

# 3
def writeNum(filename,number):
    '''
    A function that is be able to write number in to the opened file
    '''
    # Opens a file
    f = open(filename,'w')
    # Wirtes the givennumber to the file
    f.write(str(number))
    # Closes the file
    f.close()

# 4
def readNum(filename):
    '''
    A function that is be able to returns the number contained in the file
    '''
    # Opens a file
    f = open(filename,'r')
    # Reads the entire file to a string
    string= f.read()
    # Closes the file
    f.close()
    # Try the number that has given to the file are integer or float
    try:
        # If the number is integer then returns the number as integer type
        return int(string)
    # If the number isn't integer then
    except ValueError:
        # Returns the number as float type
        return float(string)

# 5
'''
A function turns a 2-dimensional array into a TSV string
'''
def row2TSV(row):
    '''
    A function that is able to separated each values in lines by using Tab
    '''
    # Create an empty string array called "string"
    string=''
    # Loop through the origin array
    for i in range(len(row)):
        # separated each values in lines by using "\t"
        string=string+row[i]+'\t'
    # Returns the string without adding the last "\t"
    return string[:-1]

def array2TSV(array):
    '''
    A function that is able to separated each lines in a whole list by using Tab
    '''
    # Create an empty string array called "string"
    string=''
    # Loop through the origin array
    for u in range(len(array)):
        # separated each lines in the list by using "\n"
        string=string+row2TSV(array[u])+'\n'
    # Returns the string
    return string

# 6
def TSV2array(string):
    '''
    A function turns a TSV string a into 2-dimensional array
    '''
    # Created a empty list
    List=[]
    # Separate the the line by "\n", and also delete the "\n"
    array=string[:-1].split('\n')
    # Loop through the origin array
    for i in range(len(array)):
        # Separate the the line when "i" has meet "\t", and also delete the "\t"
        List=List+[array[i].split('\t')]
    # Returns the List
    return List

# 7
def writeTSV(filename,array):
    '''
    A function that is able to write 2-dimensional array to a file as a TSV string
    '''
    # Open a file
    f = open(filename,'w')
    # Turns the 2-dimensional array to a TSV string
    f.write(array2TSV(array))
    # Close the file
    f.close

# 8
def readTSV(filename):
    '''
    A function that is able to read the entire TSV file and turns it into a 2-dimensional array
    '''
    # Open a file
    f = open(filename,'r')
    # Turns the file in the the array type
    array=TSV2array(f.read())
    # Close the file
    f.close
    # Returns the array
    return array

# codes for the function testing purpose
# 1
print(writeString('saber.txt','lancer'))
#2
print(readString('saber.txt'))
#3
print(writeNum('saber.txt',9027.0))
#4
print(readNum('saber.txt'))
#5
print(array2TSV(array))
#6
print(TSV2array('ICS4U\t Assignment 1\t Luke Skywalker\t 3+\nICS4U\t Assignment 1\t Han Solo\t 4-\n'))
#7
print(writeTSV('saber',array))
#8
print(readTSV('saber'))
