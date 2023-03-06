# 类要大写字母开头
class Car:
    # 规范: 分隔函数参数的逗号，前面没空格，后面有空格
    # 初始化函数
    def __init__(self, maker, model, year, mileage = 0):
        self.maker = maker
        self.year = year
        self.model = model
        self.mileage = mileage

    def get_base_info(self):
        # 在字符串中使用变量f"{变量名}"
        # upper()是方法，方法是python可对数据执行的操作
        print(f"info: {self.maker.upper()} {self.model.upper()} {self.year}\n")

    def get_mileage(self):
        print(f"mileage : {self.mileage}\n")

    def update_mileage(self, new_mileage):
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            # 字符串可以用单引号和双引号，单引号内部可以包双引号，双引号内部可以包单引号
            print("can't roll back mileage")

# 驼峰命名法，类名中每个单词首字母都大写，实例名和变量一样，用小写字母和下划线
class ElectricCar(Car):
    def __init__(self, year):
        super().__init__(year)


