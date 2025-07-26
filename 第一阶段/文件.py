
file = open("/Users/johnx/Desktop/新建文本文档_副本.txt", "r", encoding="utf-8")

for line in file.readlines():
    line = line.strip()  # 去除空格及换行符
    print(line)

file.close()



with open("/Users/johnx/Desktop/新建文本文档_副本.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()
        print(line)


