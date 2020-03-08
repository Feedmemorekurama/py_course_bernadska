my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(my_list)
search_val = 100
found = False
idx = 0

while idx < len(my_list):
    if my_list[idx] == search_val:
       found = True
       break

    idx += 1

if not found:
    my_list.append(search_val)

print(my_list)