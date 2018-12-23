import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
import time    
import traceback

        
@app.route('/adduser', methods=['POST'])
def add_user():
    try:
        _json = request.json
        if not (_json and 'name' in _json and 'email' in _json and 'pwd' in _json): 
            return not_found()
        _name = _json['name']
        _email = _json['email']
        _password = _json['pwd']
        # validate the received values
        if _name and _email and _password and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_users(user_name, user_email, user_password) VALUES(%s, %s, %s)"
            data = (_name, _email, _password,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

@app.route('/users', methods=['GET'])
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_users")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
@app.route('/user/<int:id>', methods=['GET'])
def user(id):
    try:
        print id, 'iddddddd'
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_users WHERE user_id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        _json = request.json
        if not (_json and 'name' in _json and 'email' in _json and 'pwd' in _json): 
            return not_found()
        _name = _json['name']
        _email = _json['email']
        _password = _json['pwd']        
        # validate the received values
        if _name and _email and _password and id and request.method == 'PUT':
            # save edits
            sql = "UPDATE tbl_users SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (_name, _email, _password, id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            if cursor.rowcount > 0:
                resp = jsonify('User updated successfully!')
                resp.status_code = 201
                return resp
            else:
                resp = jsonify('No user exists!!')
                resp.status_code = 200
                return resp
        else:
            return not_found()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_users WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 201
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
@app.route('/addproduct', methods=['POST'])
def add_prod():
    try:
        _json = request.json
        if not (_json and 'name' in _json and 'count' in _json and 'price' in _json): 
            return not_found()
        _name = _json['name']
        _count = _json['count']
        _price = _json['price']
        # validate the received values
        if _name and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_inv(prod_name, store_count, price, create_time) VALUES(%s, %s, %s, %s)"
            data = (_name, str(_count),str(_price), time.strftime('%Y-%m-%d %H:%M:%S'),)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Product added successfully!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
        
@app.route('/products', methods=['GET'])
def products():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_inv")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
@app.route('/product/<int:id>', methods=['GET'])
def product(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_inv WHERE prod_id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

@app.route('/updateproduct<int:id>', methods=['PUT'])
def update_product(id):
    try:
        _json = request.json
        if not (_json and 'name' in _json and 'count' in _json and 'price' in _json): 
            return not_found()
        _name = _json['name']
        _count = _json['count']
        _price = _json['price']
        # validate the received values
        if _name and _count and id and request.method == 'PUT':
            # save edits
            sql = "UPDATE tbl_inv SET prod_name=%s, store_count=%s, price = %s, create_time=%s WHERE prod_id=%s"
            data = (_name, _count,_price, time.strftime('%Y-%m-%d %H:%M:%S'), id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            if cursor.rowcount > 0:
                resp = jsonify('Product updated successfully!')
                resp.status_code = 201
                return resp
            else:
                resp = jsonify('No Product exists!!')
                resp.status_code = 200
                return resp
        else:
            return not_found()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
@app.route('/deleteproduct/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_inv WHERE prod_id=%s", (id,))
        conn.commit()
        resp = jsonify('Prod deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
# Utility function to get the latest order id NOT USED -- 
def latest_order():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(order_id) FROM tbl_ord_details")
        row = cursor.fetchone()
        conn.commit()
        return row[0] or 0
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
    return 0


# Utility function to Nicely format the order and topup lists
def form_dict(ord_list):
    for item in ord_list:
        item['products'] = eval(item['products'])
    return ord_list

        
# To order products
@app.route('/order', methods=['POST'])
def order_():
    try:
        _json = request.json
        if not (_json and 'user' in _json and 'products' in _json): 
            return not_found()
        _user = _json['user']
        _prods = _json['products']
        # validate the received values
        if _user and _prods and all(['id' in item and item['id'] > 0 and 'quant' in item for item in _prods]) and request.method == 'POST':
            #_order = latest_order()+1
            _prod_map = dict([(item['id'],item['quant'],) for item in _prods])
            sql_1 = "INSERT INTO tbl_orders(user_id) VALUES(%s)" %_user
            sql_2 = "UPDATE tbl_inv SET store_count = store_count - %s, last_order = %s WHERE prod_id = %s and store_count >= %s"
            sql_3 = "SELECT prod_id, prod_name, price FROM tbl_inv where last_order = %s" 
            sql_4 = "INSERT INTO tbl_ord_details(order_id, prod_id, quant, sold_price) VALUES(%s, %s, %s, %s)"
            sql_5 = "UPDATE tbl_orders SET order_date = %s, total_count  =%s, order_value =%s WHERE order_id = %s"
            try:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql_1)
                _order = cursor.lastrowid
                data_2 = [(item['quant'], _order, item['id'],item['quant'],) for item in _prods]
                cursor.executemany(sql_2,data_2)
                cursor.execute(sql_3,(_order,))
                avail_prods = cursor.fetchall()
                print 'available: ', avail_prods
                if not avail_prods:
                    raise Exception('No product you want is available')
                data_4 = [(_order, i[0], _prod_map[i[0]], i[2],) for i in avail_prods]
                data_5 = (time.strftime('%Y-%m-%d %H:%M:%S'),sum([_prod_map[i[0]] for i in avail_prods]),sum([_prod_map[i[0]]*i[2] for i in avail_prods]),_order,)
                cursor.executemany(sql_4, data_4)
                cursor.execute(sql_5, data_5)
                conn.commit()
            except Exception as error :
                print(traceback.format_exc())
                print(error)
                #print("Failed to order: {}".format(error))
                #reverting changes because of exception
                conn.rollback()
                resp = jsonify("Failed to order: {}".format(error))
                resp.status_code = 520
                return resp
            resp = jsonify('Ordered these successfully! ' + ', '.join([i[1] for i in avail_prods]))
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# Get all orders till now
@app.route('/orders', methods=['GET'])
def orders():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        #cursor.execute("SELECT * FROM tbl_ord_details")
        #cursor.execute("SELECT a.user_id, a.order_id, CONCAT('[',GROUP_CONCAT(CONCAT('{','id: ',a.prod_id,', name: ',b.prod_name,', quantity: ',a.quant,', price: ',a.sold_price,'}')),']') as products  FROM tbl_ord_details AS a INNER JOIN tbl_inv AS b ON a.prod_id = b.prod_id  GROUP BY a.order_id,a.user_id;")
        cursor.execute("SELECT temp.order_id,user_id,order_date,total_count,order_value,temp.products FROM tbl_orders, (SELECT a.order_id, CONCAT('[',GROUP_CONCAT(CONCAT('{','''id'': ',a.prod_id,', ''name'': ''',b.prod_name,''', ''quantity'': ',a.quant,', ''price'': ',a.sold_price,'}')),']') as products  FROM tbl_ord_details AS a INNER JOIN tbl_inv AS b ON a.prod_id = b.prod_id  GROUP BY a.order_id) AS temp WHERE tbl_orders.order_id = temp.order_id;")
        rows = cursor.fetchall()
        resp = jsonify(form_dict(rows))
        #resp = jsonify(rows)
        #print rows, type(rows), 'Check here'
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# All orders by a user
@app.route('/ordersby/<int:id>', methods=['GET'])
def orders_by(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        #cursor.execute("SELECT * FROM tbl_ord_details WHERE user_id=%s", id)
        #cursor.execute("SELECT a.order_id, CONCAT('[',GROUP_CONCAT(CONCAT('{','id: ',a.prod_id,', name: ',b.prod_name,', quantity: ',a.quant,', price: ',a.sold_price,'}')),']') as products  FROM tbl_ord_details AS a INNER JOIN tbl_inv AS b ON a.prod_id = b.prod_id WHERE a.user_id = %s GROUP BY a.order_id;", id)
        cursor.execute("SELECT temp.order_id,user_id,order_date,total_count,order_value,temp.products FROM tbl_orders, (SELECT a.order_id, CONCAT('[',GROUP_CONCAT(CONCAT('{','''id'': ',a.prod_id,', ''name'': ''',b.prod_name,''', ''quantity'': ',a.quant,', ''price'': ',a.sold_price,'}')),']') as products  FROM tbl_ord_details AS a INNER JOIN tbl_inv AS b ON a.prod_id = b.prod_id  GROUP BY a.order_id) AS temp WHERE user_id = %s AND  tbl_orders.order_id = temp.order_id;",id)
        rows = cursor.fetchall()
        #resp = jsonify(rows)
        resp = jsonify(form_dict(rows))
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
        
# All orders of a Product
@app.route('/ordersof/<int:id>', methods=['GET'])
def orders_of(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_ord_details WHERE prod_id=%s", id)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# Utility function to get the latest topup id. Unlike latest_order, this is USED. We assume there'll be only one user topping up the inventory
def latest_topup():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(topup_id) FROM tbl_topups")
        row = cursor.fetchone()
        conn.commit()
        return row[0] or 0
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
    return 0
        
@app.route('/topup', methods=['POST'])
def topup_():
    try:
        _json = request.json
        if not (_json and 'products' in _json): 
            return not_found()
        _prods = _json['products']        # validate the received values
        if _prods and all(['id' in item and item['id'] > 0 and 'count' in item for item in _prods]) and request.method == 'POST':
            _topup = latest_topup()+1
            sql = "INSERT INTO tbl_topups(topup_id, prod_id, count, topup_date) VALUES(%s, %s, %s, %s)"
            data = [(_topup,item['id'], item['count'], time.strftime('%Y-%m-%d %H:%M:%S'),) for item in _prods]
            sql_ = "UPDATE tbl_inv SET store_count = store_count + %s, last_topup = %s WHERE prod_id = %s"
            data_ = [(item['count'], _topup, item['id'],) for item in _prods] # time.strftime('%Y-%m-%d %H:%M:%S') for modified time in prod
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            cursor.executemany(sql_, data_)
            conn.commit()
            resp = jsonify('Topped up successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

@app.route('/topups', methods=['GET'])
def topups():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        #cursor.execute("SELECT * FROM tbl_topups")
        cursor.execute("SELECT a.topup_id, CONCAT('[',GROUP_CONCAT(CONCAT('{','''id'': ',a.prod_id,', ''name'': ''',b.prod_name,''', ''quantity'': ',a.count,'}')),']') as products  FROM tbl_topups AS a INNER JOIN tbl_inv AS b ON a.prod_id = b.prod_id  GROUP BY a.topup_id;")
        rows = cursor.fetchall()
        resp = jsonify(form_dict(rows))
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# All topups of a product. 
@app.route('/topupsof/<int:id>', methods=['GET'])
def topups_of(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_topups where prod_id = %s", id)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
        
if __name__ == "__main__":
    app.run(debug = True, host = '127.0.0.1', port = 5057)