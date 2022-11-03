#boolean logic- there are three boolean login in python -and, or, not. This boolean logic can also be used in conditional statement
#boolean and-if both inputs are true, then output will be true
'''print(1==1 and 2==2)
print(1==1 and 1==2)
print(1==2 and 2==1)
'''
#boolean or- if either input is true, output will be true
'''print(1==1 or 2==2)
print(1==1 or 1==2)
print(1==2 or 2==1)
'''
#boolean not- if the input is true , output will be false
'''print(not 1==1)
print(not 1==2)'''

#operator precedence- its like extension of mathematical idea with boolean logic
'''print(False == False or True)
print(False == (False or True))
print((False == False) or True)
'''

#chaining multiple conditions
marks=int(input("Enter your marks"))
if (marks>=70 and marks<=100):
    print("Passed!")