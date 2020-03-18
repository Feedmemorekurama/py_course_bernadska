limit = int(input())
prev,cur = 0,1
print(prev,end =' ')

while cur < limit:
    print(cur,end =' ')
    prev,cur = cur,prev + cur