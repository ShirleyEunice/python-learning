# Data Types:
# 1. String - Character/Word
s = 'Hello'
print(type(s))
# 2. Integer - Numbers
a = 12
print(type(a))
# 3. Boolean- True/False
result = True
print(type(result))
# 4. Float - Numbers with decimal points
b = 12.45
print(type(b))
# 5. None
# 6. List 
# l = [20, 40, 50] - Array - List
# l = variable
# [] -> square bracket 
# 20, 40, 50 -> items of List
#--------------------------------
fruits = ['apple', 'banana', 'cherry', 'pineapple', 'orange'] #0-1-2-3-4
print(fruits)
print(fruits[0])
print('Hello ' + fruits[2])
print( ['apple', 'banana', 'cherry', 'pineapple', 'orange'][4])
# print(fruits[100]) - list index out of range
# print(fruits[1.0]) - list indices must be integers or slices, not float
print(fruits[int(1.0)])
#------------------------------------
list2 = [
  ['apple', 'banana', 'cherry', 'pineapple', 'orange'], #list1 - 0 -> [0][0] -. [0][3]
  [10, 20, 30, 40, 50] #list2 - 1
  ]
print(list2[0])
print(list2[1])
print(list2[0][3])
print(list2[1][1])
#------------------------------------
#Negative Indexes
num = [1, 2, 3, 4, 6] #
# Positive index - 0 -> 1 -> 2 -> 3-> 4
# Negative index - -5 -> -4 -> -3 -> -2 -> -1 
print(num[4])
print(num[-5])
# num[0] -> index representation -> Single value
# num[0:3] -> Slice representation -> Multiple values
# In slice 0 -> First Index: Start of the index
#          3 -> Second Index: End of the index but will not include, the value at the second index
print(num[0:3]) # [1, 2, 3]
print(num[0:5])
print(num[0:-1])

