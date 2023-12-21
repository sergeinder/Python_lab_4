from Product import Product


class BrokenProduct(Product):
    def __init__(self, name: str = "No name", price: float = 0.01, size: float = 0.01,
                 fault_description: str = "No description"):
        super().__init__(name=name, price=price, size=size)
        self.__fault_description = fault_description

    @property
    def fault_description(self) -> str:
        return self.__fault_description

    @fault_description.setter
    def fault_description(self, fault_description: str):
        self.fault_description = fault_description

    def __str__(self) -> str:
        return f'Products name: {self.name}\n ' \
               f'price: {self.price}\n ' \
               f'size: {self.size}\n ' \
               f'fault description: {self.__fault_description}'
