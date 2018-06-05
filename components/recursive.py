# 在函数内部可以调用其他函数
# 如果一个函数在内部调用自己这个函数就叫做递归函数


def calculator(n):
    print(n)
    if int(n/2) >0:
        return calculator(int(n/2))


calculator(1024)