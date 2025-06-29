n =int(input("How many limit of number you need to add?")) #3
#3-> 5+10+15=30
sum = 0
for i in range(n):#1-> 2->3 ->4
  num=int(input(f"Enter your {i+1} number:"))#5 ->10 ->15
  sum += num #0+5->5 , 5+10->15, 15+15->30

print("The total sum is: ", sum)