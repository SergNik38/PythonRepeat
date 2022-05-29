class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        result = self.price - self.price * (self.discount / 100)
        return f'Цена со скидкой {result}'

    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


parent = ItemDiscount('parent_name', 1000)
child = ItemDiscountReport('child_name', 100, 10)

print(f'name: {parent.name} price: {parent.price}')
child.get_parent_data()
print(str(child))
