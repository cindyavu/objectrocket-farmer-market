from Store import Store


import re
class Main(object):
    def __init__(self):
        self.line="__________________________\n"
        self.store=Store()
    
    def start(self):
        option=input("What would you like to do? \n1. Add to cart\n2. Check current cart\n3. Checkout\nEnter 1,2,3\nOption: ")
        print(self.line)
        

        while option!="1" and option!="2" and option!="3":
            option=input("Not a valid option. Please enter 1,2,3\nOption: ")


        while option=="1" or option=="2":

            if option == "1":
                self.option1()
            elif option == "2":
                self.option2()
                
            
            option=input("What would you like to do? \n1. Add to cart\n2. Check current cart\n3. Checkout\nEnter 1,2,3\nOption: ")
            print(self.line)

            while option!="1" and option!="2" and option!="3":
                option=input("Not a valid option. Please enter 1,2,3\nOption: ")

        if option=="3":
            self.option3()        
    #User wants to add to cart
    def option1(self):
        item=input("What item would you like to add? \nItem: ").upper()
        print(self.line)
        while item not in self.store.inventory:
            item=input("That item does not exist! Please enter a valid item.\nItem: ").upper()
            print(self.line)

        self.store.addtoCart(item)
        print("{} added to cart!".format(self.store.getName(item)))
        print(self.line)

    #User wants to check current cart status    
    def option2(self):
        print("Here is your current cart:\n")
        self.store.printReceipt()
        print(self.line)
    #User wants to check out cart
    def option3(self):
        print("Checkout: \n")
        self.store.printReceipt()

        print("\nHave a nice day!") 


m=Main()
m.start()
