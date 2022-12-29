# Write a Python program that accepts a word from the user and reverse it
wrd=input()
for i in reversed(range(0,len(wrd))):
    print(wrd[i],end="")
