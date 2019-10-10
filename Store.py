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
        return self.inventory[item].getName()


    def populateInventory(self):
        f=open("Product_List.txt", "r")
        f1=f.readlines()
        for x in f1:
            x=x.strip().split(" ")
            p=Product(x[0],x[1],float(x[2]))
            self.inventory[x[0]]=p
      

    def addtoCart(self, item): 
        self.cartTotal+=self.inventory[item].getPrice()
        self.cart[item]=self.cart.get(item,0)+1


    def printReceipt(self):
        discount=self.p.getDiscount(self.cart)
        total=self.cartTotal-discount
        total=round(total,2)
        self.display(total)


    def display(self,total):
        tab1="              "
        tab3="      "
        tab4="            "
        line="_______________________"
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
                charge="{}".format(item)+tab1+"${:,.2f}\n".format(self.inventory[item].getPrice())
                discount=""
                if j<len(promoItem[item]):
                    discount=tab3+"{}".format(promo_list[i])+tab3+"$-{:,.2f}\n".format(promo[promo_list[i]])
                receipt+=charge+discount
                j+=1

        endline=line+"\n"
        total="Total"+tab4+"${:,.2f}".format(total)
        receipt+=endline+total
        print(receipt)


                









            



        


        







        
