# Creating a list with 4 menu items in the cafe
menu = ["orange juice", "flat white", "cheese toast", "chocolate muffin"]

# Creating a dictionary called stock which contains inventory item in the cafe
stock = {"orange juice": 25, "flat white": 35, "cheese toast": 18, "chocolate muffin": 15}

# Creating a dictionary called price which contains how much each items costs in £
price = {"orange juice": 2.50, "flat white": 1.75, "cheese toast": 3.50, "chocolate muffin": 2.00}

# Validating that all menu list keys are present in the stock and price dictionaries
menu_keys_present = True
for key in menu:
    if key not in stock or key not in price:
        menu_keys_present = False
        print(f"{key}: not present in stock or price")
    else:
        print(f"{key}: present in stock and price")

# using a conditional statement if all keys are present and a for loop to iterate each menu item value in stock price,
# adding it together to find the total worth in the cafe
total_stock_value = 0
if menu_keys_present == True:
        for item in menu:
            total_stock_value += stock[item] * price[item]            
else:
    print("Not all menu items are present in both stock and price dictionaries")

# printing total stock value outside the loop to have the the total sum and not each iteration
print(f"The total stock value in the cafe is £{total_stock_value}")