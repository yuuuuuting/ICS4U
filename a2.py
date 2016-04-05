'''
Program:     a2.py
Name:        John Zhang
Date:        april 4th. 2016
Desc:        a program that is be able to calculate the assignment/test average grades for the students and courses
'''

# Initialize the database of student grades
database = [
    ['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+'],
    ['ICS4U', 'Assignment 1', 'Han Solo', '4-'],
    ['SPH3U', 'Unit 1 Test', 'Leia Organa', '4'],
    ['SPH3U', 'Unit 1 Test', 'Luke Skywalker', '3-'],
    ['SPH4U', 'Unit 1 Test', 'Yoda', '4+'],
    ['SPH4U', 'Unit 1 Test', 'Anakin Skywalker', '3'],
    ['MHF4U', 'Unit 1 Test', 'Boba Fett', '2+'],
    ['MHF4U', 'Unit 1 Test', 'Kylo Ren', '3'],
    ['MHF4U', 'Unit 1 Test', 'Chewbacca', '4']
    ]

def tfInput(string):
    ''' Prompt the user for a yes/no question and return True/False '''
    # Display the question and return an answer
    answer = input(string)
    return answer[0].lower() == 'y'

# ICS4U:

#1
def level2Percent(level):
        '''
        1.Transform string level to numerical percentage.
        '''
        # codes for changing different level to percent
        if level=='4+':
            return 100
        elif level=='4':
            return 94
        elif level=='4-':
            return 86
        elif level=='3+':
            return 79
        elif level=='3':
            return 76
        elif level=='3-':
            return 72
        elif level=='2+':
            return 69
        elif level=='2':
            return 66
        elif level=='2-':
            return 62
        elif level=='1+':
            return 59
        elif level=='1':
            return 56
        elif level=='1-':
            return 52
        elif level=='< 1':
            return 40

#2
def percent2Level(percent):
        '''
        2.Transform numerical percentage to string level.
        '''
        # codes for changing different percentage to levels
        if percent in range (95,101):
            return "4+"
        elif percent in range (87,95):
            return "4"
        elif percent in range (80,87):
            return "4-"
        elif percent in range (77,80):
            return "3+"
        elif percent in range (73,77):
            return "3"
        elif percent in range (70,73):
            return "3-"
        elif percent in range (67,70):
            return "2+"
        elif percent in range (63,67):
            return "2"
        elif percent in range (60,63):
            return "2-"
        elif percent in range (57,60):
            return  "1+"
        elif percent in range (53,57):
            return "1"
        elif percent in range (50,53):
            return "1-"
        elif percent in range (0,50):
            return "<1"

#3
def stringCompare(string1,string2):
    '''
    3.Be able to check if two strings are the same.
    '''
    # returns the equation of string compare, it used for making two different type but same letters'string same
    return string1.lower().strip()== string2.lower().strip()

#4
def addGrade(database,course,assignment,student,grade):
    '''
    4.Be able to add new grades to database.
    '''
    # returns the formula of adding database
    return database+[[course,assignment,student,grade]]

#5
def inputGrades(database):
        '''
        5. Allows the user to input more grades into database
        '''
        # Asking user question and save their input into database
        course=input('please enter the course name:')
        assignment=input('please enter the name of the assignment/test/exam:')
        student=input('please enter the student name:')
        grade=input('please enter the grade that student have:')
        database=database+[[course,assignment,student,grade]]

        # looping and Asking if user wants to input another grade
        while True:
            decision=tfInput('would you like to input another grade?')
            # ask user question if they decide to input one more grade
            if decision==True:
                student=input('please enter the student name:')
                grade=input('please enter the grade that student have:')
                database=database+[[course,assignment,student,grade]]
            # break the loop if user decide to not inputs anymore grades into database
            elif decision==False:
                break
    # return the database
        return database

#6
def studentAverage(database,student):
    '''
    6. Be able to returns the average percent grade for the specified student.
    '''
    # An array that can store grades in string type.
    gLevel=[]
    # An array that can store grades in percentage type.
    gPercent=[]
    # The total of grades.
    sum=0

    # Functions that is able to find the right student and store grades in to the array I have created name gLevel.
    for e in range(len(database)):
        if stringCompare(database[e][2],student)== True:
            gLevel.append(database[e][3])
    # Functions that allows you to change level to percent and store percentages in to the array name gPercent.
    for r in range(len(gLevel)):
        gPercent.append(level2Percent(gLevel[r]))
    # Functions that can add grades together and became the Sum.
    for f in range(len(gPercent)):
        sum=(sum+gPercent[f])
    # Return the formula of calculating the average
    return sum/len(gPercent)

#7
def courseAverage(database,course):
    '''
    7. Be able to returns the average percent grade for the specified course.
    '''
    # An array that can store grades in string type.
    gLevel=[]
    # An array that can store grades in percentage type.
    gPercent=[]
    # The total of grades.
    sum=0

    # Functions that is able to find the right course and store grades in to the array I have created name gLevel.
    for e in range(len(database)):
        if stringCompare(database[e][0],course)== True:
            gLevel.append(database[e][3])

    # Functions that allows you to change level to percent and store percentages in to the array name gPercent.
    for r in range(len(gLevel)):
        gPercent.append(level2Percent(gLevel[r]))

    # Functions that can add grades together and became the Sum.
    for f in range(len(gPercent)):
        sum=(sum+gPercent[f])

    # Return the formula of calculating the average
    return sum/len(gPercent)



# codes that are able to let program testing/running
if __name__=="__main__":
    pass
    # ICS4U:
    #1
    print(level2Percent('4+'))
    #2
    print(percent2Level(87))
    #3
    print(stringCompare('joHn','JoHN'))
    #4
    print(addGrade(database,'ABC4D','unit 1 test','lancer','4'))
    #5
    print(inputGrades(database))
    #6
    print(studentAverage(database,'Luke Skywalker'))
    #7
    print(courseAverage(database,'ICS4U'))