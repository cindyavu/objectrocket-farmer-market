class Promotion(object):
    def __init__(self):
        self.promo=dict()
        self.promoItem=dict()
        self.populatePromo()
        

        
    def populatePromoItem(self):
        f=open("Product_List.txt", "r")
        f1=f.readlines()
        for x in f1:
            x=x.strip().split(" ")
            self.promoItem[x[0]]=[]


    def populatePromo(self):
        f=open("Promos.txt", "r")
        f1=f.readlines()
        for x in f1:
            x = x.rstrip().split(" ")
            self.promo[x[0]]=float(x[1])
    
    def getDiscount(self, cart):
        self.populatePromoItem()
        discount=0
        discount+=self.BOGO(cart) + self.APPL(cart) + self.CHMK(cart) + self.APOM(cart)
        return discount
    
    def getPromoItem(self):
        return self.promoItem

    def getPromo(self):
        return self.promo

    def APOM(self, cart):
        amount=0
        discount=0
        if "AP1" in cart  and "OM1" in cart:
            discount = self.promo["APOM"]
            amount=1
        for i in range(amount): 
            self.promoItem["AP1"].append(("APOM"))
        return discount

    def BOGO(self, cart):
        discount=0
        amount=0  
        if "CF1" in cart:
            amount=cart["CF1"]//2
            discount=(amount)*self.promo["BOGO"]
        for i in range(amount):
            self.promoItem["CF1"].append(("BOGO"))
        return discount

    def APPL(self,cart):
        discount=0
        amount=0  
        if "AP1" in cart:
            if "OM1" in cart:
                amount=(cart["AP1"]-1)//3
            else:
                amount=cart["AP1"]//3
            discount=(amount*3*self.promo["APPL"])
        for i in range(amount*3):          
            self.promoItem["AP1"].append(("APPL"))

        return discount

    def CHMK(self, cart):
        discount=0
        amount=0      
        if "CH1" in cart and "MK1" in cart:
            discount = self.promo["CHMK"]
            amount=1
        for i in range(amount):
            self.promoItem["MK1"].append(("CHMK"))
        return discount

    