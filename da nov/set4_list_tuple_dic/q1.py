#transpose of a given matrix

#how to input a matarix
lst=[]

M=int(input("Enter the number of rows"))
N=int(input("Enter the number of columns"))
for i in range(M):
    ilst=[]
    for j in range(N):
        print("Enter the number at row= ",i," column= ",j)
        ele=int(input())
        ilst.append(ele)
    lst.append(ilst)

print("The matrix is: ",lst)

#transpose of a given matrix
newlst=[]
newlst=[[0,0,0],[0,0,0],[0,0,0]] #imp step
for i in range(len(lst)):
    for j in range(len(lst[0])):
        newlst[j][i]=lst[i][j]
    #     iilst=[]
    #     ele=lst[j][i]
    #     # print("the extracted element", ele)
    #     iilst.append(ele)
    # # print("The inner list",ilst)
    # newlst.append(iilst)
newlst=[[lst[j][i] for j in range(len(lst[0]))] for i in range(len(lst))]
print("matrix after transpose: ",newlst)