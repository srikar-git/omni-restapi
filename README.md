# omni-restapi
Task of creating a rest api for basic inventory/ordering products


Objective: Create backend logic for a basic inventory and orders model. We keep track of the count of products present in the inventory


Running instructions:

mysql is needed and listed the needed python packages below.

You can use create.sql script to create the tables. This will create a database named omni1 and create tables in it. Make sure you set this in db_confi.py. OR
omni_bkp.sql is a dump of a db (with name omni) with some data already in. You can restore this dump also.


main.py,db_config.py,app.py should be there in the folder.
Give the db details in the db_config.py and run the main.py.
It will run on host = 127.0.0.1 and on port = 5057
Access is like this http://127.0.0.1:5057/<path>
Paths for various jobs:
/adduser - POST, Add a user, Takes input json which should have name, email and pwd, E.g., - {
	"name":"user 1oo",
	"email":"user1@la.al",
	"pwd":"1usr"
} 
/users - GET all the users
/update/<id> - PUT update user by user id, input json should have name, email, pwd
/delete/<id> - DELETE delete user by id
/addproduct - POST add product, Takes input json which should have name, count, price
/updateproduct/<id> - PUT update product by id,  input json which should have name, count, price
/products - GET  get all the products
/product/<id> - GET  get the product by id
/deleteproduct - DELETE delete product by id
/order - POST, To order, user, products should be there in the input json, each product should have id and quant Example:{
	"user":1,
	
  "products":
   [ 
	  	{
	        "id": 4,
	        "quant": 5
	    }
    ]
}
/orders - GET get all the orders
/ordersby/<id> - GET get all the orders by a user (user id to be given)
/ordersof/<id> - GET get all the orders of a product
/topup - POST To topup the inventory, input json should have products, and each product should have id and count
/topups - GET To get all the topups till now
/topups_of/<id> - GET To get all the topups of a product till now



Versions:
python 2.7.12  (should be working with python 3 also )
mysql  Ver 14.14 Distrib 5.7.24, for Linux (x86_64) using  EditLine wrapper
python packages:
flask, flask-mysql
pymysql for getting results as dictionaries

Flask==1.0.2
Flask-MySQL==1.4.0
PyMySQL==0.9.3


Assumptions:
One order or topup will have a product only once in the input request json (Error is thrown otherwise). UI can generally ensure that.
If by an order the count of a product is going negative that product won't be sold in that order but the rest will be sold. If none can be sold, the order is not accepted.

We're storing only dates in db and not the times. The results may give time as 0:0:0 always. sql dat -> python date object 

Assumed all products are sold at their original price. But maintained sold_price in order details of each product, if we want to introduce discounts afterwards.

latest_topup is the Utility function to get the latest topup id. Unlike latest_order, this is USED. We assume there'll be only one user topping up the inventory.


Tables and columns:
 
tables: tbl_users, tbl_inv, tbl_ord, tbl_topups

tbl_orders - order_id, user_id, order_date, total_count, order_value   ---> One record is one order, primary key is order_id

tbl_ord_details - order_id, prod_id, quant, sold_price   --> primary key is order_id+prod_id

tbl_inv - prod_id, prod_name, store_count, create_time, last_order, last_topup

tbl_topups - topup_id, prod_id, topup_date, count    --> primary key is topup_id+prod_id

tbl_users - user_id, user_name, user_email, user_password


