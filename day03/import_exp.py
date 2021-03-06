import os

# I/O  i input   O output

# os 常用方法演示
def os_demo():
    # 获取当前目录的路径
    getcwd = os.getcwd()
    print(getcwd)

    # 获取上级目录的路径
    abspath = os.path.abspath('..')
    print(abspath)

    # 获取上上级目录的路径
    abspath1 = os.path.abspath('../..')
    print(abspath1)

# open 方法演示
def open_demo():
    # 相对路径 ../test.text
    # 绝对路径 C:\Users\YSL\PycharmProjects\myedu\test.text
    # w+ 代表读写模式,写入时会覆盖 原文档内容
    a = open('test.text', 'w+')
    a.write("我呵呵呵呵呵呵")
    print(a)
    print(type(a))

# open 方法演示
def open_demo1():
    # 相对路径 ../test.text
    # 绝对路径 C:\Users\YSL\PycharmProjects\myedu\test.text
    # a+ 代表读写模式,写入时不会覆盖 原文档内容,相当于追加内容
    text_io = open('../test.text', 'a+')
    text_io.write("\n我呵呵呵呵呵呵")

# open 方法演示
def open_demo2():
    # 相对路径 ../test.text
    # 绝对路径 C:\Users\YSL\PycharmProjects\myedu\test.text
    # r 代表只读模式 ,不可写入
    text_io = open('../test.text', 'r')
    # 读取第一行
    readline = text_io.readline()
    # print(readline)
    # 读取所有行 返回一个list对象
    readlines = text_io.readlines()
    print(readlines)
    print(type(readlines))
    print(readlines[2])

if __name__ == '__main__':
    # 相对路径 ../test.text
    # 绝对路径 C:\Users\YSL\PycharmProjects\myedu\test.text
    # open_demo2()
    # print('hello \n world')
    # os_demo()
    open_demo2()
    pass
