

from traceback import print_exception


class Property:
    def __init__(self, square_feet, num_bedrooms, num_bathroom):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathroom = num_bathroom

    def display(self):
        print(
            f"Square feet = {self.square_feet} bedrooms = {self.num_bedrooms} bath = {self.num_bathroom}")

    @staticmethod
    def prompt_init():
        dict = {
            "square_feet": 0,
            "num_bedroom": 0,
            "num_bathroom": 0
        }
        while True:
            dict.update(
                {"square_feet": int(input(f"what square feet do you need?\n"))})
            dict.update(
                {"num_bedroom": int(input(f"what num bedroom do you need?\n"))})
            dict.update(
                {"num_bathroom": int(input(f"what num bathroom do you need?\n"))})

            return dict


class House(Property):
    def __init__(self, square_feet, num_bedrooms, num_bathroom, garage, fenced_yard):
        super().__init__(square_feet, num_bedrooms, num_bathroom)
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        print(
            f"{super().display()} garage = {self.garage} fenced = {self.fenced_yard} ")

    @staticmethod
    def prompt_init():
        test = Property.prompt_init()
        while True:
            try:
                garage = int(input("num of garage?\n"))
                fenced_yard = int(input("num of fenced yard?\n"))
                test["garage"] = garage
                test["fenced_yard"] = fenced_yard
            except:
                print("Error wrong type")
            else:
                return test


class Purchase:
    def __init__(self, price):
        self.price = price

    def display(self):
        print(f"{self.price}")

    @staticmethod
    def prompt_init():
        final_dict = {"price": 0}
        while True:
            try:
                price = int(input("price = "))
                final_dict.update({"price": price})
            except:
                print("error wrong type!!")
            else:
                return final_dict


class HousePurchase(House, Purchase):
    @staticmethod
    def prompt_init():
        final_dict = House.prompt_init()
        final_dict.update(Purchase.prompt_init())
        return final_dict

# b = House.prompt_init()
# myhouse = House(b["square_feet"], b["num_bedroom"],
#                 b["num_bathroom"], b["garage"], b["fenced_yard"])
# myhouse.display()


z = HousePurchase.prompt_init()
house1 = HousePurchase()
print(z)
# print(b)
