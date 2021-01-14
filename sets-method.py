 # creating an empty set
b = set()
print(type(b))

 # adding values to an empty set

b.add(4)
b.add(6)
b.add(4)
b.add(6)
b.add(4)            # adding a value repeatedly does not changes a set

b.add((4,5,7,8,8))
# accessing element
# b.add({4:5})        # cannot add add list or dictionary to sets...

print(b)
# length of the set
print(len(b))       # print the lenght of the sets...
# removal of an items ...
#b.remove(4)        # remove 4 from set b
#b.remove(34)       # throws an error while trying to remove  34 (which is not present in the sets)
#print(b)        

#print(b.pop())
# print(b.clear())
#print(b.union()) 
#print(b.intersection())

