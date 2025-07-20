


my_set = {"ffdfd", "fsdds", "112233", "334455", "112233"}

print(my_set)

my_set.add("4343443")
print(my_set)

my_set.remove("4343443")
my_set.pop()
my_set.clear()


set1 = {1,2,3,4,5,6,9}
set2 = {1,2,3,6,9,8,7}

set3 = set1.difference(set2)
print(set3)    # {4, 5}

set4 = set1.copy()
set1.difference_update(set2)
print(set1)
set2.difference_update(set4)
print(set2)


set4 = set4.union(set2)
print(set4)


for item in set4:
    print(item)

