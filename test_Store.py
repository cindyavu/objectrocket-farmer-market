from Store import Store
from Product import Product
from Promo import Promotion

        

def test_populateInventory():
    store=Store()
    c=Product("CH1", "Chai", float(3.11))
    a=Product("AP1", "Apples", float(6.00))
    cf=Product("CF1", "Coffee", float(11.23))
    m=Product("MK1", "Milk", float(4.75))
    o=Product("OM1", "Oatmeal", float(3.69))
    inventory={
        "CH1": c,
        "AP1": a,
        "CF1": cf,
        "MK1": m,
        "OM1": o
    }
    store.populateInventory()
    assert store.inventory == inventory 

def test_addtoCart():
    store=Store()
    i1="BR1"
    i2="EG1"
    i3="EG1"
    cart={
        "BR1": 1,
        "EG1": 2
    }

    eggs=Product("EG1", "Eggs", float(3.88))
    bread=Product("BR1", "Bread", float(2.00))
    store.inventory={
        "EG1": eggs,
        "BR1": bread
    }
    total= float(9.76)
    store.addtoCart(i1)
    store.addtoCart(i2)
    store.addtoCart(i3)

    assert store.cart == cart 
    assert store.cartTotal == total
    
def test_populatePromoItem():
    promo=Promotion()
    promo.populatePromoItem()
    item={
        "CH1":[],
        "AP1":[],
        "CF1":[],
        "MK1":[],
        "OM1":[],

    }
    assert promo.promoItem==item
    
def test_APOM():
    testDiscount=3
    cart={
        "OM1":3,
        "AP1":2
    }
    promo=Promotion()
    promo.populatePromoItem()
    discount=promo.APOM(cart)
    assert discount==testDiscount

def test_APPL():
    testDiscount=4.50
    cart={
        "AP1":5
    }
    promo=Promotion()
    promo.populatePromoItem()
    discount=promo.APPL(cart)
    assert discount==testDiscount

def test_CHMK():
    testDiscount=4.75
    cart={
        "MK1":5,
        "CH1":5
    }
    promo=Promotion()
    promo.populatePromoItem()
    discount=promo.CHMK(cart)
    assert discount==testDiscount

def test_getName():
    product=Product("CH1", "Chai", float(4.00))
    testName="Chai"
    name=product.getName()
    assert testName==name

def test_getId():
    product=Product("CH1", "Chai", float(4.00))
    testId="CH1"
    id=product.getId()
    assert id==testId



    
