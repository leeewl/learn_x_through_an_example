# 类要大写字母开头
class Car:
    # 规范: 分隔函数参数的逗号，前面没空格，后面有空格
    # 初始化函数,__init__()是一个特殊方法，创建Car实例时自动运行，形参self必不可少，而且必须位于其他形参前面。
    def __init__(self, maker, model, year, mileage = 0):
        # self为前缀的变量可供类中所有方法使用，可以通过类的任何实例访问，这样的变量称为属性
        self.maker = maker
        self.year = year
        self.model = model
        self.mileage = mileage

    def get_base_info(self):
        # 在字符串中使用变量f"{变量名}"
        # title()是方法，方法是python可对数据执行的操作
        return f"{self.maker.title()} {self.model.title()} {self.year}"

    def get_mileage(self):
        return self.mileage
        print(f"mileage : {self.mileage}\n")

    def update_mileage(self, new_mileage):
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            # 字符串可以用单引号和双引号，单引号内部可以包双引号，双引号内部可以包单引号
            print("can't roll back mileage")

    def increment_mileage(self, miles):
        self.mileage += miles

# 驼峰命名法，类名中每个单词首字母都大写，实例名和变量一样，用小写字母和下划线
# 父类需要import进来，或者包含在当前文件中，并且位于子类前面！！！
class ElectricCar(Car):
    """电车类，Car是父类，ElectricCar是子类"""
    def __init__(self, maker, model, year, mileage = 0, battery_size = 100):
        super().__init__(maker, model, year, mileage)
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size} kwh battery"


