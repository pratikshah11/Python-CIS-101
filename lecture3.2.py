#if statement - it is a conditional statement and gives some output if specified and the condition matches
'''
number= int(input("Enter a number "))
if number>0:
    print("This is a positive number")
    if number<100:
        print("This is a number between 1 and 100")
'''

#if-else statement - its a conditional statement which gives some output if specified and if the if condition does not match
'''
number= int(input("Enter a number "))
if number>0:
    print("This is a positive number")
else:
    print("This is a negative number")
'''

#multiple else if statement- else statement can be added multiple times with a different condition
'''number= int(input("Enter a number "))
if number>0:
    print("This is a positive number")
else:
    if number ==0:
        print("This is zero")
    else:
        print("This is a negative number")'''

#elif statement- short form of multiple else if statement
number= int(input("Enter a number "))
if number>0:
    print("This is a positive number")
elif number ==0:
    print("This is zero")
else:
    print("This is a negative number")