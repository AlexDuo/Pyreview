# print([i*2 for i in range(10)])
# #下面的就是生成器
# b= (i+1 for i in range(10000000))
#
#
# for i in b:
#     print(i)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1

userinput = int(input('please input the lenght you want to generate'))

f = fib(userinput)


while True:
    try:
        print(f.__next__())
    except StopIteration as e:
        print('generating stoped',e.value)
        break
