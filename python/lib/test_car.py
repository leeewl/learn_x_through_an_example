import unittest
from car import Car
# as 重新命名
from car import ElectricCar as ECar

class TestCar(unittest.TestCase):
    """针对Car类的测试"""
    # 方法名必须以test_开头
    def test_get_base_info(self):
        my_car = Car("Audi", "a4", 2008)
        base_info = my_car.get_base_info()
        print(base_info)
        """
        断言方法
        assertEqual(a, b)
        assertNotEqual(a, b)
        assertTrue(x)
        assertFalse(x)
        assertIn(item, list)
        assertNotIn(item, list)
        """
        self.assertEqual( "Audi A4 2008", base_info)

class TestECar(unittest.TestCase):
    """针对ElectricCar类的测试"""
    def setUp(self):
        """
        创建一次对象
        """
        self.my_electric_car = ECar("tesla", "model s", 2020, 0, 100)

    def test_get_base_info(self):
        base_info = self.my_electric_car.get_base_info()
        self.assertEqual("Tesla Model S 2020", base_info)

    def test_describe_battery(self):
        battle_describe = self.my_electric_car.describe_battery()
        self.assertEqual("This car has a 100 kwh battery", battle_describe)

    def test_get_mileage(self):
        mileage = self.my_electric_car.get_mileage()
        self.assertEqual(0, mileage)

    def test_update_mileage(self):
        self.my_electric_car.update_mileage(10)
        mileage = self.my_electric_car.get_mileage()
        self.assertEqual(10, mileage)

    def test_increment_mileage(self):
        # 重新创建一个
        my_electric_car_2 = ECar("tesla", "model x", 2022)
        my_electric_car_2.increment_mileage(15)
        mileage = my_electric_car_2.get_mileage()
        self.assertEqual(15, mileage)


if __name__ == '__main__':
    unittest.main()