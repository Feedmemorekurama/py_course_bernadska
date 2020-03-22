my_list = [52, 9, 13 ,-84, 7, 25 ,-18, 32]
new_list = []
idx = 0
for i in my_list:
    if idx == 0:
        idx+=1
    elif i % idx ==0:
        new_list.append(i)
        
        idx+=1
    else:
        idx+=1

print(new_list)