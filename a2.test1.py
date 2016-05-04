# Import the assignment
import a2

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
        return bool( re.search(b,a) )
    else:
        # Non-strings: compare using ==
        return a == b


def gradeFcn(fcnStr, args, expectOut, expectStdout, stdin):
    ''' Main grading function. '''

    # Start the grade at 0 and display some feedback
    grade = 0
    print(fcnStr, ':', sep='')

    # Try to find the specified function
    try:
        fcn = eval(fcnStr)
    except Exception:
        print('\tDoes not exist')
        return grade

    # Loop through each set of arguments (separate tests)
    for i in range(len(args)):
        # Run the function with the right inputs
        output, stdout = runWith(fcn, args[i], stdin[i])

        # Display the results of the test
        print('\tTest ', i+1, ':\n\t\tInput:\t\t', args[i], sep='')
        if stdin[i] != None:
            print('\t\tUser Input:\t', repr(stdin[i]), sep='')
        if expectOut[i] != None:
            grade += compare(output, expectOut[i])
            print('\t\tOutput:\t\t', repr(output), '\n\t\tExpected:\t', repr(expectOut[i]), sep='')
        if expectStdout[i] != None:
            grade += compare(stdout, expectStdout[i])
            print('\t\tUser Output:\t', repr(stdout), '\n\t\tExpected:\t', repr(expectStdout[i]), sep='')

    # Display the overall score and return the final grade
    print('\tOVERALL SCORE:\t\t', grade, '/', len(args), sep='')
    print('\n' + '-'*50 + '\n')
    return grade

# Values to be used in testing below
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
addGradeIn = ['SPH3U', 'Catapult project', 'Jar Jar Binks', '2']
addGradeOut = database + [addGradeIn]
inputGradesStdin = 'SPH3U\nUnit 2 Test\nChewbacca\n1-\nyes\nHan Solo\n3\nno\n'
inputGradesOut = database + [['SPH3U', 'Unit 2 Test', 'Chewbacca', '1-'], ['SPH3U', 'Unit 2 Test', 'Han Solo', '3']]

# A list of inputs/outputs to test each function with
# Format: ['Function name', [[List_of_args], Expect_out, Expect_stdout, stdin]]
evalList = [
    ['a2.level2Percent', [['3+'], 79, None, None]],
    ['a2.percent2Level', [[78], '3+', None, None]],
    ['a2.stringCompare', [['Luke Skywalker', ' luke skywalker\n '], True, None, None]],
    ['a2.addGrade', [[database, *addGradeIn], addGradeOut, None, None]],
    ['a2.inputGrades', [[database], inputGradesOut, None, inputGradesStdin]],
    ['a2.studentAverage', [[database, 'luke skywalker'], 75.5, None, None]],
    ['a2.courseAverage', [[database, 'sph3u  '], 83, None, None]]
    ]

# Start the grade at 0
grade = 0
nGrades = 0

# Loop through each function to be tested
for i in range(len(evalList)):
    # Get the function to be tested
    fcnStr= evalList[i][0]

    # Initialize empty arrays
    args = []
    expectOut = []
    expectStdout = []
    stdin = []

    # Loop through each test to be done on this function
    for j in range(1,len(evalList[i])):
        # Piece the test into its separate variables
        args.append(evalList[i][j][0])
        expectOut.append(evalList[i][j][1])
        expectStdout.append(evalList[i][j][2])
        stdin.append(evalList[i][j][3])
        nGrades += 1

    # Perform the test and update the overall grade
    grade += gradeFcn(fcnStr, args, expectOut, expectStdout, stdin)

# Print the final grade
print( grade, '/', nGrades, ', ', grade*100//nGrades, '%', sep='' )

