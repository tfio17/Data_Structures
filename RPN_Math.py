#
#
## Tom
#
## Assignment 1
#

'''


The way math equations are presented and worked on classically is called “infix” notation.

(3+4)*5/((2+4) evaluates to 7*5 / 6 to 12 / 6 to 2.

There are other kinds of notations.  Famously, there is “Polish”

notation where the operator proceeds the operands.  +34 would be 7 and so forth.

This is called “prefix” notation.

Computer Scientists are fond on RPN or reverse polish notation.

That’s when the operator appears AFTER the operands.

They like it because then we can use stacks to do arithmetic.

This is called postfix notation.

Write a program that uses stacks to solve postfix equations.

Do the example in the slides and these as well:

Read the below in a strings, character by character, into a stack and solve them.

3 2 + 4 * 5 1 - /

4 7 8 * / 2 1 + +

4 5 + 7 2 - *

'''

# begin with an empty stack and an input stream

# Think about it like this:


# while more input, do:
#       read next input symbol
#       if it is a numeral,
#           push it onto the stack
#       if it's an operator
#           pop two numerals from stack
#               perform operation on numerals
#               push result
# end

# the answer is on the top of the stack, pop it



# Let's Begin:

eq1 = "3 2 + 4 * 5 1 - /"
eq2 = "4 7 8 * / 2 1 + +"
eq3 = "4 5 + 7 2 - *"


def compute(string):
    stack = list()
    inList = list(string.split(' '))
    inList.reverse()

    while len(inList) != 0:
        #print("Processing item:",i)
        x = inList.pop()
        #print("x is",x)
        if x.isnumeric():
            stack.append(x)
        else:
            #print("The stack:", stack)
            y = stack.pop()
            z = stack.pop()
            if x == '+':
                ans = int(y) + int(z)
            elif x == '-':
                ans = int(y) - int(z)
            elif x == '/':
                ans = int(y) / int(z)
            elif x == '*':
                ans = int(y) * int(z)
            else:
                print("Hmmmmmmm.......")
            #print(ans)
            stack.append(ans)

    return stack.pop()

                      

print(compute(eq1))
print(compute(eq2))    
print(compute(eq3))
