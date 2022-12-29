'''
Have a list of number of days in a month and another list of months. Traverse through both the lists appropriately. 
Write program to display number of days in a month when the user enters the month.
L1=[Jan,Feb,March...]
L2=[31,28,31..]
Input: Dec
Output:31
'''
month=input("Enter the month \n")
L1=['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
L2=[31,28,31,30,31,30,31,31,30,31,30,31]
i=L1.index(month)
print(L2[i])