a = int(input("enter the value 1: "))
b = int(input("enter the value 2: "))
c = int(input("enter the value 3: "))
#largest number
#all three are equal
# if any two are equal

if a == b == c:
  print("all three numbers are equal")
elif a == b or b == c or a == c:
  print("Two numbers are equal")
  if a == b:
    print("First and Second are equal")
  elif b ==c:
    print("Second and Third number are equal")
  elif a == c:
    print("First and Third number are equal")
else:
  if a > b and a > c:
    print("First number is the Largest")
  elif b > a and b > c:
    print("Second number is the Largest")
  elif c > a and c > b:
    print("Third number is the Largest")
