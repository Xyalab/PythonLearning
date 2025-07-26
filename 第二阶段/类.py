
# 学生类
class Student:

    # 存在构造方法可以不再单独定义变量
    # name = None
    # age = None
    # gender = None

    # 私有变量，不能被外部直接访问
    __addr = None
    # __phone = None



    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.__phone = phone
        print('构造方法执行')


    def __str__(self):
        return f"name={self.name}, age={self.age}, gender={self.gender}, phone={self.__phone}"

    # 比较最小/大
    def __lt__(self, other):
        return self.age < other.age
    # 比较小于等于/大于等于
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age and self.gender == other.gender and self.name == other.name


    def get_name(self):
        return self.name

    def say_hi(self, msg):
        print(f"hello，I'm {self.name}，{msg}")

    def __get_stu_info(self):
        self.__addr = "河南"
        return f"{self.name}家在{self.__addr}"


    def print_info(self):
        print(self.__get_stu_info()+f"{self.age}岁了")



stu = Student("张三",23, "男", "123654789")
stu1 = Student("张三",23, "男", "123654789")
stu2 = Student("李四",30, "男", "123654789")

# stu.name = "张三"
# stu.age = 23
# stu.gender = "男"

print(stu > stu2)
print(stu >= stu2)


print(stu==stu1)   # 如果不实现__eq__方法比较的是内存地址

stu.print_info()

stu.say_hi("拜拜！！！")


print(stu)
print(str(stu))


print(stu.get_name())


print(stu.name)
print(stu.age)
print(stu.gender)












