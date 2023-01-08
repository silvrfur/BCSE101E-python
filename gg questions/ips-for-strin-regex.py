'''
Given two strings, s1 (all Upper Case) and s2 (All lowerCase), create a mixed String
Instructions:
Create a third-string made of the first char of s1 then the last char of s2, Next,
the second char of s1 and second last char of s2, and so on. Any leftover chars
go at the end of the result.

Check whether the output string follows the pattern of Upper and lower case alphabets being available in the alternate position.

If not in the expected pattern, Please display "Does Not Follow Any Pattern"

If it follows the pattern, then display, "Follows Pattern"

Test Case1:

Input:

ABC
xyz

Output:

AzByCx
Follows Pattern

Test Case2:

Input:

CDEf
lmn

Output:

CnDmElf
Does Not Follow Any Pattern
'''