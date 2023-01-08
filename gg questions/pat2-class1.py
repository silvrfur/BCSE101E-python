'''
Get the following states and their number of districts as key and value pairs in a dictionary. 
Example: {'GOA':2, 'LADAKH':2, 'PUDUCHERRY':4, 'SIKKIM':4, 'DELHI':11, 'MEGHALAYA':11, 'MIZORAM':11, 'ANDHRA PRADESH':13, 'UTTARAKHAND':13, 'PUNJAB':23, 'WEST BENGAL':23, 'ASSAM':33, 'GUJARAT':33, 'RAJASTHAN':33, 'TELANGANA':33}
For every entered state,
- find its number of districts 
- count the number of states that has the same count of districts
- Form a new dictionary from the above-founded number of districts as key and the list of states that have the same number of districts as its value.

Sample i/p:
State1
2(No. of districts)
State2
2(No. of districts)
State3
4(No. of districts)
State4
4(No. of districts)
State5
11(No. of districts)
State6
11(No. of districts)
State7
11(No. of districts)
State8
13(No. of districts)
State9
13(No. of districts)
State10
23(No. of districts)
State11
23(No. of districts)
State12
33(No. of districts)
State13
33(No. of districts)
State14
33(No. of districts)
State15
33(No. of districts)
Sate12  [Search Key]
Sample o/p:
33
4
{33: ['Sate12', 'State13', 'State14', 'State15']}



Test case 1:

Input:

GOA
2
LADAKH
2
PUDUCHERRY
4
SIKKIM
4
DELHI
11
MEGHALAYA
11
MIZORAM
11
ANDHRA PRADESH
13
UTTARAKHAND
13
PUNJAB
23
WEST BENGAL
23
ASSAM
33
GUJARAT
33
RAJASTHAN
33
TELANGANA
33
GOA

Output:

2
2
{2: ['GOA', 'LADAKH']}

Test case2:

Input:

GOA
2
LADAKH
2
PUDUCHERRY
4
SIKKIM
4
DELHI
11
MEGHALAYA
11
MIZORAM
11
ANDHRA PRADESH
13
UTTARAKHAND
13
PUNJAB
23
WEST BENGAL
23
ASSAM
33
GUJARAT
33
RAJASTHAN
33
TELANGANA
33
MEGHALAYA

Output:

11
3
{11: ['DELHI', 'MEGHALAYA', 'MIZORAM']}
'''

dict={}
l=int(input()) #input the length of dictionary
for i in range(l):
    state=input() #input the state
    dis=int(int(input())) #input the no. of districts

    dict[state]=dis
search_dis=input()
print(dict[search_dis])
count=0
lst=[]
for i in dict:
    if dict[i]==dict[search_dis]:
        count+=1
        lst.append(i)
new_dict={dict[search_dis]:lst}
print(count)
print(new_dict)

