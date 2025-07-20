__all__ = ['minus1', 'add1']   # 定义 import * 的范围

def add1(a, b):
    print("a+b=", a+b)
    return a+b

def add2(a, b, c):
    print("a+b+c=", a+b+c)
    return a+b+c

def minus1(a, b):
    print("a+b=", a+b)
    return a+b

if __name__ == "__main__":   # 程序直接执行时才会为True，其他程序导入时则为False，不会执行该代码
    add1(1, 3)