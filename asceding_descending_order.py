l = [10,30,20,40,50]
i = 0
for i in range(i,len(l)):
	for j in range(i+1,len(l)):
		if l[i]>l[j]:
			val = l[i]
			l[i] = l[j]
			l[j]= val
print("Asecending_order = ",l)

l = [10,30,20,40,50]
i = 0
for i in range(i,len(l)):
	for j in range(i+1,len(l)):
		if l[j]>l[i]:
			val = l[i]
			l[i] = l[j]
			l[j]= val
print("Descending_order",l)					
