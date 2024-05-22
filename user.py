class Users:
    def __init__(self,name,email):
        self.name = name
        self.email = email


class Customer(Users):
    def __init__(self, name, email,wallet,address):
        super().__init__(name, email)
        self.wallet = wallet
        self.address = address
        self.due = None



class Employees(Users):
    def __init__(self, name, email,salary,department,start):
        super().__init__(name, email)
        self.salary = salary
        self.department = department
        self.start = start
        self.salary_due = salary



class Chef(Employees):
    def __init__(self, name, email, salary, department,start,cooking):
        super().__init__(name, email, salary, department,start)
        self.cooking = cooking
        
        



class Server(Employees):
    def __init__(self, name, email, salary, department,start,catagory):
        super().__init__(name, email, salary, department,start)
        self.catagory = catagory
        


class Manager(Employees):
    def __init__(self, name, email, salary, department, start):
        super().__init__(name, email, salary, department, start)
    