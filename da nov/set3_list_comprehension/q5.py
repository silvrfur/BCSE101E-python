#Write a Python program to create a new list of Numbers that are divisible by 7 from all the numbers in the range of 1-1000
lst=[i for i in range(1,1000) if i%7==0]
print(lst)
