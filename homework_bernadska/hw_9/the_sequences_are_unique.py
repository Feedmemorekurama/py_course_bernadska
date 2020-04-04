import random
n = 10
my_list = []
while len(my_list) < 10:
    my_list.append(random.randint(0,50))


print(my_list)
for i in range(n-1):
    for j in range(i+1,n):     
        if my_list[i] == my_list[j]:
            print("the numbers are repeated ")
            quit()
print("All number unique")