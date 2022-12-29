# Write a program in python to calculate the net pay given basic pay, hra, da and deductions
bp=int(input("Enter the basic pay \n"))
hra=int(input("Enter the hra \n"))
da=int(input("Enter the da \n"))
deduction=int(input("Enter the deduction \n"))
np=bp+hra+da-deduction
print("The net pay is ",np)