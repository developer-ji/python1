a = [1,2,"s","d",0.3,0.4]
b =[]
c =[]
d =[]
for i in a:
    if type(i) == int:
        b.append(i)
    if type(i) == str:
        c.append(i)
    if type(i) == float:
        d.append(i)
        
    
    
print("int value = {}".format(b))
print("str value = {}".format(c))
print("float value = {}".format(d)) 
        