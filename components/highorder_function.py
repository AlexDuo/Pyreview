# 一个函数如果可以接受另一个函数作为参数传入，这个函数就叫做高阶函数


# abs 是绝对值
def add(a,b,f):
    return f(a)+f(b)
print(add(3,-6,abs))