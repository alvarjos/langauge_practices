# Angel 
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

import random
import pandas as pd

class Product():
    def __init__(self, product_id, product_name, product_category, price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category
        self.price = price
    
    def display_info_and_return_price(self):
        print(f"\t{self.product_name}: {self.price}")
        return self.price

class ElectronicProduct(Product):
    def __init__(self, product_id, product_name, product_category, price, warranty_type, warranty_price_percent):
        super().__init__(product_id, product_name, product_category, price)
        self.warranty_type = warranty_type
        self.warranty_price_percent = warranty_price_percent
    
    def display_info_and_return_price(self):
        warranty_boosted_price = self.price * (1 + self.warranty_price_percent)
        print(f"\t{self.product_name}: {self.price}. Price including {self.warranty_type} warranty: {warranty_boosted_price}")
        return warranty_boosted_price
    
class Order():
    def __init__(self):
        self.order_id = random.randint(1,50000)
        self.list_of_products = []

    def add_products_to_order(self, passed_list_of_products, num_products_to_add):
        for _ in range(num_products_to_add):
            randomly_chosen_product = random.choice(passed_list_of_products)
            self.list_of_products.append(randomly_chosen_product)
        print(f"Added {num_products_to_add} products to order {self.order_id}")
    
    def show_all_products_and_total(self):
        print(f"Order {self.order_id} has the following products:")
        # display_info_and_return_price(self.selected_product)
        total_price = 0
        for product in self.list_of_products:
            total_price += product.display_info_and_return_price()
        print(f"The total order total is {total_price}") 

df_products = pd.read_excel("instructions_final_practice_2_online_store\product_data.xlsx")
list_of_products = []

for index, row in df_products.iterrows():
    product_id, product_name, product_category, price, warranty_type, warranty_price_percent = row
    if product_category == "Electronics":
        product_object = ElectronicProduct(product_id, product_name, product_category, price, warranty_type, warranty_price_percent)
    else:
        product = Product(product_id, product_name, product_category, price)
    list_of_products.append(product_object)

ordered_list_of_products = []
for _ in range(5):
    order_object = Order()
    ordered_list_of_products.append(order_object)

for order in ordered_list_of_products:
    rand_num = random.randint(1,5)
    order.add_products_to_order(list_of_products, rand_num)

for order in ordered_list_of_products:
    order.show_all_products_and_total()
     


 



