'''
Get a Python list of N integer values.
Find the presence of ODD and EVEN numbers in the list.
If the ODD number occurs at the ODD position replace the ODD number with 'odd'.
If the EVEN number occurs at the EVEN position replace the EVEN number with 'even'.

Find the number of odd places that were changed and also the number of even places that were changed

Prepare a new list for the odd and even positions.


Sample Input:
5 
231
453
806
1240
3228

Output: 

['odd', 453, 806, 'even', 3228]

odd=1

oddpositionlist=[0]

even=1

evenpositionlist=[3]

Test Case1:

Input:

5
23
45
80
12
32

Output:

['odd', 45, 80, 'even', 32]
odd= 1
oddpositionlist= [0]
even= 1
evenpositionlist= [3]

Test Case2:

Input:

6
23
44
3
12
71
33

Output:

['odd', 'even', 'odd', 'even', 'odd', 33]
odd= 3
oddpositionlist= [0, 2, 4]
even= 2
evenpositionlist= [1, 3]


'''

N=int(input()) #enter the length of list
lst=[]
for i in range(0,N):
    ele=int(input())
    lst.append(ele)

ce,co=0,0
oddpositionlist=[]
evenpositionlist=[]
for i in range(0,N):
    if lst[i]%2==0 and (i+1)%2==0:
        lst[i]='even'
        ce+=1
        evenpositionlist.append(i)
    elif lst[i]%2!=0 and (i+1)%2!=0:
        lst[i]='odd'
        co+=1
        oddpositionlist.append(i)
    else:
        pass

print(lst)
print("odd= ",co)
print("oddpositionlist= ",oddpositionlist)
print("even= ",co)
print("evenpositionlist= ",evenpositionlist)
    