list_1 = [1, 5, 7]
list_2 = [5, 6, 3]
sum_list =[]
for i in range(0,len(list_1)):
    if len(list_1) != len(list_2):
        print("Both lists are not equal")
        break
    else:    
        sum_list = list_1[i] + list_2[i]
    print(sum_list)




    

