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


class division:
    pass


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


class divition:
    def __init__(self, divition_name, divition_id):
        self.divition_name = divition_name
        self.divition_id = divition_id


# หลักการค้นหา ดูจาก Noun ในโจทย์ หรือ หาสิ่งที่เป็น คน สั่ตว์ สิ่งของ ที่จับต้องได้

dell_00001 = Computer("black", "dell", "380", {
                      "cpu": "core 2 duo", "ram": 16}, 5000)
dell_00002 = Computer("black", "dell", "390", {
                      "cpu": "core 2 duo", "ram": 8}, 3000)
dell_00003 = Computer("black", "dell", "2020", {
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

BenTen = Employee("6406041", "Ben Tennison", 30)
Gwen = Employee("6406042", "Gwen Tennison", 31)

benjamin = EmployeeService("6406044", "benjamin mondy", 20, True)
benjamon = EmployeeService("6406043", "menjamon mendy", 22, True)

divition01 = divition("markting", "1001")
divition02 = divition("research and development", "2002")


print(dell_00001.spec)
dell_00001.color = "white"

print(notebook01.spec)
notebook01.price = 5000

print(printer02.spec)
printer02.price = 6000

print(monitor02.spec)
monitor02.serie = "2000"

print(BenTen.name)
BenTen.id = "6406050"

print(benjamon.name)
benjamon.is_free = False

print(divition01.divition_name)
divition01.divition_id = "1002"
