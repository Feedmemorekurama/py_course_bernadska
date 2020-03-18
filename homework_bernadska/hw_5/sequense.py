my_list = [1, 2, 3, 4, 6, 7, 8]
i = 0
for j in my_list:
    if j - i != 1:
        i +=1        
else:
    print(f"The number {i} is not sequential")