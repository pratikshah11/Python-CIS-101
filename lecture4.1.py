#reusing code-it is very important and can be used in big programs for multiple times
#functions-we can define and make some functions in addition to using pre defined functions
'''def func():
    print("hello world")
    print("Pratik Shah")
    
func()'''
#you have to define a function and then you can call it, remember that after defining a function you will have to call it if you want to run that
#functions have to be first defined and then they can be called and not before that

#function arguments- in this function, we can use the function combining it with some other function
'''def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")'''

#Arguments- You can also define functions with more than one argument; separate them with commas.
'''def print_sum_twice(x, y):
   print(x + y)
   print(x - y)

print_sum_twice(5, 8)'''

#Arguments-function arguments can be used as variables inside the function definition.
def function(variable):
    variable += 1
    print(variable)

function(7)
