class Product:

    # Constructor
    def __init__(self, name: str = "No name", price: float = 0.01, size: float = 0.01):
        self.__name = name
        self.__price = price
        self.__size = size

    # Getters
    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def size(self) -> float:
        return self.__size

    # Setters
    @name.setter
    def name(self, name: str):
        self.__name = name

    @price.setter
    def price(self, price: float):
        self.__price = price

    @size.setter
    def size(self, size: float):
        self.__size = size

    def __str__(self) -> str:
        return f'Products name: {self.__name}\n ' \
               f'price: {self.__price}\n ' \
               f'size: {self.__size}\n'

    def sale(self, sale: float) -> float:
        if self.__price - self.__price * (sale / 100) < 0.01:
            return 0.01
        else:
            return self.__price - self.__price * (sale / 100)

    def box(self, width: float, length: float, deep: float) -> int:
        box_size = width * length * deep
        return int(box_size / self.__size)

    # Operator +
    def __add__(self, other):
        return Product(name=self.__name,
                       price=self.__price,
                       size=self.__size + other.__size) if self.__name == other.__name \
            else Product(name=self.__name + " and " + other.__name,
                         size=self.__size + other.__size,
                         price=self.__price + other.__price)
