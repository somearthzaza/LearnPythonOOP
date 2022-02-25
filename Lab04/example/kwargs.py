

class Contact:

    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self._name = name
        self._email = email

class AddressHolder:

    def __init__(self, street='', city='', state='', **kwargs):
        super().__init__(**kwargs)
        self._street = street
        self._city = city
        self._state = state
        
class Friend(Contact, AddressHolder):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
neo = Friend(email="email@gmail", name="neo", street="rmaintra", city="bangkok", state="th")
print(neo.__dict__)

