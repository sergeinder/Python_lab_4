from Foreign_product import ForeignProduct


class TestClass:

    def test_sale(self):
        product = ForeignProduct("Yes", 1000, 1, "Nigeria")
        result = product.sale(99.999999999)
        assert result == 0.01

    def test_box(self):
        product = ForeignProduct("Yes", 1000, 1, "Nigeria")
        result = product.box(1, 1, 1)
        assert result == 1


obj = TestClass()
obj.test_sale()
obj.test_box()
