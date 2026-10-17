numbers = [10,20,30,40,50]

max_num = numbers[0]
min_num = numbers[0]

for i in numbers:
    if i > max_num:
        max_num = i
        
    elif i < min_num:
        min_num = i
        
print(max_num,end=" ")
print(numbers.index(max_num))
print(min_num,end=" ")
print(numbers.index(min_num))        