#while loops-loops are things which keep on repeting untile the statement is true
'''i=0
while i<10:
    i=i+1
    print (i)'''

#concatenating loops- concatenating a while loop with a conditional statement
'''x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1 '''

#break statement- to end a while loop prematurely, the break statement can be used.
'''i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")'''

#continue statement- Unlike break, continue jumps back to the top of the loop, rather than stopping it
i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)