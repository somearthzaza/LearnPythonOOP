class Device:
    pass


class Computer:
    pass


class Notebook:
    pass


class Printer:
    pass


class Monitor:
    pass


class Employee:
    pass


class EmployeeService:
    pass


class Department:
    pass


class Device:

    def __init__(self, color, type):
        self.color = color
        self.type = type


class Computer:

    def __init__(self, color, brand, serie, spec, price):
        self.color = color
        self.brand = brand
        self.serie = serie
        self.spec = spec
        self.price = price


class Notebook:

    def __init__(self, color, brand, serie, spec, price):
        self.color = color
        self.brand = brand
        self.serie = serie
        self.spec = spec
        self.price = price


class Printer:

    def __init__(self, color, brand, serie, spec, price):
        self.color = color
        self.brand = brand
        self.serie = serie
        self.spec = spec
        self.price = price


class Monitor:

    def __init__(self, color, brand, serie, monitor_size, spec):
        self.color = color
        self.brand = brand
        self.serie = serie
        self.monitor_size = monitor_size
        self.spec = spec


class Employee:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class EmployeeService:

    def __init__(self, id, name, age, is_free):
        self.id = id
        self.name = name
        self.age = age
        self.is_free = is_free


class Department:
    def __init__(self, department_id, department_name):
        self.department_id = department_id
        self.department_name = department_name


# หลักการค้นหา ดูจาก Noun ในโจทย์ หรือ หาสิ่งที่เป็น คน สั่ตว์ สิ่งของ ที่จับต้องได้

device01 = Device("green", "desktop")
device02 = Device("yellow", "mobile")

pc01 = Computer("black", "dell", "380", {
    "cpu": "core 2 duo", "ram": 16}, 5000)
pc02 = Computer("black", "dell", "390", {
    "cpu": "core 2 duo", "ram": 8}, 3000)
pc03 = Computer("black", "dell", "2020", {
    "cpu": "i3 2200", "ram": 8}, 3500)

notebook01 = Notebook("black", "acer", "nitro", {
                      "cpu": "i3 2200", "ram": 8}, 3500)
notebook02 = Notebook("black", "acer", "nitro", {
                      "cpu": "i3 2200", "ram": 8}, 3500)

printer01 = Printer("white", "canon", "A380", {
                    "rgb": 360, "connection": "wireless"}, 1000)
printer02 = Printer("green", "canon", "l280", {
                    "rgb": 360, "connection": "wireless"}, 1000)

monitor01 = Monitor("white", "lg", "380", "32 inch", "rgb 128bit")
monitor02 = Monitor("white", "sumsung", "380", "32 inch", "144 hz")

ben_ten = Employee("6406041", "Ben Tennison", 30)
gwen = Employee("6406042", "Gwen Tennison", 31)

benjamin = EmployeeService("6406044", "benjamin mondy", 20, True)
benjamon = EmployeeService("6406043", "menjamon mendy", 22, True)

dep01 = Department("1001", "markting")
dep02 = Department("2002", "research and development")

print(device01.type)
device01.type = "headphone"

print(pc01.spec)
pc01.color = "white"

print(notebook01.spec)
notebook01.price = 5000

print(printer02.spec)
printer02.price = 6000

print(monitor02.spec)
monitor02.serie = "2000"

print(ben_ten.name)
ben_ten.id = "6406050"

print(benjamon.is_free)
benjamon.is_free = False

print(dep01.department_id)
dep01.department_id = "1002"
print(dep01.department_id)
