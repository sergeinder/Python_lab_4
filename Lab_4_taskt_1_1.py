from Foreign_product import ForeignProduct
from Broken_product import BrokenProduct
from NeededFunction import *

list_of_broken_product = []
list_of_foreign_product = []

while True:
    text_of_menu()
    number_of_function = input_number_of_function()
    if number_of_function == 1:
        list_of_foreign_product.append(add_foreign_product())
    elif number_of_function == 2:
        list_of_broken_product.append(add_broken_product())
    elif number_of_function == 3:
        show_info(list_of_broken_product, list_of_foreign_product)
    elif number_of_function == 4:
        import_data(list_of_broken_product, list_of_foreign_product)
    elif number_of_function == 5:
        export_data(list_of_broken_product, list_of_foreign_product)
    elif number_of_function == 6:
        break
