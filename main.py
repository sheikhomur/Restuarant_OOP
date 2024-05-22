from user import Users,Customer,Employees,Chef,Server,Manager
from menu import Burger,Pizza,Drinks,Menu
from resturant import Restuarant
from order import Order


def main():

# restuarant creation
    customer1 = Customer("Abul","abul@gmail.com",200000,"Sujapur")
    customer2 = Customer("Jabul","jabul@gmail.com",300000,"Alampur")
    customer3 = Customer("Habul","habul@gmail.com",1500000,"Gopinathput")


    restuarant = Restuarant("Brothers","Sylhet",1200)

    chef1 = Chef("Mumin Baburchi","rustom@gmail.com",1000,"Cooking","Janury 02,2023","Kacchi")
    chef2 = Chef("Hashem Baburchi","hashem@gmail.com",800,"Cooking","Janury 02,2024","Fast_Food")

    server1 = Server("Jibon da","jibon@gmail.com",300,"Cleaning","January 01,2017","Cleaner")
    server2 = Server("Ripon da","ripon@gmail.com",200,"Cleaning","January 01,2019","Cleaner")

    manager = Manager("Mujib","mujib@gmail.com",1200,"Office","Janury 2, 2021")



    restuarant.add_employee(chef1,"chef")
    restuarant.add_employee(chef2,"chef") 

    restuarant.add_employee(server1,"server")
    restuarant.add_employee(server2,"server")

    restuarant.add_employee(manager,"manager")

    print("--------------------Employee------------")
    restuarant.show_employee()















    # menu creation
    customer1 = Customer("Abul","abul@gmail.com",10000,"sujapur")

    menu = Menu()
    burger1 = Burger("Chicken_Burger",600,"Fast_Food","Chicken","Large")
    menu.add_menu_item(burger1,"burger")
    burger2=Burger("Beaf_Burger",700,"Fast_Food","Beaf","Lagre")
    menu.add_menu_item(burger2,"burger")


    pizza1 = Pizza("Mexican_Pizza",1200,"Fast_Food","Medium","Chicken")
    menu.add_menu_item(pizza1,"pizza")
    pizza2 = Pizza("Italian_Pizza",1500,"Fast_Food","Medium","Beaf")
    menu.add_menu_item(pizza2,"pizza")


    drinks1 = Drinks("Lemon_Mint",150,"Drinks","500ml","NO")
    menu.add_menu_item(drinks1,"drinks")
    drinks2 = Drinks("Papaya_Milk_Shake",250,"Drinks","500ml","NO")
    menu.add_menu_item(drinks2,"drinks")


    menu.show_menu()


    print(restuarant.revenue,restuarant.balance)
    order1=Order(customer1,[burger1,pizza1,drinks1])
    restuarant.pay_bill(customer1,order1)
    print("after customer1",restuarant.revenue,restuarant.balance)
    order2=Order(customer2,[burger2,drinks2,pizza2])
    restuarant.pay_bill(customer2,order2)
    print("after customer2",restuarant.revenue,restuarant.balance)
    order3=Order(customer3,[burger1,pizza2,drinks2])
    restuarant.pay_bill(customer3,order3)
    print("after customer3",restuarant.revenue,restuarant.balance)

    restuarant.pay_salary(chef1)
    print("after pay salary",restuarant.revenue,restuarant.balance)
    restuarant.pay_expense(1500,"rent")
    print("after pay rent",restuarant.revenue,restuarant.balance)

if __name__ == "__main__":
    main()