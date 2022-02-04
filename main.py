title1 = "WK2 Challenges I, Part 3"
title1 = title1.upper()

input(title1)

total = 0
for num in range(21):
    total = total + num
    
print(total)


total = 0
for num in range(21):
    total = total + num
    print(total) # Wanted to see how the 'for' loop works.

print(" ")

import operator

numbers = range(0,21)
for num in numbers:
  if num <0:
    if num >= 20:
      total = operator.add(total, num)
  
print(total)

# My initial attempts (some are not as intuitive; clunky):

twenty = [x for x in range(21) if x % 1 == 0]
print(twenty)
sum_20 = sum(twenty)
print(sum_20)

rnge = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rngesum = sum(rnge)
print(rnge)
print(rngesum)

rnge2 = []
for x in range(50):
  if x > 0:
    if x < 21:
      rnge2.append(x) 
print(rnge2)
sum_rnge2 = sum(rnge2)
print(sum_rnge2)

#Did this to see what .append really does:
rnge3 = []
for x in range(50):
  if x > 0:
    if x < 21:
      rnge3.append(x) # So .append is a "collector" of sorts?
print(rnge3)

###############################################

title2 = "WK2 Challenges I, Part 4"
title2 = title2.upper()

input(title2)

num1 = int(input("Pick a number. Any number. "))
num2 = int(input("Pick another number. Again, any number will do. "))
num3 = int(input("Pick a third number. "))
num4 = int(input("Pick a fourth number. "))

numbers = [num1, num2, num3, num4]
numbers.sort()
# numbers = numbers.sort() is incorrect. Why, though?

max = numbers[3]
min = numbers[0]

print(f"Your max number is {max}.")
print(f"Your min number is {min}.")

print(" ")

## list_name.sort(reverse=True) --> sort the given list in descending order

# list_name.sort(key=…, reverse=…) --> sorts according to user’s choice. Parameters:
    # reverse: reverse=True will sort the list descending. Default is reverse=False
    # key: A function to specify the sorting criteria(s)

###########################################################
title3 = "WK2 Challenges I, Part 5"
title3 = title3.upper()

input(title3)

import operator
num1 = float(input("Pick a number. Any number. "))
num2 = float(input("Pick another number. Again, any number will do. "))
total = round(operator.add(num1,num2))

print(f"Your total is {total}.")

#I TRIED ALL  OF THESE:
# numbers = [num1,num2]
# numbers.add(numbers)
# total = sum(num1,num2)
# total = sum(num1:int,num2:int)
# print(numbers)








# ADDITIONAL NOTES # (FOR REFERENCE LATER)

# total = num1 + num2--> works, but doesn't use .add()

# #for x in rnge if x % 1 == 0:
#  # rnge.append(x)
# #print(rnge)


# five = list(input("Enter five numbers, from one to nine. "))
# print(five)


# inrange = list(input("Enter five numbers, from one to nine. "))
# newrange = tuple(inrange)-> TUPLES CANT SPLIT!
# #for x in newrange:
#   #if x % 1 == 0:
#    # newrange.append(x)
#     #print(inrange)
# #numlist = int(inrange)
# print(inrange)
# print(newrange)
# #fivesum = sum(newrange)


# inrange2 = list(input("Enter five numbers, from one to nine. "))
# #? inrange = [st for st in {inrange2}]
# for x in inrange:
#   if x % 1 == 0:
#     inrange.append(x)
#     #print(inrange)
# print(inrange)


# #four = input("Enter four numbers, from one to eight. ")
# #newfour = list(four)
# #print(newfour)



