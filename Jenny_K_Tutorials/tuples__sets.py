intgr = (10,)
tuple = --(10)
print(type(intgr))
print(type(tuple))

set1 = {"Gift", "Joy", "Emerald", "Favour", 10, 23, 45} #sets have unordered outputs
set2 = {1, 2, 3, 4, 5, True} #duplicate items are not alowed in set unlike tuples and lists
set1.add(6)
print(set1)
#sets like tuples cannot be changed, except modified as a list with defined or predefined method

#opertors in sets
set1 = {'Chinwe', 'Enweremchi', 'Esther', 'Chimaobi', 'Onyinye'}
set2 = {'Gift', 'Esther', 'Joy', 'Francis', 'Rachael'}
set3 = {"Chidera", "Chidalu"}
print(set1.union(('Unknown', 'Ghost')))
#in set arguments, you can pass any iterable
print(set2.union(set1)) #union operator = "|"
print(set1 | set2 | set3)
print(set1)

set1.update(set2)
print(set1.intersection(set2)) #intersection operator = "&"
set1.intersection_update(set2)
print(set1.difference(set2|set3)) #difference operator = "-"

set1.difference_update(set2)
print(set1)
print(set2)
print(set1.symmetric_difference(set2)) #prints items in either sets but not in both
#operator for symetric_difference = "^"
#symetric_difference takes only one argument,  and it has room for updating its difference
#Other operators: isdisjoint(no element in set1 must be set2). it has not operator
#issubset(every element of set1 is a member if set2 also). its operator is "<="
#The reverse of issubsetv is issuperset. its operator is ">="

Other iterable arguments can be used in these methods too
set1.clear() #clears every element in set1
del set2 # deletes every element including the set as well