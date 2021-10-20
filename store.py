# # # # # Declarations # # # # #

cash = 0

quant_products = {
    1 : 10,
    2 : 13
}
price_products = {
    1 : 6,
    2 : 13
}

option = 0

# # # # # Functions # # # # #

def get_product_price(code):
    if not price_products:
        return False
    else:
        return price_products[code]

def get_quantity_product(code):
    if not quant_products:
        return False
    else:
        return quant_products[code]
    
def get_detail_product(code):
    if not quant_products:
        if not price_products:
            return False
    else:
        quantity = get_quantity_product(code)
        price = get_product_price(code)
        
        msg = "{}, {}".format(quantity, price)
        return msg
    
def get_cash():
    global cash
    
    return float(cash)

def add_quantity(code, quantity):
    if not quant_products:
        return False
    else:
        quant_products[code] = get_quantity_product(code) + quantity
   
def set_price(code, price):
    if not price_products:
        return False
    else:
        price_products[code] = price
        msg = "Price of",price_products[code],"updated."
        return msg
        
def product_sold(code):
    if not price_products or not quant_products:
        return False
    else:
        global cash
        cash = cash + (get_product_price(code)*get_quantity_product(code))
        quant_products[code] = 0
        msg = "SUCCESSFULY SOLD"
        return msg

def restock_product(code, quantity):
    global cash
    if not price_products or not quant_products:
        return False
    elif cash < get_product_price(code) * quantity:
        msg = "NOT ENOUGH TO OPERATE."
        return msg
    else:
        cash = cash - (get_product_price(code) * 0.2)
        quant_products[code] = get_quantity_product(code) + quantity
        msg = "SUCCESSFULY RESTOCKED"
        return msg

def get_full_stock():
    if not price_products or not quant_products:
        return False
    else:
        full_stock = []
        for k in quant_products.keys():
            full_stock.append( (k,quant_products[k],price_products[k]) )
            
        return full_stock
    
def menu():
    print("---------------")
    print("1. Show store details")
    print("2. Sales")
    print("3. Replace")
    print("4. Change price of product")
    print("5. Exit")
    print("---------------")

while True:
    menu()
    
    option = int(input("Choose an option"))
    
    if option == 1:
        
        if get_full_stock() == False:
            print("ERROR. EMPTY DATA.")
        else:
            print("STORE STATUS")
            print("================")
            print("Code - Units - Price")
            for e in get_full_stock():
                print(e)
            print("Cash",get_cash(),"€")
    
    if option == 2:
        code = int(input("Enter product code: "))
        
        if product_sold(code) == False:
            print("ERROR. EMPTY DATA.")
        else:
            print(product_sold(code))
    
    if option == 3:
        code = int(input("Enter product code: "))
        units = int(input("Enter units: "))
        
        if restock_product(code, units) == False:
            print("ERROR. EMPTY DATA.")
        else:
            print(restock_product(code, units))
            
    if option == 4:
        code = int(input("Enter product code: "))
        price = float(input("Set new price: "))
        
        if set_price(code, price) == False:
            print("ERROR. EMPTY DATA.")
        else:
            print(set_price(code, price))
    
    if option == 5:
        print("Bye-bye!")
        break