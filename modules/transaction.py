import uuid
'''Import library uuid to make unique id'''

class Transaction:
  '''
  Create a transaction class to run the super cashier program
  '''
  
  def __init__(self):
    '''
    defines a transaction class that holds the id parameter using the imported uuid library and defined items with empty dictionary value 
    '''
    self.id = uuid.uuid1()
    self.items = {}
  
  def add_item(self, item_detail):
    '''
    create an add_item method that contains name, qty, and price. Then after that we add it to the dictionary that was created in the transaction class

    Parameters 
    item_detail : list
    contained name from first list
    qty from second list
    price from third list
    and then append to self.items
    '''
  
    name = item_detail[0]
    qty = item_detail[1]
    price = item_detail[2]
    # append item as a key value pair to items (dictionary)
    self.items[name] = [qty, price]
    print(f"Purchased Items : {self.items}")
  
  def update_item_name(self, old_item_name, new_item_name):
    '''create an update_item_name method that is used to change the item name

    Parameters
    old_item_name, new_item_name : str
      Creates a value object that contains the old_item_name parameter
      Then initializes the new item name into the value object
      After that delete the old item name
  
    '''
    # get element value from old item
    value = self.items[old_item_name]
    # append the new item name to items dictionary as a new key
    self.items[new_item_name] = value
    # delete the old item
    del self.items[old_item_name]
    print(f"Purchased Items : {self.items}")
  
  def update_item_qty(self, item_name, new_item_qty):
    '''
    create an update_item_qty method that is used to change item qty

    Parameters
    item_name, new_item_qty : str, int
    Initialize new_item_qty to the first self items list
    '''
    
    # replace the item quantity
    
    self.items[item_name][0] = new_item_qty
    print(f"Purchased Items : {self.items}")
  
  def update_item_price(self, item_name, new_item_price):
    '''create an update_item_price method that is used to change item prices
  
    Parameters:
    item_name, new_item_price : str, int         
    Initialize new_item_price to the second self items list
      
    '''
    self.items[item_name][1] = new_item_price
    print(f"Purchased Items : {self.items}")
 
  def delete_item(self, item_name):
    '''
    create a delete_item method that contains the item_name parameter which is used to delete one of the items you
    want to delete
    
    Parameters:
    item_name : str
    delete item_name
    '''
    del self.items[item_name]
    print(f"Purchased Items : {self.items}")
  
  def reset_transaction(self):
    '''
    create a reset transaction method that is used to delete all recorded transactions
    '''
    self.items.clear()
    print("All items are deleted!")
  
  def showTransaction(self):
    '''
    create a show_transaction method to display item name, quantity, price, and total price
    '''
    i = 0
    print("==============================================================================")
    print("| No. | Item Name         | Quantity  | Price             | Total Price     |")
    print("==============================================================================")
    for key in self.items:
      i += 1
      qty = self.items[key][0]
      price = self.items[key][1]
      total_item_price = qty * price
      print(f"| {i}   | {key:<18}| {qty:<10}| {price:<17} | {total_item_price:<16}|")
    print("==============================================================================")
    
  def check_items(self):
    '''
    create a check_items method that is used to ensure whether the data entered in the items is correct
    '''
    error = 0
    print("\nChecking items...")
    for key in self.items:
      # iterate through self.items item key
      # send error if the key is not an str
      if (type(key) is not str):
        error += 1
        print(
          f"There is an error in items with name of '{key}'. It should be a string"
        )
        print(f"value = {key}: {self.items[key]}")
      for item in self.items[key]:
        # get each value from key
        # check the item value data type
        if (type(item) is not int):
          error += 1
          # send error if the data type is not an integer
          print(
            f"There is an error in items with name of '{key}'. the value should be an integer"
          )
          print(f"value = {key}: {self.items[key]}")
    if (error == 0): 
      print("items format is already correct")
      self.showTransaction()
      return 0
    
  def total_price(self):
    '''Create a total_price function that is used to find out the total price of customers who make transactions with several conditions that get a discount'''
    # make variable for total price
    total_price = 0
    for key in self.items:
      qty = self.items[key][0]
      price = self.items[key][1]
      total_item_price = qty * price
      total_price += total_item_price
    #  check discount
    if total_price > 200000 and total_price <= 300000:
        print(f"Purchased Items {self.items}")
        print(f'Total price after discount is Rp. {total_price - (5/100*total_price)}')
    elif total_price > 300000 and total_price <= 500000:
        print(f"Purchased Items {self.items}")
        print(f'Total price after discount is Rp. {total_price - (8/100*total_price)}')
    elif total_price > 500000:
        print(f"Purchased Items {self.items}")
        print(f'Total price after discount is Rp. {total_price - (10/100*total_price)}')