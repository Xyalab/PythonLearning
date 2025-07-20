
def len_str(s):
    count = 0
    for c in s:
        count += 1
    return count

stra = "4387wq7e3r348u3urf34wr"
strb = "ftetferferf"


a = len_str(stra)
print(a)
b = len_str(strb)
print(b)



def add(a, b):
    return a + b

print(add(10, 100))



def change_str():
    global stra
    stra = "fdfdfdfd"

print(stra)
change_str()
print(stra)
