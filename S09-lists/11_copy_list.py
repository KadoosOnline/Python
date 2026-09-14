# IMPORTANT TRAP: '=' does not copy a list, it only gives it a second name.
list1 = [1, 2, 3]
list2 = list1

list2.append(4)
print(list1)      # [1, 2, 3, 4]  -> list1 changed too!

# To get a real copy use copy(), list() or a full slice.
list3 = list1.copy()
list3.append(5)
print(list1)      # [1, 2, 3, 4]  -> unchanged
print(list3)      # [1, 2, 3, 4, 5]

list4 = list1[:]     # the same idea with a slice
print(list4)
