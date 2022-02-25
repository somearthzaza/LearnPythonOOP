
is_have_balcony = input("Does have balcony(Y/n): ").lower()
is_have_laundry = input("Does have laundry(Y/n): ").lower()

boolean_balcony = any([is_have_balcony == "yes", is_have_balcony == "y"])
boolean_laundry = any([is_have_laundry == "yes", is_have_laundry == "y"])

print(boolean_balcony, boolean_laundry)