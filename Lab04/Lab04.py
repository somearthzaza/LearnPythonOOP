
class Property:
    last_property_id = 1

    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms='', **kwargs):
        super().__init__(**kwargs)
        self._square_feet = square_feet
        self._num_bedrooms = num_bedrooms
        self._num_bathrooms = num_bathrooms
        self._property_id = Property.last_property_id
        Property.last_property_id += 1

    @property
    def property_id(self):
        return self._property_id

    def display(self):
        print(f"property id: {self._property_id}")
        print(f"square feet(ft^2): {self._square_feet}")
        print(f"number of bedrooms: {self._num_bedrooms}")
        print(f"number of bathrooms: {self._num_bathrooms}")

    @staticmethod
    def prompt_init():

        while True:
            try:
                square_feet = float(input("Enter square feet(ft^2): "))
                num_bedrooms = int(input("Enter number of bedroom: "))
                num_bathrooms = int(input("Enter number of bathroom: "))
                break
            except (TypeError, ValueError):
                print("square feet is float and numer of bedroom is int! ")

        return {"square_feet": square_feet, "num_bedrooms": num_bedrooms, "num_bathrooms": num_bathrooms}


class House(Property):

    def __init__(self, garage='', fenced_yard='', **kwargs):
        super().__init__(**kwargs)
        self._garage = garage
        self._fenced_yard = fenced_yard

    def display(self):
        super().display()
        print(f"number of garage: {self._garage}")
        print(f"have fenced yard: {self._fenced_yard}")

    @staticmethod
    def prompt_init():

        input_property_dict = Property.prompt_init()

        while True:
            try:
                garage = int(input("Enter number of garage: "))
                is_have_fenced_yard = input("Does have fenced yard (Y/n): ")
                fenced_yard = True if is_have_fenced_yard.lower(
                ) == "y" or is_have_fenced_yard.lower() == "yes" else False
                break
            except (TypeError, ValueError):
                print('garage is int')

        input_property_dict.update(
            {
                "garage": garage,
                "fenced_yard": fenced_yard
            }
        )
        return input_property_dict


class Apartment(Property):

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self._balcony = balcony
        self._laundry = laundry

    def display(self):
        super().display()
        print(f"have balcony: {self._balcony}")
        print(f"have laundry: {self._laundry}")

    @staticmethod
    def prompt_init():
        input_property_dict = Property.prompt_init()

        is_have_balcony = input("Does have balcony(Y/n): ")
        is_have_laundry = input("Does have laundry(Y/n): ")
        balcony = True if is_have_balcony.lower(
        ) == "y" or is_have_balcony.lower() == "yes" else False
        laundry = True if is_have_laundry.lower(
        ) == "y" or is_have_laundry.lower() == "yes" else False

        input_property_dict.update(
            {
                "balcony": balcony,
                "laundry": laundry
            }
        )
        return input_property_dict


class Purchase:

    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self._price = price
        self._taxes = taxes

    def display(self):
        print(f"price: {self._price}")
        print(f"taxes %: {self._taxes}%")

    @staticmethod
    def prompt_init():

        while True:
            try:
                price = float(input("Enter price: "))
                taxes = int(input("Enter taxes(%): "))
                break
            except (TypeError, ValueError):
                print("price is int or float and taxes is int")

        return {"price": price, "taxes": taxes}


class Rental:

    def __init__(self, furnished='', rent='', **kwargs):
        super().__init__(**kwargs)
        self._furnished = furnished
        self._rent = rent

    def display(self):
        print(f"have furnished: {self._furnished}")
        print(f"rent price: {self._rent}")

    @staticmethod
    def prompt_init():

        while True:
            try:
                is_have_furnished = input("Does have furnished(Y/n): ")
                rent = float(input("Enter rent price: "))

                furnished = True if is_have_furnished.lower(
                ) == "y" or is_have_furnished.lower() == "yes" else False
                break
            except (TypeError, ValueError):
                print("rent is int or float!")

        return {"furnished": furnished, "rent": rent}


class HouseRental(House, Rental):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        House.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        house_rental_input = House.prompt_init()
        house_rental_input.update(Rental.prompt_init())
        return house_rental_input


class HousePurchase(House, Purchase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        House.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        house_purchase_input = House.prompt_init()
        house_purchase_input.update(Purchase.prompt_init())
        return house_purchase_input


class ApartmentRental(Apartment, Rental):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        Apartment.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        apartment_rental_input = Apartment.prompt_init()
        apartment_rental_input.update(Rental.prompt_init())
        return apartment_rental_input


class ApartmentPurchase(Apartment, Purchase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        Apartment.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        apartment_purchase_input = Apartment.prompt_init()
        apartment_purchase_input.update(Purchase.prompt_init())
        return apartment_purchase_input


class Agent:

    def __init__(self):
        self._property_list = []

    def list_properties(self, show_all=False):
        if show_all == True:
            for property in self._property_list:
                print("="*20)
                property.display()
                print("="*20)
        else:
            while True:
                try:
                    search_property_id = int(
                        input("Please specify property id: "))
                    break
                except (ValueError, TypeError):
                    print("property id is int only!")

            for property in self._property_list:
                if property.property_id == search_property_id:
                    print("="*20)
                    property.display()
                    print("="*20)
                    return
            print("Not found!")

    def add_property(self, property_type, purchase_type):
        property_map = {
            ("House", "Rental"): HouseRental,
            ("House", "Purchase"): HousePurchase,
            ("Apartment", "Rental"): ApartmentRental,
            ("Apartment", "Purchase"): ApartmentPurchase
        }

        property_class = property_map.get((property_type, purchase_type))
        if property_class:            
            property_input = property_class.prompt_init()
            self._property_list.append(property_class(**property_input))
        else:
            print("Please provide correct args!")


# test
smith1 = Agent()
smith1.add_property("House", "Rental")
smith1.add_property("House", "Purchase")
smith1.add_property("Apartment", "Rental")
smith1.add_property("Apartment", "Purchase")
smith1.add_property("", "")
smith1.list_properties(True)
smith1.list_properties()

neo = Agent()
neo.add_property("House", "Rental")
neo.add_property("House", "Purchase")
neo.add_property("Apartment", "Rental")
neo.add_property("Apartment", "Purchase")
neo.list_properties(True)
neo.list_properties()

