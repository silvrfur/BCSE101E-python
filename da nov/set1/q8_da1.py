'''
Get a list of intergers from the user. 
Find the sum of all the elements in the even position of the list and store it 
in a variable called "EvenSum".
Find the average of all the elements in the odd position of the list and store 
it in another variable called "OddAverage"
Display both the values
'''
lst = []
n = int(input("Enter length of list : "))
print("Enter the elements of the list: ")

for i in range(0, n): 
    ele = int(input())
    lst.append(ele)

EvenSum=0
sa=0
c=0
for i in range(0,n):
    if i%2==0 or i==0:
        EvenSum+=lst[i]
    else:
        sa+=lst[i]
        c+=1
OddAverage=sa/c
print("Sum of elements at even position is: ",EvenSum)
print("Average of all elements in odd position is: ",OddAverage)