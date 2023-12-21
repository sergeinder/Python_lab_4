from Foreign_product import ForeignProduct
from Broken_product import BrokenProduct


class MyException(Exception):
    pass


def input_name(massage: str = "") -> str:
    while True:
        try:
            my_name = input(massage)
            if my_name == "":
                raise ValueError
            return my_name
        except ValueError:
            print("You entered empty name: ")


def input_float(massage: str = "") -> float:
    while True:
        try:
            float_value = float(input(massage))
            if float_value < 0.01:
                raise ValueError
            return float_value
        except ValueError:
            print("You entered incorrect data")


def input_number_of_function() -> int:
    while True:
        try:
            number_of_function = int(input())
            if number_of_function < 1 or number_of_function > 6:
                raise ValueError
            return number_of_function
        except ValueError:
            print("You entered incorrect data")


def text_of_menu():
    print("_______________________________")
    print("1 - Add foreign product")
    print("2 - Add broken product")
    print("3 - Show info about products")
    print("4 - Import data from database")
    print("5 - Export data to database")
    print("6 - Exit program")
    print("_______________________________")


def add_broken_product() -> BrokenProduct:
    result = BrokenProduct(name=input_name("Enter name: "), size=input_float("Enter size: "),
                           price=input_float("Enter price: "),
                           fault_description=input_name("Enter fault description: "))
    return result


def add_foreign_product() -> ForeignProduct:
    result = ForeignProduct(name=input_name("Enter name: "), size=input_float("Enter size: "),
                            price=input_float("Enter price: "),
                            country_name=input_name("Enter country name: "),
                            transit_tax=input_float("Enter transit tax: "))
    return result


def show_info(list_of_broken_product, list_of_foreign_product):
    try:
        if len(list_of_broken_product) == 0:
            raise MyException("We don't have broken product")
        else:
            print("Broken products:\n")
            for product in list_of_broken_product:
                print(product)
    except MyException:
        print("Error: We don't have broken product")

    try:
        if len(list_of_foreign_product) == 0:
            raise MyException("We don't have foreign product")
        else:
            print("Foreign products:\n")
            for product in list_of_foreign_product:
                print(product)
    except MyException:
        print("Error: We don't have foreign product")


def import_data(list_of_broken_product, list_of_foreign_product):
    try:
        file = open("database.bin", "rb")
        tmp = str(file.read())
        tmp = tmp[2:-1].split(";")
        n = 0
        for i in range(0, int(tmp[0])):
            list_of_broken_product.append(BrokenProduct(name=tmp[i * 4 + 1], price=float(tmp[i * 4 + 2]),
                                                        size=float(tmp[i * 4 + 3]), fault_description=tmp[i * 4 + 4]))
            n = i * 4 + 4
        for j in range(0, int(tmp[n + 1])):
            list_of_foreign_product.append(ForeignProduct(name=tmp[n + 2], price=float(tmp[n + 3]),
                                                          size=float(tmp[n + 4]), country_name=tmp[n + 5],
                                                          transit_tax=float(tmp[n + 6])))
            n += 5
        file.close()
    except FileNotFoundError:
        print("File is not exist")


def export_data(list_of_broken_product, list_of_foreign_product):
    file = open("database.bin", "wb")
    result = str(len(list_of_broken_product)) + ";"

    for product in list_of_broken_product:
        result += product.name + ";"
        result += str(product.price) + ";"
        result += str(product.size) + ";"
        result += product.fault_description + ";"

    result += str(len(list_of_foreign_product)) + ";"

    for product in list_of_foreign_product:
        result += product.name + ";"
        result += str(product.price) + ";"
        result += str(product.size) + ";"
        result += product.country_name + ";"
        result += str(product.transit_tax) + ";"

    file.write(bytearray(result, encoding='utf8'))
    file.close()
