#Obtain a character, check if it is lower case, uppercase or digit. (elif statement)
ch=input("Enter the character \n")
if ch.islower():
    print("Character entered is lower case")
elif ch.isupper():
    print("Character entered is upper case")
elif ch.isdigit():
    print("Character entered is digit")
else:
    pass