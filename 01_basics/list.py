import copy

l1 = [1,2,3]
l2 = l1    # l1 and l2 refer to the same list
print(l1 == l2) # == operator checks the value if these are equal or not
print(l1 is l2) # is operator checks whether the reference is same or not
print(l1)
print(l2)
l1[0] = 21
print(l1)
print(l2)

# l1, l2, l3, l4 are different objects
l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1[:]
l4 = copy.copy(l1)

print(l1 == l2)
print(l1 is l2)
print(l1)
print(l2)
print(l3)
print(l4)

l1[1] = 100
print(l1)
print(l2)
print(l3)
print(l4)
