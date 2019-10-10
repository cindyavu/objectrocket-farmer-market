class Promotion(object):
    def __init__(self):
        self.promo=dict()
        self.promoItem=dict()
        self.populatePromo()

    #maps product to empty array, promoItem contains mapping of product to discount  
    def populatePromoItem(self):
        f=open("Product_List.txt", "r")
        f1=f.readlines()
        for x in f1:
            x=x.strip().split(" ")
            self.promoItem[x[0]]=[]

    #Populates promo name to discount amount
    def populatePromo(self):
        f=open("Promos.txt", "r")
        f1=f.readlines()
        for x in f1:
            x = x.rstrip().split(" ")
            self.promo[x[0]]=float(x[1])

    #runs discount on cart
    def getDiscount(self, cart):
        self.populatePromoItem()
        discount=0
        discount+=self.BOGO(cart) + self.APPL(cart) + self.CHMK(cart) + self.APOM(cart)
        return discount

    #returns promoItem object
    def getPromoItem(self):
        return self.promoItem

    #returns promo object
    def getPromo(self):
        return self.promo
        
    #checks for APOM discount
    def APOM(self, cart):
        amount=0
        discount=0
        if "AP1" in cart  and "OM1" in cart:
            discount = self.promo["APOM"]
            amount=1
        for _ in range(amount): 
            self.promoItem["AP1"].append(("APOM"))
        return discount

    #checks for BOGO discount
    def BOGO(self, cart):
        discount=0
        amount=0  
        if "CF1" in cart:
            amount=cart["CF1"]//2
            discount=(amount)*self.promo["BOGO"]
        for _ in range(amount):
            self.promoItem["CF1"].append(("BOGO"))
        return discount

    #checks for APPL discount
    def APPL(self,cart):
        discount=0
        amount=0  
        if "AP1" in cart:
            if "OM1" in cart:
                amount=(cart["AP1"]-1)//3
            else:
                amount=cart["AP1"]//3
            discount=(amount*3*self.promo["APPL"])
        for _ in range(amount*3):          
            self.promoItem["AP1"].append(("APPL"))

        return discount

    #checks for CHMK discount
    def CHMK(self, cart):
        discount=0
        amount=0      
        if "CH1" in cart and "MK1" in cart:
            discount = self.promo["CHMK"]
            amount=1
        for _ in range(amount):
            self.promoItem["MK1"].append(("CHMK"))
        return discount

    