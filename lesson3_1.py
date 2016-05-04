'''
=========================
Unit 3: File Input/Output
=========================

In this unit, we're going to learn how to read and write text files.
These are the commands we'll be learning:

OPEN/CLOSE A FILE:
f = open(filename, mode)
f.close()

WRITE:
f.write(string)

READ:
f.read()
f.readline()
f.readlines()
list(f)
for line in f:

LOCATION:
f.tell()
f.seek(offset, reference)

Start at the top of the code, read all of the comments, and follow the
instructions!
'''

# -------------------PART 1: OPENING AND WRITING---------------------------- #

# You can ignore this line - it imports code that is used to ask you questions.
import lesson3_1_prompts

# We're going be reading and writing to a file called 'test.txt' in our current
#   directory.
# test.txt doesn't exist yet, so it will be created when we open it!
filename = 'test.txt'

# Opening a file creates a 'file object' that lets us talk to the file.
# We're going to call our file object 'f'.
f = open(filename,'w')

# Let's write 'Hello world!' to test.txt and close it.
f.write('EXACRLY')
f.close()

# The file is now closed - if we tried to write more, we'd get an error.
### RUN this program now, and follow the prompts on the screen! ###
lesson3_1_prompts.p1()


# -------------------PART 2: READING---------------------------------------- #

# Welcome back! We're going to open 'test.txt' again, this time to read it.
# When we open a file, we need to say whether we're reading it (r) or writing
#   to it (w). We can also use 'r+' for read AND write permissions.
f = open(filename,'r')

# Let's read the whole file and store it into a variable 'string1'.
string1 = f.read()

# Every time you're done with a file, close it!
f.close()

# We can see what we've read from the file...
print( string1 )

# Sometimes we want to read the file one line at a time (until the first
#   newline), instead of reading the whole file. We can use f.readline()!
f = open(filename,'r')
string2 = f.readline()
f.close()

# Since our file was only one line (it didn't even have a newline at the end!),
#   string1 and string2 are identical.
print(string2)
print(string1==string2)

### GO BACK to the running code and hit enter, then follow the prompts! ###
lesson3_1_prompts.p2()


# -------------------PART 3: READING MULTIPLE LINES------------------------- #

# We'll open the file for reading, read one line, and leave it open for now
f = open(filename,'r')
string1 = f.readline()

# Let's see what's in string1 - look at the running code to see the output.
print(string1)

# Did you notice, string1 contains a newline at the end? That's why there's a
#   blank line between each line of output.
# Okay. Let's read another line into string2, and another into string3.
string2 = f.readline()
string3 = f.readline()
print(string2)
print(string3)

# We can even print lines directly, without storing them into a string.
print(f.readline())

# Each time we read a line, we 'move forward' in our text file.
# We can even read a line and not store it into anything, to 'skip' a line.
f.readline()

# test.txt has 6 lines of text, we've read 5. Let's store line 6 into string4!
string4 = f.readline()
print(string4)

# What if we try to read another line? No problem, it reads as an empty string.
string5 = f.readline()
print(string5)

# Looks like we're done with our file, so let's close it.
f.close()

### GO BACK to the running code and hit enter, then follow the prompts! ###
lesson3_1_prompts.p3()


# -------------------PART 4: READING FILES AS LISTS------------------------- #

# You've learned most of the basics of file reading and writing!
# One other useful thing is to read a file into a list, with each line as its
#   own element:
f = open(filename,'r')
stringList = f.readlines()
f.close()

# Now we have the whole file as a list of strings! We can use individual
#   elements in whatever way we like.
print(stringList)
print(stringList[0])

# We can do the exact same thing with another command:
f = open(filename,'r')
stringList2 = list(f)
f.close()

# These two lists are identical:
print(stringList2)
print(stringList==stringList2)

### GO BACK to the running code and hit enter, then follow the prompts! ###
lesson3_1_prompts.p4()


# -------------------PART 5: SEEKING IN A FILE------------------------------ #

# There's one more topic to cover: seeking in a file.
# Let's start by opening the file (in binary mode!) and reading one line.
f = open(filename,'rb')
string = f.readline()

# By reading a line, we have 'moved forward' in the file. f.tell() will tell us
#   where in the file we are (what byte we're reading next).
print(f.tell())

# We can seek to a different part of the file using f.seek(). For instance, we
#   can seek to the start of the file (byte 0):
f.seek(0)

# If we read another line, it will be from the start of the file again!
print(f.readline())

# We can seek wherever we like, for instance byte 5:
f.seek(5)
print(f.readline())

# f.seek() has three modes: seeking from the start of the file (mode 0), from
#   your current position in the file (mode 1), or backwards from the end of
#   the file (mode 2). Mode 0 is the default. Here's mode 0 one more time:
f.seek(0,0)
print("Mode 0:\tPosition:", f.tell(), "Next line:", f.readline(), sep="\t")

# Mode 1 - let's seek forward from our current location by 2 bytes (characters):
f.seek(2,1)
print("Mode 1:\tPosition:", f.tell(), "Next line:", f.readline(), sep="\t")

# Mode 2 - let's seek back 10 bytes from the end of the file:
f.seek(-10,2)
print("Mode 2:\tPosition:", f.tell(), "Next line:", f.readline(), sep="\t")

# One last thing to learn. One of the first commands in this lesson was
#   f.read(). Instead of reading the WHOLE file, we can use f.read to only
#   read a certain number of bytes (characters).
# Let's seek to the start of the file, read 10 characters, then close the file.
f.seek(0)
string = f.read(10)
print(string)
f.close()

### GO BACK to the running code and hit enter, then follow the prompts! ###
lesson3_1_prompts.p5()
