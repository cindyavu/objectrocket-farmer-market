from Product import Product 
from Promo import Promotion
import textwrap
import re
class Store(object):
    def __init__(self):
        self.inventory=dict()
        self.cart=dict()
        self.cartTotal=0
        self.p=Promotion()
        self.populateInventory()


    def getName(self, item):
        return self.inventory[item].get_name()


    def populateInventory(self):
        f=open("Product_List.txt", "r")
        f1=f.readlines()
        for x in f1:
            x=x.strip().split(" ")
            p=Product(x[0],x[1],float(x[2]))
            self.inventory[x[0]]=p
      

    def addtoCart(self, item): 
        self.cartTotal+=self.inventory[item].get_price()
        self.cart[item]=self.cart.get(item,0)+1


    def checkout(self):
        discount=self.p.getDiscount(self.cart)
        total=self.cartTotal-discount
        total=round(total,2)
        self.display(total)


    def display(self,total):
        line1="Item             Price\n"
        line2="____             _____\n"
        receipt=line1+line2
        promoItem=self.p.getPromoItem()
        promo=self.p.getPromo()

        for item in self.cart:
            item_count=self.cart[item]
            promo_list=promoItem[item]
            j=0

            for i in range(item_count):
                charge="{}              ${:,.2f}\n".format(item, self.inventory[item].get_price())
                discount=""
                if j<len(promoItem[item]):
                    discount="      {}     $-{:,.2f}\n".format(promo_list[i], promo[promo_list[i]])
                receipt+=charge+discount
                j+=1

        endline="______________________\n"
        total="Total            ${:,.2f}".format(total)
        receipt+=endline+total
        print(receipt)


                









            



        


        







        
