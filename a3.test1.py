# Import the assignment
import a3

# Import required libraries
import io, sys, re, copy
from contextlib import redirect_stdout

class SetStdin():
    ''' Class to manipulate the stdin stream. '''
    def __init__(self, stdin):
        self.stdin = stdin
        self.oldstdin = sys.stdin
    def __enter__(self):
        sys.stdin = io.StringIO(self.stdin)
    def __exit__(self, type, value, traceback):
        sys.stdin = self.oldstdin

def runWith(fcn, args, stdin):
    ''' Run a function with given arguments and stdin,
    and return the output and stdout. '''

    # Copy arguments in case the function modifies its inputs
    args2 = copy.deepcopy(args)
    
    # Set the stdin
    with SetStdin(stdin):
        # Redirect the stdout
        f = io.StringIO()
        with redirect_stdout(f):
            # Try the function with the arguments, catch any exceptions
            try:
                # *args expands the 'args' list into separate arguments
                output = fcn(*args2)
            except Exception:
                output = None

    # Provide a warning if the function modifies its inputs
    if args != args2:
        print('\tWARNING: THIS FUNCTION MODIFIES ITS INPUTS.')

    # Extract a string for the stdout
    stdout = f.getvalue()
    return output, stdout


def compare(a,b):
    ''' Compare two values (string or numeric). '''
    if isinstance(b, str):
        # Strings: compare using regular expressions
        if a == None:
            a = ''
        #return bool( re.search(b,a) )
        return a == b
    else:
        # Non-strings: compare using ==
        return a == b and type(a) == type(b)

def readFile(filename):
    f = open(filename)
    string = f.read()
    f.close()
    return string

def compareFile(a,b):
    return readFile(a) == readFile(b)

def gradeFcn(fcnStr, args, expectOut, expectStdout, stdin, outFile):
    ''' Main grading function. '''

    # Start the grade at 0 and display some feedback
    grade = 0
    print(fcnStr, ':', sep='')
    print('-'*50)

    # Try to find the specified function
    try:
        fcn = eval(fcnStr)
    except Exception:
        print('\tDoes not exist')
        return grade

    # Loop through each set of arguments (separate tests)
    for i in range(len(args)):
        # Run the function with the right inputs
        thisGrade = 0
        output, stdout = runWith(fcn, args[i], stdin[i])

        # Display the results of the test
        print('\tTest ', i+1, ':\n\t\tInput:\t\t', args[i], sep='')
        if stdin[i] != None:
            print('\t\tUser Input:\t', repr(stdin[i]), sep='')
        if expectOut[i] != None:
            thisGrade += compare(output, expectOut[i])
            print('\t\tOutput:\t\t', repr(output), '\n\t\tExpected:\t', repr(expectOut[i]), sep='')
        if expectStdout[i] != None:
            thisGrade += compare(stdout, expectStdout[i])
            print('\t\tUser Output:\t', repr(stdout), '\n\t\tExpected:\t', repr(expectStdout[i]), sep='')
        if outFile[i] != None:
            thisGrade += compareFile(*outFile[i])
            print('\t\tOutput file:\t', outFile[i][0], '\n\t\tComparison file:\t', outFile[i][1], sep='')

        # Give the score for the test
        grade += thisGrade
        print('\t\tScore:\t\t', thisGrade, '/1', sep='')
        print('-'*50)
        # print('\n' + '-'*50 + '\n')

    # Display the overall score and return the final grade
    print('\tOVERALL SCORE:\t\t', grade, '/', len(args), sep='')
    print('\n' + '='*50 + '\n')
    return grade

