class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


parent = ItemDiscount('parent_name', 1000)
child = ItemDiscountReport('child_name', 100)

parent.name = 'new_parent_name'
parent.price = 500

print(f'name: {parent.name} price: {parent.price}')

child.name = 'new_child_name'
child.price = 200
child.get_parent_data()
