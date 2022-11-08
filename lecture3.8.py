#range function-this function is used to display the numbers starting from 0 and increasing by 1
'''numbers =list(range(10))
print(numbers)'''

#If range is called with one argument, it produces an object with values from 0 to that argument.
#If it is called with two arguments, it produces values from the first to the second.
'''numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))
'''

#range can have a third argument, which determines the interval of the sequence produced, also called the step.
'''numbers = list(range(5, 20, 2))
print(numbers)
'''
#The for loop is commonly used to repeat some code a certain number of times. This is done by combining for loops with range objects.
for i in range(5):
    print("hello!")
