from Store import Store


import re
class Main(object):
    def start(self):

        line="__________________________\n"
        store=Store()
        option=input("What would you like to do? \n1. Add to cart\n2. Check current cart\n3. Checkout\nEnter 1,2,3\nOption: ")
        print(line)
        

        while option!="1" and option!="2" and option!="3":
            option=input("Not a valid option. Please enter 1,2,3\nOption: ")


        while option=="1" or option=="2":

            if option=="1":
                self.option1(store)
            if option=="2":
                self.option2(store)
                
            
            option=input("What would you like to do? \n1. Add to cart\n2. Check current cart\n3. Checkout\nEnter 1,2,3\nOption: ")
            print(line)
            while option!="1" and option!="2" and option!="3":
                option=input("Not a valid option. Please enter 1,2,3\nOption: ")

        if option=="3":
            self.option3(store)        

    def option1(self,store):
        line="__________________________\n"
        item=input("What item would you like to add? \nItem: ").upper()
        print(line)
        while item not in store.inventory:
            item=input("That item does not exist! Please enter a valid item.\nItem: ").upper()
            print(line)

        store.addtoCart(item)
        print("{} added to cart!".format(store.getName(item)))
        print(line)

        
    def option2(self,store):
        line="_______________________________\n"
        print("Here is your current cart:\n")
        store.checkout()
        print(line)

    def option3(self,store):
        print("Checkout: \n")
        store.checkout()

        print("\nHave a nice day!") 


m=Main()
m.start()
