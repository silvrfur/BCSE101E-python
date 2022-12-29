# Check whether the given number is palindrome or not 
num=int(input())
n=num
rev=0
while(n!=0):
    rev=(rev*10)+(n%10)
    n//=10
print("rev num is ",rev)
if rev==num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")