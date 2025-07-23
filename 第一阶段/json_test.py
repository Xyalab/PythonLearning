
import json

dict1 = {"a": 1, "b": 2, "c": 3, "姓名":"张三", "性别":"男"}
list1 = [{"姓名":"张三", "性别":"男"}, {"a": 1, "b": 2, "c": 3}, {1:"ONE", 2:"TWO", 3:"THREE"}]

# python格式数据转换成json字符串
print(json.dumps(dict1, ensure_ascii=False))   # ensure_ascii 是否使用ascii码转换
print(json.dumps(list1, ensure_ascii=False))


dict1_str = '{"a":"1", "b":"2", "c":3}'
print(json.loads(dict1_str), type(json.loads(dict1_str)))











