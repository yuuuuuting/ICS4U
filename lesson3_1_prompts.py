import re

def myInput(prompt):
    return input(prompt + "\n> ")

def tfInput(prompt):
    ''' Prompt the user for a yes/no question and return True/False '''
    # Display the question and return an answer
    response = myInput(prompt)
    if response == '':
        return False
    return response[0].lower() == 'y'

def stringCompare(a,b):
    return bool( re.search(b.strip().lower(),a.strip().lower()) )

def quiz(prompt, answer):
    q = myInput(prompt)
    if stringCompare(q, re.escape(answer)):
        print("Correct!")
        return 1
    else:
        print("The correct answer was '{0}'.".format(answer))
        return 0

def p1():
    print("="*50 + "\nPART 1:\n" + "="*50)
    
    prompt = "Hello! Open 'text.txt' and look at its contents.\n" + \
             "Does it have a newline at the end?"
    info = "f.write() puts the string EXACTLY as we wrote it, without a newline."
    if tfInput(prompt):
        print("Look again! " + info)
    else:
        print("Correct! " + info)
    myInput("Hit enter here, then return to the code!")
    
    print("="*50 + "\nPART 2:\n" + "="*50)

def p2():
    myInput("-"*50)
    
    prompt = "Now let's make test.txt more interesting. Open the file and\n" + \
             "replace everything with the following lines (starting with Hello):\n\n" \
             "Hello!\nThis\nis\na\ntest.\nThere are 6 lines in this file!\n"
    print(prompt)
    prompt2 = "When you're done, save the file, hit enter here, and return to the code!"
    myInput(prompt2)
    
    print("="*50 + "\nPART 3:\n" + "="*50)

def p3():
    myInput("-"*50)

    print("Quiz time!")
    grade = 0
    grade += quiz("What is the name of the text file we're using?","test.txt")
    grade += quiz("How many lines of text are there in test.txt?","6")
    grade += quiz("What line of code did we use to open a file for reading?",
                  "f = open(filename,'r')")
    grade += quiz("How do we read the whole file into a string?", "f.read")
    grade += quiz("How do we read one line into a string?", "f.readline")
    grade += quiz("How do we close the file?", "f.close")
    print("You scored {0} out of 6!".format(grade))

    prompt = "When you're ready to continue, hit enter and return to the code."
    myInput(prompt)

    print("="*50 + "\nPART 4:\n" + "="*50)

def p4():
    myInput("-"*50)

    print("Quiz time!")
    grade = 0
    grade += quiz("What is the first way to read the file into a list?","f.readlines")
    grade += quiz("What is the second way to read the file into a list?","list(f)")
    print("You scored {0} out of 2!".format(grade))

    prompt = "When you're ready to continue, hit enter and return to the code."
    myInput(prompt)

    print("="*50 + "\nPART 5:\n" + "="*50)

def p5():
    myInput("-"*50)

    print("Quiz time!")
    grade = 0
    grade += quiz("How do we find where we are in an open file?","f.tell")
    grade += quiz("How do we move to another location in the file?","f.seek")
    grade += quiz("How many modes does f.seek have?","3")
    grade += quiz("What would we use to read 15 bytes from file f?","f.read(15)")
    print("You scored {0} out of 4!".format(grade))

    prompt = "Congratulations, that's all! Hit enter to end this program."
    myInput(prompt)
