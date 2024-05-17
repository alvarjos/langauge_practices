# Name: Jacob Steffen
# Description: This program imports some mock product data, some of which is related to Electronics. Electronics have warranties that boost the final sale price. Products get put in orders, and then it displays the items in the order.

import random # to randomly generate stuff

# choose one of the following to use. You don't need both.
import openpyxl
import pandas as pd

class Product:
    def __init__(self, product_id, product_name, product_category, price): # the constructor
        self.product_id = product_id # all of these are instance variables
        self.product_name = product_name
        self.product_category = product_category
        self.price = price

    def display_info_and_return_price(self):
        print(f"\t{self.product_name}: {self.price}") # prints out info
        return self.price # returns the price of the product

class ElectronicProduct(Product):
    def __init__(self, product_id, product_name, product_category, price, warranty_type, warranty_price_percent):
        super().__init__(product_id, product_name, product_category, price) # uses super to add all the same instance variables as Product
        self.warranty_type = warranty_type # some extra instance variables that only ElectronicProduct gets
        self.warranty_price_percent = warranty_price_percent

    def display_info_and_return_price(self):
        warranty_boosted_price = self.price * (1 + self.warranty_price_percent) # calculate the increased cost due to the warranty.
        print(f"\t{self.product_name}: {self.price}. Price including {self.warranty_type} warranty: {warranty_boosted_price:.2f}")
        return warranty_boosted_price # return the warranty_boosted_price.

class Order:
    def __init__(self):
        self.order_id = random.randint(1,50000) # you could do this outside the constructor and pass it in too.
        self.list_of_products = [] # an empty list to store products later.

    def add_products_to_order(self, passed_list_of_products, num_products_to_add):
        for _ in range(num_products_to_add): # _ is convention when you don't use the looping variable
            randomly_chosen_product = random.choice(passed_list_of_products)
            self.list_of_products.append(randomly_chosen_product)
        print(f"Added {num_products_to_add} products to order #{self.order_id}")    

    def show_all_products_and_total(self):
        print(f"Order #{self.order_id} has the following products: ")
        order_total = 0
        for product in self.list_of_products:
            order_total += product.display_info_and_return_price()
        print(f"\tThe order total is: {order_total:.2f}")

    
# import the excel file of product information. You can use pandas or openpyxl

# using pandas:
df_products = pd.read_excel("product_data.xlsx")
list_of_products = []
for index, row in df_products.iterrows():
    product_id, product_name, product_category, price, warranty_type, warranty_price_percent = row

    if product_category == 'Electronics':
        product_object = ElectronicProduct(product_id, product_name, product_category, price, warranty_type, warranty_price_percent)
    else:
        product_object = Product(product_id, product_name, product_category, price)
    list_of_products.append(product_object)

# using openpyxl:
# wb_products = openpyxl.load_workbook("product_data.xlsx")
# list_of_products = []
# for row in wb_products.active.iter_rows(min_row=2, values_only = True):
#     product_id, product_name, product_category, price, warranty_type, warranty_price = row

#     if product_category == 'Electronics':
#         product_object = ElectronicProduct(product_id, product_name, product_category, price, warranty_type, warranty_price)
#     else:
#         product_object = Product(product_id, product_name, product_category, price)
#     list_of_products.append(product_object)

# now create 5 orders and put them in a list:
list_of_orders = []
for _ in range(5):
    order_object = Order()
    list_of_orders.append(order_object)


# now add a random number of products between 1 and 5 to each of the orders:
for order in list_of_orders:
    rand_num = random.randint(1,5)
    order.add_products_to_order(list_of_products, rand_num)

# show the order total for all the products.
for order in list_of_orders:
    order.show_all_products_and_total()