lst =[[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
x = 0
y = 0
count = 0
count1 = 0
li = []
l1 = []


for i in lst:
    li.append(i[x])
    count = count+i[x]
    x = x+1
        
    y = y+(-1)
    count1 = count1+i[y]
    l1.append(i[y])
   
print(li)
print(l1)
print(count)
print(count1)
print(count-count1)

