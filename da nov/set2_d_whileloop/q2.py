# Write a program in python to print all the two digit numbers which are either divisible by 3 or by 4. 
i=10
while(i<100):
    if i%3==0 or i%4==0:
        print(i)
    i+=1
