'''
Get first, second best scores from the list. 
List may contain duplicates.
Ex: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85
'''
numbers=[86,86,85,85,85,83,23,45,84,1,2,0]

temp1,temp2 = numbers[0], numbers[1]

if temp1 < temp2:
        temp1, temp2 = temp2, temp1


for i in range(len(numbers)):
        if numbers[i] > temp2:
            if numbers[i] > temp1:
                temp2 = temp1
                temp1 = numbers[i]
            else:
                temp2 = numbers[i]
        else:
            if(temp1==temp2):
                temp2 = numbers[i]
        
print("Max is ", temp1)
print("Second max is ",temp2)