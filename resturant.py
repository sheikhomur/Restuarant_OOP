class Restuarant:
    def __init__(self,name,address,rent):
        self.name = name
        self.address = address
        self.rent = rent 
        self.expense = 0
        self.revenue = 0
        # self.profit = 0
        self.chef = []
        self.manager = []
        self.balance = 0
        self.server = []
        self.expense_description = {}


    def add_employee(self,employee,designation):
        if designation == 'chef':
            self.chef.append(employee)

        elif designation == 'server':
            self.server.append(employee)

        elif designation == 'manager':
            self.manager.append(employee)



    def pay_expense(self,amount,expenditure_sector):
        if self.balance < amount:
            print("Not Enough Money In Balance")

        else:
            self.balance -= amount
            self.expense += amount
            self.expense_description[expenditure_sector]=amount




    def pay_salary(self,employee):
        if self.balance < employee.salary:
            print("Not Enough Money For Pay Salary")

        else:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.salary_due = 0



    def pay_bill(self,customer,order):
        if customer.wallet >= order.bill:
            customer.wallet -= order.bill
            customer.due = 0
            self.balance += order.bill
            self.revenue += order.bill

        else:
            print("Not enough Money in {customer.name}'s Wallet")



    def show_employee(self):
        print('Manager:')
        for manager in self.manager:
            print(f"Name:{manager.name},Salary:{manager.salary}")


        print('Chefs:')
        for chef in self.chef:
            print(f"Name:{chef.name},Salary:{chef.salary}")


        print('Servers:')
        for server in self.server:
            print(f"Name:{server.name},Salary:{server.salary}")


        