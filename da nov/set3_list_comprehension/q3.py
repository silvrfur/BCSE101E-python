#Write a program using list comprehension to extract and print all the numbers from a given string.
str="shri9g404"
lst=[i for i in str if i.isnumeric()]
print(lst)