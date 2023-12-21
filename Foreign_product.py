from Product import Product


class ForeignProduct(Product):

    # Constructor
    def __init__(self, name: str = "No name", price: float = 0.01, size: float = 0.01,
                 country_name: str = "No country name", transit_tax: float = 0):
        Product.__init__(self, name=name, price=price, size=size)
        self.__country_name = country_name
        self.__transit_tax = transit_tax

    # Getters
    @property
    def country_name(self) -> str:
        return self.__country_name

    @property
    def transit_tax(self) -> float:
        return self.__transit_tax

    # Setters
    @country_name.setter
    def country_name(self, country_name: str):
        self.__country_name = country_name

    @transit_tax.setter
    def transit_tax(self, transit_tax: float):
        self.__transit_tax = transit_tax

    # For print()
    def __str__(self) -> str:
        return f'Products name: {self.name}\n ' \
               f'price: {self.price}\n ' \
               f'size: {self.size}\n ' \
               f'country name: {self.__country_name}\n' \
               f'transit tax: {self.__transit_tax}'

    # Rebuild function sale for this class
    def sale(self, sale: float) -> float:
        if self.price - (self.price * (sale / 100) + self.__transit_tax) < 0.01:
            return 0.01
        else:
            return self.price - (self.price * (sale / 100) + self.__transit_tax)
