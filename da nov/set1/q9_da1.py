'''
Get a list of float values from the user and convert the elements to integer.
Remove the duplicate values in the resultant list as well. 
Note: Do not use separate list. 
Store the result in the same list.
Input: [2.3, 25.9, 456.01, 31.1, 25.8, 31.8]
Output: [2,26,456,31,32]
'''
lst = []
n = int(input("Enter length of list : "))
print("Enter the elements of the list: ")

for i in range(0, n): 
    ele = float(input())
    lst.append(ele)

lst = [int(x) for x in lst]

nlst = []
[nlst.append(x) for x in lst if x not in nlst] #remove duplicate item using list comprehension

print(nlst)