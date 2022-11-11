#returning from functions-Certain functions, such as int or str, return a value that can be used later, To do this for your defined functions, you can use the return statement.
'''def max(x,y):
    if x>y:
        return x
    else:
        return y
print(max(2,3))
y=max(4,5)
print(y)'''
#if print command is used in this conditional statement, then there will an extra output

#Once you return a value from a function, it immediately stops being executed. Any code after the return statement will never happen.
'''def add_numbers(x, y):
    total = x + y
    return total
    print("lol")

print(add_numbers(4, 5))'''

#replace function- this replaces some specific string with what you want
'''s = "My name is Pratik"
s1=s.replace("Pratik", "Pratik Shah")
print(s1)
'''

#another way of calling a function with multiple arguments
'''def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))'''

#use return functions while using a function

#Functions can also be used as arguments of other functions.
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

#comment- any line which starts with is # is a comment
#Docstrings- multiple lines of comment can be saved between '''    '''