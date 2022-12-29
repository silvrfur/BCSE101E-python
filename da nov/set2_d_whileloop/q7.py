# Compute the GCD of two numbers.(Euclidean Method and using common factors) 
x=int(input()) #input number 1
y=int(input()) #input number 2

if x>y:
    smaller=y
else:
    smaller=x

for i in range(1,smaller+1):
    if x%i==0 and y%i==0:
        hcf=i

lcm=(x*y)/hcf
print("hcf is: ",hcf)
print("lcm is: ",lcm)