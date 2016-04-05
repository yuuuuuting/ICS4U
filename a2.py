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

#1 transform string level to numerical percentage
def level2Percent(level):
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

#2 transform numerical percentage to string level
def percent2Level(percent):
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

#3 to check if two are the same
def stringCompare(string1,string2):
    return string1.lower().strip()== string2.lower().strip()

#4 be able to add new grades to database
def addGrade(database,course,assignment,student,grade):
    return database+[[course,assignment,student,grade]]

#5 allows the user to input more grades into database
def inputGrades(database):
        course=input('please enter the course name:')
        assignment=input('please enter the name of the assignment/test/exam:')
        student=input('please enter the student name:')
        grade=input('please enter the grade that student have:')
        database=database+[[course,assignment,student,grade]]

        while True:
            decision=tfInput('would you like to input another grade?')
            if decision==True:
                student=input('please enter the student name:')
                grade=input('please enter the grade that student have:')
                database=database+[[course,assignment,student,grade]]

            elif decision==False:
                break

        return database

#6 be able to returns the average percent grade for the specified student.
def studentAverage(database,student):
    gLevel=[]
    gPercent=[]
    sum=0

    for e in range(len(database)):
        if stringCompare(database[e][2],student)== True:
            gLevel.append(database[e][3])

    for r in range(len(gLevel)):
        gPercent.append(level2Percent(gLevel[r]))

    for f in range(len(gPercent)):
        sum=(sum+gPercent[f])

    return sum/len(gPercent)

#7 be able to returns the average percent grade for specified course
def courseAverage(database,course):
    gLevel=[]
    gPercent=[]
    sum=0

    for e in range(len(database)):
        if stringCompare(database[e][0],course)== True:
            gLevel.append(database[e][3])

    for r in range(len(gLevel)):
        gPercent.append(level2Percent(gLevel[r]))

    for f in range(len(gPercent)):
        sum=(sum+gPercent[f])

    return sum/len(gPercent)

if __name__=="__main__":
    pass
    # ICS4U:
    # codes that are able to let program testing/running
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