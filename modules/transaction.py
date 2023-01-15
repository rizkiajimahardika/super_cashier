import uuid
'''Import library uuid to make unique id'''

class Transaction:
  '''
  Create a transaction class to run the super cashier program
  '''
  
  def __init__(self):
    '''
    defines a transaction class that holds the id parameter using the imported uuid library and defined order with empty dictionary value 
    '''
    self.id = uuid.uuid1()
    self.order = {}
  
  def add_item(self, item_detail):
    '''
    create an add_item method that contains name, qty, and price. Then after that we add it to the dictionary that was created in the transaction class

    Parameters 
    item_detail : list
    contained name from first list
    qty from second list
    price from third list
    and then append to self.order
    '''
  
    name = item_detail[0]
    qty = item_detail[1]
    price = item_detail[2]
    # append item as a key value pair to order (dictionary)
    self.order[name] = [qty, price]
    print(f"Item yang dibeli adalah : {self.order}")
  
  def update_item_name(self, old_item_name, new_item_name):
    '''create an update_item_name method that is used to change the item name

    Parameters
    old_item_name, new_item_name : str
      Creates a value object that contains the old_item_name parameter
      Then initializes the new item name into the value object
      After that delete the old item name
  
    '''
    # get element value from old item
    value = self.order[old_item_name]
    # append the new item name to order dictionary as a new key
    self.order[new_item_name] = value
    # delete the old item
    del self.order[old_item_name]
    print(f"Item yang dibeli adalah : {self.order}")
  
  def update_item_qty(self, item_name, new_item_qty):
    '''
    create an update_item_qty method that is used to change item qty

    Parameters
    item_name, new_item_qty : str, int
    Initialize new_item_qty to the first self order list
    '''
    
    # replace the item quantity
    
    self.order[item_name][0] = new_item_qty
    print(f"Item yang dibeli adalah : {self.order}")
  
  def update_item_price(self, item_name, new_item_price):
    '''create an update_item_price method that is used to change item prices
  
    Parameters:
    item_name, new_item_price : str, int         
    Initialize new_item_price to the second self order list
      
    '''
    self.order[item_name][1] = new_item_price
    print(f"Item yang dibeli adalah : {self.order}")
 
  def delete_item(self, item_name):
    '''
    create a delete_item method that contains the item_name parameter which is used to delete one of the items you
    want to delete
    
    Parameters:
    item_name : str
    delete item_name
    '''
    del self.order[item_name]
    print(f"Item yang dibeli adalah : {self.order}")
  
  def reset_transaction(self):
    '''
    create a reset transaction method that is used to delete all recorded transactions
    '''
    self.order.clear()
    print("Semua item berhasil di delete!")
  
  def showTransaction(self):
    '''
    create a show_transaction method to display item name, quantity, price, and total price
    '''
    i = 0
    print("==============================================================================")
    print("| No. | Item Name         | Quantity  | Price             | Total Price     |")
    print("==============================================================================")
    for key in self.order:
      i += 1
      qty = self.order[key][0]
      price = self.order[key][1]
      total_item_price = qty * price
      print(f"| {i}   | {key:<18}| {qty:<10}| {price:<17} | {total_item_price:<16}|")
    print("==============================================================================")
    
  def check_order(self):
    '''
    create a check_order method that is used to ensure whether the data entered in the order is correct
    '''
    error = 0
    print("\nChecking Order...")
    for key in self.order:
      # iterate through self.order item key
      # send error if the key is not an str
      if (type(key) is not str):
        error += 1
        print(
          f"There is an error in order with name of '{key}'. It should be a string"
        )
        print(f"value = {key}: {self.order[key]}")
      for item in self.order[key]:
        # get each value from key
        # check the item value data type
        if (type(item) is not int):
          error += 1
          # send error if the data type is not an integer
          print(
            f"There is an error in order with name of '{key}'. the value should be an integer"
          )
          print(f"value = {key}: {self.order[key]}")
    if (error == 0): 
      print("Order format is already correct")
      self.showTransaction()
      return 0
    
  def total_price(self):
    '''Create a total_price function that is used to find out the total price of customers who make transactions with several conditions that get a discount'''
    # make variable for total price
    total_price = 0
    for key in self.order:
      qty = self.order[key][0]
      price = self.order[key][1]
      total_item_price = qty * price
      total_price += total_item_price
    #  check discount
    if total_price > 200000 and total_price <= 300000:
        print(f"Item yang dibeli adalah {self.order}")
        print(f'Total belanja yang harus dibayarkan adalah Rp. {total_price - (5/100*total_price)}')
    elif total_price > 300000 and total_price <= 500000:
        print(f"Item yang dibeli adalah {self.order}")
        print(f'Total belanja yang harus dibayarkan adalah Rp. {total_price - (8/100*total_price)}')
    elif total_price > 500000:
        print(f"Item yang dibeli adalah {self.order}")
        print(f'Total belanja yang harus dibayarkan adalah Rp. {total_price - (10/100*total_price)}')