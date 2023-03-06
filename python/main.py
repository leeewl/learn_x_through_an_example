from lib.car import Car

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
    my_car_1.get_base_info()
    # 数字很大何以用下划线分隔，只是为了阅读清晰，内部使用跟没有下划线一样
    # 下面是浮点数
    my_car_1.update_mileage(1_444_111.01)
    my_car_1.get_mileage()


def show_list_slice_tuple_dict_set():
    """
    展示列表，切片，元祖，字典，集合的函数
    列表方括号，可修改
    切片方括号，可修改
    元祖圆括号， 不可修改
    字典花括号，可修改
    """
    friend_list = ['anny', 'david', 'bob', 'lucy', 'tony']

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
    就是键值对
    值可以是数，字符串，列表，字典
    """








if __name__ == '__main__':
    show_class()
    show_list_slice_tuple_dict_set()
