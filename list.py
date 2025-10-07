l=[15,20,2,35,4,65,4]
#list is mutable means changes can be made at any part of code
print(l)
print("Appending: ")
l.append(10)
print(l)
#ascending sorting
print("Sorting Ascending")
l.sort()
print(l)
print("Sorting Descending")
l.sort(reverse=True)
print(l)
print("Reverse")
l.reverse()
print(l)
print("returning index")
print(l.index(4))
print("count")
print(l.count(4))
print("copy")
m=l.copy()
print(l)
#inserting element
print("inserting")
l.insert(2,899) #inserting 899 at index 2
print(l)
print("Extend")
m=[100,400,200]
l.extend(m)
print(l)

