list_1 = [0,2,-1,8,-20,3,-75,71,-50,12,27]
i = j = 0
i1 = i3 = i6 = 0

while i < len(list_1):
    if list_1[i]>0:
        if j == 1:
            i1 = i
        elif j == 3:
            i3 = i
        elif j == 6:
            i6 = i
            break
        j+=1
    i+=1
#if i6>0:
    #s_list = list_1[i1]*list_1[i3]*list_1[i6]
print(i1,i3,i6)