#while loop-The code below outputs each item in the list and adds an exclamation mark at the end(it is used to iterate over items such as strings)
'''words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")'''

#The for loop can be used to iterate over strings, in the code below it is used to find the number of times letter t is written
#the count statement is the initial count i.e.=0
str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

#Both, for and while loops can be used to execute a block of code for multiple times.
#It is common to use the for loop when the number of iterations is fixed. For example, iterating over a fixed list of items in a shopping list.
#The while loop is used in cases when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop.
#For example, ending the loop when the user enters a specific input in a calculator program.