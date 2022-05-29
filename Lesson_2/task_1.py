class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


parent = ItemDiscount('parent_name', 1000)
child = ItemDiscountReport('child_name', 100)


print(f'name: {parent.name} price: {parent.price}')
child.get_parent_data()


