#a = [1,1,2,3,5,8,13,21,34,55,89]
#b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

list_a = set([1,1,2,3,5,8,13,21,34,55,89])
list_b = set([1,2,3,4,5,6,7,8,9,10,11,12,13])

all_list = list_a.union(list_b)
all_list = sorted(all_list)
print(all_list)