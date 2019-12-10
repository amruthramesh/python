# Importing a Support Module
import Support
import math
import Fruit


def sampleFunction( data ):
    print data
    return 1;
Support.printFunction('# Sample Fucntion Execution')
sampleFunction("Amruth")
print '\t'    

    # Global and Local Variables 
total = 0; # This is global variable.
    # Function definition is here
def sum( arg1, arg2 ):
        # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   Support.printFunction('# Global and Local Variable Execution')
   print "Inside the function local total : ", total
   return total;

    # Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total
print '\t'

# Import function execution
Support.printFunction('# Import Function Execution')
Support.printFunction('Nani')
print '\t'

# dir() Execution
content = dir(math)
Support.printFunction('# dir() Execution')
print content
print '\t'

# Package Execution
Support.printFunction('# Package Execution')
Fruit.functionApplePrint()
Fruit.functionOrangePrint()
print '\t'


