# The Farmer's Market
A stand is selling proudcts at a farmer's market and is offering promotions. This program is a checkout system that will add to a cart, apply promotions, and print out the receipt.

These are the products:
```
+--------------|--------------|---------+
| Product Code |     Name     |  Price  |
+--------------|--------------|---------+
|     CH1      |   Chai       |  $3.11  |
|     AP1      |   Apples     |  $6.00  |
|     CF1      |   Coffee     | $11.23  |
|     MK1      |   Milk       |  $4.75  |
|     OM1      |   Oatmeal    |  $3.69  |
+--------------|--------------|---------+
```

These are the promotions:
```
1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples
```


For example if a cart was:
```
OM1, AP1, CF1, CF1
```

After OM1 and AP1 are added, it should yield:
```
Item                          Price
----                          -----
OM1                           $3.69
AP1                           $6.00
-----------------------------------
Total                         $9.11
```

After the entire cart is added, it should yield:

```
Item                          Price
----                          -----
OM1                           $3.11
AP1                           $6.00
            APOM             $-3.00
CF1                          $11.23
            BOGO            $-11.23
CF1                          $11.23
-----------------------------------
Total                        $17.34
```

## Installation
### Clone 
- Clone this repo to your local maching using ```https://github.com/cindyavu/objectrocket-farmer-market.git```

### Setting up docker
```
$ cd objectrocket-farmer-market
$ docker build -t farmers_market .
``` 

### Running program
```
$ docker run -it farmers_market 
```

## Testing
- Tests will run automatically upon finishing the main program

## Usage
- Upon launching the program you will be prompted to enter an option:
```
What would you like to do? 
1. Add to cart
2. Check current cart
3. Checkout
Enter 1,2,3
Option:
```
- If the user chooses option 1, input product name by their product code 
```
What would you like to do? 
1. Add to cart
2. Check current cart
3. Checkout
Enter 1,2,3
Option: 1
__________________________

What item would you like to add? 
Item: AP1
__________________________

Apples added to cart!
```


