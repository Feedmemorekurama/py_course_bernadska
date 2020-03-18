my_list = [1, 5, 7, 10, 16, 8, 20, 27, 15, 25]
num =int(input("Enter num:"))

for i in my_list:
    if num == 0:
        print("not delete 0")
        break
    elif i % num == 0:
        print("This number is divided =",i)
    else:
        print("This {} is not divisible by {}".format(i,num))