
total = 0
for num in range(21):
    total = total + num
    
print(total)


total = 0
for num in range(21):
    total = total + num
    print(total)


num1 = int(input("Pick a number. Any number."))
num2 = int(input("Pick another number. Again, any number will do."))
num3 = int(input("Pick a third number."))
num4 = int(input("Pick a fourth number."))

numbers = [num1, num2, num3, num4]
numbers.sort()
# numbers = numbers.sort() is incorrect. Why, though?
## list_name.sort(reverse=True) --> sort the given list in descending order

# list_name.sort(key=…, reverse=…) – it sorts according to user’s choice. Parameters:
    # reverse: reverse=True will sort the list descending. Default is reverse=False
    # key: A function to specify the sorting criteria(s)
max = numbers[3]
min = numbers[0]

print(f"Your max number is {max}.")
print(f"Your min number is {min}.")

# for every num in numbers:
#   if 

# if numbers < 
# twenty = [x for x in range(21) if x % 1 == 0]
# print(twenty)
# sum_20 = sum(twenty)
# print(sum_20)

# rnge = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# rngesum = sum(rnge)
# print(rnge)
# print(rngesum)

# rnge2 = []
# for x in range(50):
#   if x > 0:
#     if x < 21:
#       rnge2.append(x)
# print(rnge2)
# sum_rnge2 = sum(rnge2)
# print(sum_rnge2)


# rnge3 = []
# for x in range(50):
#   if x > 0:
#     if x < 21:
#       rnge3.append(x)
# print(rnge3)

# #for x in rnge if x % 1 == 0:
#  # rnge.append(x)
# #print(rnge)


# five = list(input("Enter five numbers, from one to nine. "))
# print(five)


# inrange = list(input("Enter five numbers, from one to nine. "))
# newrange = tuple(inrange)
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



