#lists- they are used to store strings in square brackets and their numbering starts from 0
'''numbers=[10,11,12,13,14]
print(numbers[2])
print (numbers)
'''
#list inside list- there csan be list inside list and use it like matrix
'''name=[
    [1,2,3,4,5],
    [6,7,8,9,0]
      ]
print(name[1][2])'''

#we can also extract a value from a string by using this method
'''name ="Pratik Shah"
print(name[7])'''

#list operations
#element in a list can be swapped
'''numbers=[5,4,3,2,1,0]
numbers[2]=9
print(numbers)'''

#a list can be concantated or added to another list and can be even multiplied 
'''nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)'''

#we can check if there is any item present in a list
'''words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
'''
#this method can be used along with boolean logic also
nums = [1, 2, 3]
print(not 4 in nums)
print(not 3 in nums)