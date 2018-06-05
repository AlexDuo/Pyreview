def change_name(name):
    print("before change",name)
    name = 'Alex' #change name 这个函数的作用域
    print('after change',name)


# 局部变量只在函数里生效
name = 'duo'

change_name(name)

# 全局变量就是在整个程序中都生效的变量，在程序的最上层定义
# 列表，字典，集合像这种复杂的数据类型都可以在局部对全局进行修改。

# 当局部变量与全局变量重名的时候，定义局部变量的子程序中局部变量起作用，其他地方全局变量起作用 