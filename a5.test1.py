# Import the assignment
import a5

# Import required libraries
import io, sys, re, copy, os, shutil
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
def makeFiles(root,files):
    # Remove the folder (and everything in it) if it exists already
    if os.path.exists(root):
        shutil.rmtree(root)
    # Create the folder
    os.makedirs(root)

    # Loop through each file to create
    for file in files:
        if type(file) is dict:
            # dicts are used for subdirectories
            for subdir in file.keys():
                # Loop through each subdirectory and make its files
                filePath = os.path.join(root,subdir)
                makeFiles(filePath,file[subdir])
        else:
            # Make the given file
            filePath = os.path.join(root,file)
            f = open(os.path.join(root,file),'a')
            f.close()

    # End the function
    return

root = 'a5test'
files = ['a.txt', 'b.txt',
         {'folder1': ['c.txt','d.txt'],
          'folder2': ['e.txt','f.txt']} ]
makeFiles(root,files)
printFilesOut = 'a5test\\a.txt\na5test\\b.txt\na5test\\folder1\\c.txt\n' + \
                'a5test\\folder1\\d.txt\na5test\\folder2\\e.txt\n' + \
                'a5test\\folder2\\f.txt\n'

evalList = {
    'a5.power':             [{'args': [6,4],        'expectOut': 1296}],
    'a5.morePower':         [{'args': [7,5],        'expectOut': 16807}],
    'a5.GCF':               [{'args': [36,20],      'expectOut': 4}],
    'a5.isPalindrome':      [{'args': ['civic'],    'expectOut': True}],
    'a5.printFiles':        [{'args': ['a5test'],   'expectStdout': printFilesOut}],
    }

funcList = ['a5.power', 'a5.morePower', 'a5.GCF', 'a5.isPalindrome', 'a5.printFiles']


# Redirect the stdout
main()
#f = open('grade.txt','w')
#with redirect_stdout(f):
#    main()
#f.close()
