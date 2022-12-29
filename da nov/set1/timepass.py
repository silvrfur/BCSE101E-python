s="abbbccdddb"
# current=None
# str=None
# for x in s:
#     if x==current:
#         str=str+x
#     else:
#         current=x
#         str+=current
j=0
count2=0
for i in range(0,len(s)-1):
    i=j
    str=s[i]
    count=0
    for j in range(i+1,len(s)):
        
        if s[i]==s[j]:
            count=1
            str=str+s[j]
        else:
            # i=j
            if count==1:
                print(str)
                count2+=1
            # count+=1
            break
    
        