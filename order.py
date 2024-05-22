class Order:
    def __init__(self,customer,orders):
        self.bill = 0

        for order in orders:
           self.bill += order.price

        customer.due = self.bill