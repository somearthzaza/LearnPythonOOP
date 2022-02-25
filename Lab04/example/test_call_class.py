class HouseRental:

    @staticmethod
    def show():
        print("fuck you")


class HousePurchase:

    @staticmethod
    def show():
        print("hello from hell")


type_map = {
    ("house", "rental"): HouseRental,
    ("house", "purchase"): HousePurchase
}


select_list = ("house", "purchase")
prop_test = type_map.get(select_list)
prop_test.show()
