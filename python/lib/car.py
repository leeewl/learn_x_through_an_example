# 类要大写字母开头
class Car:
    # 规范 分隔函数参数的逗号，前面没空格，后面有空格
    # 初始化函数
    def __init__(self, year):
        self.year = year

    def get_base_info(self):
        print(f"Produced in {self.year}")

class ElectricCar(Car):
    def __init__(self, year):
        super().__init__(year)


