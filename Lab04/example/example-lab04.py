
#! copy at your on risk

class Property:

    def __init__(self, square_feet, num_bedrooms, num_bathrooms):
        self._square_feet = square_feet
        self._num_bedrooms = num_bedrooms
        self._num_bathrooms = num_bathrooms

    def display(self):
        print(self._square_feet)
        print(self._num_bedrooms)
        print(self._num_bathrooms)

    @staticmethod
    def prompt_init():
        return_dict = {}

        square_feet = input("enter square feet: ")
        num_bedrooms = input("Enter num of bedroom: ")
        num_bathrooms = input("enter num bathroom: ")

        return_dict.update({"square_feet": square_feet})
        return_dict.update({"num_bedrooms": num_bedrooms})
        return_dict.update({"num_bathrooms": num_bathrooms})

        return return_dict


class House(Property):

    def __init__(self, square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self._garage = garage
        self._fenced_yard = fenced_yard

    def display(self):
        super().display()
        print(self._garage)
        print(self._fenced_yard)

    @staticmethod
    def prompt_init():
        dict1 = Property.prompt_init()
        garage = input("enter number of garage: ")
        is_have_fenced_yard = input("have fenced yard (Y/n): ")
        fenced_yard = True if is_have_fenced_yard.lower(
        ) == "y" or is_have_fenced_yard.lower() == "yes" else False

        dict1.update({"garage": garage})
        dict1.update({"fenced_yard": fenced_yard})
        return dict1


class Rental:

    def __init__(self, furnished, rent):
        self._furnished = furnished
        self._rent = rent

    def display(self):
        print(self._furnished)
        print(self._rent)

    @staticmethod
    def prompt_init():
        rental_dict = {}
        is_have_furnished = input("have furnished (Y/n): ")
        furnished = True if is_have_furnished.lower(
        ) == "y" or is_have_furnished.lower() == "yes" else False
        rent = input("Enter rent: ")
        rental_dict.update({"furnished": furnished})
        rental_dict.update({"rent": rent})

        return rental_dict


class HouseRental(House, Rental):

    def __init__(self, square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard, furnished, rent):
        House.__init__(self, square_feet, num_bedrooms,
                       num_bathrooms, garage, fenced_yard)
        Rental.__init__(self, furnished, rent)

    def display(self):
        House.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        hr_dict = House.prompt_init()
        hr_dict.update(Rental.prompt_init())
        return hr_dict


class Agent:

    def __init__(self):
        self._property_list = []

    @property
    def property_list(self):
        return self._property_list

    def list_properties(self, show_all=False):
        if show_all:
            for one_property in self.property_list:
                one_property.display()
        else:
            # select which one will display
            self.property_list[0].display()

    def add_property(self, property_type, purchase_type):
        create_prop = HouseRental.prompt_init()
        new_prop = HouseRental(create_prop.get("square_feet"), create_prop.get("num_bedrooms"), create_prop.get(
            "num_bathrooms"), create_prop.get("garage"), create_prop.get("fenced_yard"), create_prop.get("furnished"), create_prop.get("rent"))
        self.property_list.append(new_prop)


neo = Agent()
neo.add_property("house", "rental")
neo.add_property("house", "rental")
neo.list_properties(True)
