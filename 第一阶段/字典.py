

dict1 = {"john":"80", "tom":"91", "张三":"66"}
dict2 = dict()
dict3 = {}
print(dict1, type(dict1))

print(dict1.get("john"))
print(dict1["tom"])

for name in dict1.keys():
    print(name, dict1[name])



dict4 = {
    "张三":{
        "语文":"95",
        "数学":"99",
        "英语":"88"
    },
    "李四":{
        "语文":"99",
        "数学":"90",
        "英语":"80"
    },
    "王五":{
        "语文":"98",
        "数学":"97",
        "英语":"98"
    }
}

print(dict4)
for name in dict4.keys():
    print(name+"的成绩是:")
    for scores in dict4[name].keys():
        print(scores, ": ", dict4[name][scores])






