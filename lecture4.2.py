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
s = "My name is Pratik."
s1=s.replace("Pratik.", "Pratik Shah.")
print(s1)