def main():
    # Start the grade at 0
    grade = {}
    nGrades = {}

    # Loop through each function to be tested
    # for key,value in evalList.items():
    for func in funcList:
        # Get the function to be tested
        fcnStr = func

        # Initialize empty arrays
        args = []
        expectOut = []
        expectStdout = []
        stdin = []
        outFile = []

        # Loop through each test to be done on this function
        for j in evalList[func]:
            # Piece the test into its separate variables
            args.append         (j.get('args'))
            expectOut.append    (j.get('expectOut'))
            expectStdout.append (j.get('expectStdout'))
            stdin.append        (j.get('stdin'))
            outFile.append      (j.get('outFile'))
            nGrades[func] = nGrades.get(func,0) + 1

        # Perform the test and update the overall grade
        grade[func] = gradeFcn(fcnStr, args, expectOut, expectStdout, stdin, outFile)

    # Print the final grade
    print( 'SUMMARY:' )
    for func in funcList:
        print(func, ':\t', grade[func], '/', nGrades[func], sep='')
    gradeTotal = sum(grade.values())
    nGradesTotal = sum(nGrades.values())
    print( 'TOTAL:\t', gradeTotal, '/', nGradesTotal, ', ', gradeTotal*100//nGradesTotal, '%', sep='' )



# Values to be used in testing below
def writeFile(filename,info):
    f = open(filename,'w')
    f.write(str(info))
    f.close()

database = [
    ['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+'],
    ['SPH4U', 'Unit 1 Test', 'Yoda', '4+']
    ]

test1 = 'This\nis a\ttest.\n'
test2 = 42
test3 = database
#test4 = 'ICS4U\tAssignment 1\tLuke Skywalker\t3+\nSPH4U\tUnit 1 Test\tYoda\t4+\n'
test4 = 'ICS4U\tAssignment 1\tLuke Skywalker\t3+\nSPH4U\tUnit 1 Test\tYoda\t4+\n'
test5 = test4
writeFile('a3.test.1.txt',test1)
writeFile('a3.test.2.txt',test2)
writeFile('a3.test.5.txt',test5)




evalList = {
    'a3.writeString':       [{'args': ['test1.txt',test1],      'outFile': ['test1.txt','a3.test.1.txt']}],
    'a3.readString':        [{'args': ['a3.test.1.txt'],        'expectOut': test1}],
    'a3.writeNum':          [{'args': ['test2.txt',test2],      'outFile': ['test2.txt','a3.test.2.txt']}],
    'a3.readNum':           [{'args': ['a3.test.2.txt'],        'expectOut': test2}],
    'a3.array2TSV':         [{'args': [test3],                  'expectOut': test4}],
    'a3.TSV2array':         [{'args': [test4],                  'expectOut': test3}],
    'a3.writeTSV':          [{'args': ['test5.txt',test3],      'outFile': ['test5.txt','a3.test.5.txt']}],
    'a3.readTSV':           [{'args': ['a3.test.5.txt'],        'expectOut': test3}]
    }

funcList = ['a3.writeString','a3.readString','a3.writeNum','a3.readNum','a3.array2TSV','a3.TSV2array','a3.writeTSV','a3.readTSV']


'''
evalList = [
    {f: 'a2.level2Percent', args: [['3+']],                                 expectOut: [79]},
    {f: 'a2.percent2Level', args: [[78]],                                   expectOut: ['3+']},
    {f: 'a2.stringCompare', args: [['Luke Skywalker',' luke skywalker\n ']],expectOut: [True]},
    {f: 'a2.addGrade',      args: [[database, *addGradeIn]],                expectOut: [addGradeOut]},
    {f: 'a2.inputGrades',   args: [[database]],                             expectOut: [inputGradesOut], stdin: [inputGradesStdin]},
    {f: 'a2.studentAverage',args: [[database, 'luke skywalker']],           expectOut: [75.5]},
    {f: 'a2.courseAverage', args: [[database, 'sph3u  ']],                  expectOut: [83]}
    ]
evalList = [
    ['a2.level2Percent',    [['3+'], 79, None, None]],
    ['a2.percent2Level',    [[78], '3+', None, None]],
    ['a2.stringCompare',    [['Luke Skywalker', ' luke skywalker\n '], True, None, None]],
    ['a2.addGrade',         [[database, *addGradeIn], addGradeOut, None, None]],
    ['a2.inputGrades',      [[database], inputGradesOut, None, inputGradesStdin]],
    ['a2.studentAverage',   [[database, 'luke skywalker'], 75.5, None, None]],
    ['a2.courseAverage',    [[database, 'sph3u  '], 83, None, None]]
    ]
'''

# Redirect the stdout
main()
#f = open('grade.txt','w')
#with redirect_stdout(f):
#    main()
#f.close()
