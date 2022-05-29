class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name: {self._name}, price: {self._price}')


parent = ItemDiscount('parent_name', 1000)
child = ItemDiscountReport('child_name', 100)


print(f'name: {parent._name} price: {parent._price}')
child.get_parent_data()
