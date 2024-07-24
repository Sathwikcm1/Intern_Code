a, b, c = (1,2,3)
print(a)
print(b)
print(c)
#

#sets: no duplicates : 
# an unordered collection of items. every set element is unique andmust be immutable
# however a set itself is mutable. we can add or remove items from it.

#characteristics : 
# unordered, mutable, No duplicates, can't contain mutable data types.
s = set()
# an empty set is created.

s = {1,2,3,4,4,5}
print(type(s)) # print the data type which is set.
# print(s)
# s2 = {1,3,5,[3,5],5} # will throw an erorr : cuz set can only contain immutable items.

s3 = {1,2,34,4,(3,5),5} 
print(s3)
# print(s2)

s4 = {1,2,4,5,"goodbye world",3}  #todo: check this for it is printing ordered items.
print(s4)

s5 = {1,2,1,1,1,1,} # prints just 1,2.


s7 = {1,2,3}
s8 = {3,2,1}
print(s7)
print(s8)

# s7[0] # won't work, because of unordered and it is stored in datatype : Hashmap.

#add function

s7.add(2000)
print(s7)


#update() function: we can use 
s7.update([23,23,45,65])
print(s7)

#set operation:
#union() |
s11 = {3,4,5,5,4,6}
s12 = {4,3,5,5,5}
print(s11 | s12)

#intersection function:
print(s11 & s12)


#iteration:
dir(s) 


#Frozen set:
# it is stricly immutable, cannot modify once declared or initiliased.

fs = frozenset([1,2,3,4,5])
print(fs)

s20= {1,32,3,45,5}
fs2 = frozenset(s20)
print(fs2)
