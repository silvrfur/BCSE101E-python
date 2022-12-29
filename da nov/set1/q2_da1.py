''' 
WAP to find the sum of series: 
a) 1 + 1/2 + 1/3 + ….. + 1/N.
b) 1 + 2/4 + 3/9 + ....+ N/(N*N)
c) 1 + sqrt(2) + sqrt(3) + sqrt(4) + sqrt(N) 
'''

import math
sa=0
sb=0
sc=0
N=int(input("Enter N: \n"))
for i in range(1,N+1):
    sa=sa+(1/i)
    sb=sb+(1/i*i)
    sc=sc+math.sqrt(i)
print("Sum of series a= ",sa)
print("Sum of series b= ",sb)
print("Sum of series c= ",sc)