# CLI based e-commerce app

## An e-commerce app using json for storage and allowing users to perform CRUD operations on their cart and perform other basic e-commerce app functionality with fake money

This project was built to tie together my learning of core Python syntax beyond basic syntax excersises and small projects building a real structured application
This project helped me practiccally use and apply
  - OOP
  - File handling
  - SoC

---

## Features
  - Admin control allowing admins to perform CRUD operations on products and to view users and user count
  - Password hashing is usedd throghout with bcrypt
  - products viewing and a fully functional cart
  - depositing money (fake money)

---

## how to run
  - make sure you have python installed
  - make sure you have bcrypt installed if not run:
    - pip install bcrypt
  - clone the github repository
    - git clone https://github.com/your-username/cli-ecommerce-app.git cd cli-ecommerce-app
  - run it
    - python main.py

---

## Usage examples

# Logging In as a non-Admin Account
This is the CLI based e-commerce app! made by mr.e  
  
press q if you'd like to close the app otherwise hit anything else  
Hello this is the User Gate you will have to login or signup enter 1 or 2  
[1] login  
[2] signup  
1  
Please Enter your username: coolguy123  
please Enter your password: pass123  
Alright, you're now inside the app!  
  
Welcome coolguy123  
[0] End Session / Log out  
[1] Browse Products  
[2] View Cart  
[3] View Account Balance  
[4] Make a Deposit  
[5] View Order History  
Select option:  
  
# Logging In as an Admin  
This is the CLI based e-commerce app! made by mr.e  
  
press q if you'd like to close the app otherwise hit anything else  
Hello this is the User Gate you will have to login or signup enter 1 or 2  
[1] login  
[2] signup  
1  
Please Enter your username: cool admin  
please Enter your password: password  
Alright, you're now inside the app!  
  
Welcome cool admin  
[0] End Session / Log out  
[1] Browse Products  
[2] View Cart  
[3] View Account Balance  
[4] Make a Deposit  
[5] View Order History  
[6] Admin: add a product  
[7] Admin: remove a product  
[8] Admin: edit a product  
[9] Admin: view users  
[10] Admin: view number of users  
Select option:  
  
# Adding a product to your cart  
Select option: 1  
name: 65% Mechanical Keyboard  
description: Cream coloured compact 65% mechanical keyboard, wired with detachable USB-C cable. Great for work and gaming.  
cost: 50  
weight: 500  
product_id: 1000  
  
name: Wireless Mouse  
description: Ergonomic wireless mouse with 50m range, RGB lighting, and adjustable DPI for precise control.  
cost: 30  
weight: 100  
product_id: 1001  
  
name: 27-inch 4K Monitor  
description: Ultra HD 4K monitor with vibrant colors, 60Hz refresh rate, and HDMI/DisplayPort inputs.  
cost: 300  
weight: 4000  
product_id: 1002  
  
name: USB-C Hub  
description: Multiport USB-C hub with 4 USB 3.0 ports, HDMI output, SD card reader, and fast data transfer.  
cost: 45  
weight: 150  
product_id: 1003  
  
name: Noise Cancelling Headphones  
description: Over-ear wireless headphones with active noise cancellation, 20-hour battery life, and Bluetooth 5.0.  
cost: 120  
weight: 350  
product_id: 1004  
  
name: Mechanical Gaming Keyboard  
description: RGB mechanical gaming keyboard with customizable lighting, programmable macros, and wrist rest.  
cost: 80  
weight: 700  
product_id: 1005  
  
name: Ergonomic Office Chair  
description: Comfortable ergonomic chair with adjustable height, lumbar support, and breathable mesh back.  
cost: 150  
weight: 15000  
product_id: 1006  
  
  
would you like to do:  
[1] add a product to your cart  
[2] buy a product  
[3] delete a product globally  
[4] Edit a product  
[5] add a product globally  
[6] nothing I'm good  
1  
Enter the product ID of the product you wanna add to your cart: 1000  
Enter the amount you'd like to add: 2  
2 of product 1000 added to cart successfully!  
  
# globally creating a new product as Admin  
[0] End Session / Log out  
[1] Browse Products  
[2] View Cart  
[3] View Account Balance  
[4] Make a Deposit  
[5] View Order History  
[6] Admin: add a product  
[7] Admin: remove a product  
[8] Admin: edit a product  
[9] Admin: view users  
[10] Admin: view number of users  
Select option: 6  
Enter product name: water-gun  
Enter product description: this cool plastic watergun is fun for the whole family!  
Enter product cost: 10  
Enter product weight: 500   
Added product water-gun  