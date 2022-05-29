class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportFirst(ItemDiscount):

    def get_info(self):
        print(f'name: {self.name}')


class ItemDiscountReportSecond(ItemDiscount):

    def get_info(self):
        print(f'price: {self.price}')


child1 = ItemDiscountReportFirst('child1_name', 100)
child2 = ItemDiscountReportSecond('child2_name', 200)

child1.get_info()
child2.get_info()
