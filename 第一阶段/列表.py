
list1 = ["sss", 345, True, [1, 2, 4, 6]]
print(list1)

print(list1[2])

print(list1.index(True))


list1[2] = False
print(list1)

list1.append("打老虎")
print(list1)

list1.insert(2, "TRUE")
print(list1)

list1.extend([2, "测试", "一下"])
print(list1)

list1.pop(4)
print(list1)

list1.remove("TRUE")
print(list1)

print(list1.count("打老虎"))
print(len(list1))

list1.clear()
print(list1)
