# List
# List is mutable

l = [11 , 45 , 19 , 2]
print(l)
l.append(81)
print(l)
m = l # this means m is a refferece of l and any changes in m will reflect the change in l
m[0] = 2 
#----------------------------------------------------------------------------
l1 = [11 , 45 , 19 , 2]
m1 = l1.copy();
m1[0] = 2 
print(l1)
l1.sort(reverse=True) #Descending
print(l1)
l1.sort(reverse=False) #Ascending
print(l1)
l1.insert(1 , 899)  #(index , value)
print(l1)
l1.extend([5])
l1.extend(m)
print(l1)

k = l + m  # Concatenate list
print(k)