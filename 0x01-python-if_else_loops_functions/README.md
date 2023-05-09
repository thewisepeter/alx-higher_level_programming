0x01. Python - if/else, loops, functions

If/Else Statements
In Python, if/else statements are used to control the flow of the program based on some condition. The basic syntax for an if/else statement is:

if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false

Here, condition is an expression that evaluates to a Boolean value (True or False). If condition is true, the code inside the if block is executed; otherwise, the code inside the else block is executed.

You can also use elif (short for "else if") to chain multiple conditions together:

if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true and condition1 is false
else:
    # code to execute if both condition1 and condition2 are false

Loops
Python has two types of loops: for loops and while loops.

For Loops
A for loop is used to iterate over a sequence (e.g. a list, tuple, or string) and execute a block of code for each item in the sequence. The basic syntax for a for loop is:

for item in sequence:
    # code to execute for each item


Here, item is a variable that will take on the value of each item in the sequence, and sequence is the sequence of items to iterate over.

While Loops
A while loop is used to repeatedly execute a block of code while some condition is true. The basic syntax for a while loop is:

while condition:
    # code to execute while condition is true


Here, condition is an expression that evaluates to a Boolean value. The code inside the loop will continue to execute as long as condition is true.

Functions
In Python, a function is a named block of code that performs a specific task. Functions can take arguments (input) and return values (output). The basic syntax for defining a function is:

def function_name(arguments):
    # code to execute
    return value

Here, function_name is the name of the function, and arguments is a comma-separated list of input arguments (if any). The code inside the function will execute when the function is called, and the return statement specifies the value the function will return (if any).

You can call a function by using its name, followed by parentheses that contain any arguments you want to pass to the function (if it takes any). For example:

result = function_name(argument1, argument2)

This will call the function function_name, passing it two arguments, and store the result in the variable result.
