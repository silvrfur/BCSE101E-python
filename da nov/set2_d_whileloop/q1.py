# Compute Exponentiation (power of a number) without using ** operator.
base=int(input("Enter the base \n"))
exp=int(input("Enter the exponent \n"))

i=0
ans=1
while(i<exp):
    ans*=base
    i+=1

print("Computed exponetial is: ",ans)