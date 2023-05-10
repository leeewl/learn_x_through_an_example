from lib.car import Car
import os

# 常量类似于变量，只包含字母，数字，下划线，但是建议字母只用大写字母
# 60万公里强制报废
MAX_MILEAGE = 600_000

# 函数用def开头
def show_class():
    """该函数展示类如何使用"""
    # 上面是文档字符串，描述了函数是用来做什么的，可以生成程序中函数的文档

    # 变量名只能包含字母、数字和下划线
    # 变量以字母或者下划线开头
    # 变量不能和python关键字相同
    # 尽量用小写的变量名，相邻单词之间用下划线
    my_car_1 = Car('Audi', "A6", 2010)
    _my_car_2 = Car('audi', 'a4', 2020)
    base_info = my_car_1.get_base_info()
    print(f"Car info : {base_info}")
    # 直接修改car的属性
    my_car_1.mileage = 10
    my_car_1.get_mileage()
    # 通过方法修改car的属性
    # 数字很大可以用下划线分隔，只是为了阅读清晰，内部使用跟没有下划线一样
    # 下面是浮点数
    my_car_1.update_mileage(1_444_111.01)
    mileage = my_car_1.get_mileage()
    print(f"mileage : {mileage}\n")
    # 通过方法递增car的属性
    my_car_1.increment_mileage(10)
    mileage = my_car_1.get_mileage()
    print(f"mileage : {mileage}\n")

def show_list_slice_tuple_dict_set():
    """
    展示列表，切片，元祖，字典，集合的函数
    列表方括号，可修改
    切片方括号，可修改
    元祖圆括号， 不可修改
    字典花括号，可修改
    """
    friend_list = ['anny', 'david', 'bob', 'lucy', 'tony']

    file_name = "friend_list.txt"

    # 可能引发错误的代码放在try..except里，try代码成功执行时才需要执行的代码放在else里。
    # r是读取模式，如果不存在文件，报错
    try:
        # with在不再需要访问文件时将其关闭
        with open(file_name, 'r') as fl:
            contents = fl.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        print(contents)

    # w是写入模式，读取时会清空文件
    with open(file_name, 'w') as fl:
        for name in friend_list:
            fl.write(name + "\n")

    # a是附加模式，不会清空文件内容
    with open(file_name, 'a') as fl:
        fl.write("jack")

    try:
        fl = open(file_name, 'r')
        lines = fl.readlines()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        for line in lines:
            print(line.rstrip())
        # 不使用with，需要手动关闭
        fl.close()

    # 删除文件
    os.remove(file_name)

    """
    列表
    下面按照 查、增、删、改的顺序熟悉列表
    """

    # 列表 查
    # 列表索引从0开始
    print(f"My first friend is {friend_list[0]}")
    # 也可以用负号从最后数起,当列表为空时，访问报错--Traceback
    print(f"My Latest Friend is {friend_list[-1]}")
    for friend in friend_list:
        print(friend)

    # 列表 增
    friend_list.append('ivo')
    friend_list.insert(0, 'joe')

    # 列表 删
    del friend_list[-1]
    no_friend = friend_list.pop()
    print(f"I lost my friend -- {no_friend}")
    no_friend = friend_list.pop(0)
    print(f"I lost my friend -- {no_friend}")
    friend_list.remove('lucy')
    # 列表 改
    friend_list[1] = 'jim'

    # 列表 组织
    # 临时排序
    print(f"Here is the original list: {friend_list}")
    print(f"Here is the sorted list: {sorted(friend_list)}")
    print(f"Here is the reverse sorted list: {sorted(friend_list, reverse=True)}")
    print(f"Here is the original list: {friend_list}")

    # 永久排序
    friend_list.sort()
    print(f"Here is the sorted list: {friend_list}")
    # 永久排序反向
    friend_list.sort(reverse=True)
    print(f"Here is the reverse sorted list: {friend_list}")

    # 颠倒
    friend_list.reverse()
    print(f"Here is the reverse list: {friend_list}")

    """
    切片
    重新复制了一部分列表
    """
    # 左闭右开
    # 左右可都指定
    print("show slice \n")
    print(friend_list[0:3])
    # 左右可指定一个
    print(friend_list[-2:])
    print(friend_list[:2])
    # 左右可都不指定，相当于复制了列表
    friend_list_backup = friend_list[:]
    print(friend_list_backup)

    """
    元祖
    """
    # 其实圆括号不是必需的，逗号必须有
    # 变量可修改，元祖不可修改
    tuple_1 = (1, 2, 3)
    tuple_1 = 1, 2
    tuple_1 = (1,)

    """
    字典
    花括号
    就是键值对
    任何python对象都可以当字典的值，比如数，字符串，列表，字典
    """
    student_score = {
        'anny': {'English': 60, 'Math': 90},
        'bob': {'English': 70, 'Math': 80}
    }

    # 字典 查
    # 有两种方式,[]和get()
    # []的方式，找不到会Trackback
    print(student_score['anny'])
    # get()方式可以指定默认值
    print(student_score.get('somebody', 'no student'))
    # get()没有默认值，错误时返回None
    print(student_score.get('someguy'))
    # 遍历键值对
    for key, value in student_score.items():
        print(f"\nKey: {key}")
        print(f"Value: {value}")

    # 遍历键值
    print("\n")
    for key in student_score.keys():
        print(key.title())
    # .key()创建了一个列表,因为是列表，所以可以用上面排序的方法
    if 'tom' not in student_score.keys():
        print("no")
    else:
        print("yes")

    # 遍历值,如果是字符串，数字，可以用set()去重
    print("\n")
    for value in student_score.values():
        print(value)

    # 字典 增
    student_score['jerry'] = {'English': 84}
    print(student_score)

    # 字典 删
    del student_score['jerry']
    print(student_score)

    # 字典 改
    student_score['anny']['English'] = 100
    print(student_score)

    # 集合
    # 集合用花括号,逗号分隔
    # 集合中每个元素是独一无二的，下面两个python只会保留一个
    languages = {'python', 'ruby', 'python', 'c'}
    print(languages)

def run_func(id = "1"):
    """
    函数举例
    一个带默认值的函数
    """
    if id == "1":
        show_class()
    elif id == "2":
        show_list_slice_tuple_dict_set()
    else:
        print("error input\n")


if __name__ == '__main__':
    # 让用户输入
    prompt = "\n what you want ? please input the number:"
    prompt += "\nEnter 'quit' to end the program"
    prompt += "\n1. show class"
    prompt += "\n2. show list slice tuple dict set\n"

    user_input =""
    while user_input != 'quit':
        user_input = input(prompt)
        run_func(user_input)
    else:
        print("bye!\n")
