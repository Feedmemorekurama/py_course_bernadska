list_1 = [15, 56, 17]
list_2 = [25, 8, 23]
sum_list =[]
for i in range(0,len(list_1)):
    if len(list_1) != len(list_2):
        print("Both lists are not equal")
        break
    else:    
        sum_list = list_1[i] + list_2[i]
    print(sum_list)




    

