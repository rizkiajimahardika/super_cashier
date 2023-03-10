# Python Project: Super Cashier
## Backgrounds
Andi is the owner of a large supermarket in a city in Indonesia. Andi has plans to improve business processes, namely Andi will create a self-service cashier system in his supermarket. So that customers can directly enter the items purchased, the number of items purchased, and the price of the items purchased and other features.

So that customers who are not in the city can buy goods from the supermarket. After Andi did his research, it turned out that Andi had a problem, namely Andi needed a programmer to develop features so that the self-service cashier system at the supermarket could run smoothly.

## Project Requirements
1. Create a super cashier application that can perform the following tasks:
   - Adding items by entering the name, price, and the number of items purchased by the user.
   - Update the name, price, or number of items purchased.
   - Delete purchased items.
   - Reset transactions.
   - Displays purchased items.
   - Check the input of goods that have been entered by the user.
   - Calculating the total price and discount obtained by the user.
2. Testing the application with a *test case*.
3. Creating a modular code and implementing Clean Code (PEP 8).

## Program Flow / Flowchart
1. Create a new folder named 'modules' to store project modules.
2. Create a new module named "transaction.py" in the modules folder.
3. Import the uuid package to the module to create transaction id.
4. Create a Transaction class that has ID and Order properties
5. Create various methods from the class, namely:
    - add_item() method to add a new item.
    - update_item_name(), update_item_qty() and update_item_price() methods to update item details.
    - delete_item() method to delete items.
    - reset_transaction() method to delete all items in the transaction.
    - check_order() method to check the format of the items that have been entered by the user.
    - total_price() method to calculate the total price.

      ![transaction_class](https://user-images.githubusercontent.com/79896604/212534776-139ae6b9-9f53-4df3-9445-3ec2671d4de7.jpeg)    

6. Create the main application file, namely 'cashier.py' outside the module folder
7. Import the 'transaction.py' module into the 'cashier.py' file.
8. Create a 'test_case' object from Class Transaction().
9. Run all test cases.

![flowchart](https://user-images.githubusercontent.com/79896604/212534797-292fa842-3b51-4bad-9e0b-d97f0c6897fc.png)

## Test Case Results
### Test 1
Add items
![111](https://user-images.githubusercontent.com/79896604/212711630-08c220eb-3697-4cbb-acfa-cbc582a3f403.png)


### Test 2
Delete an item from the transaction
![222](https://user-images.githubusercontent.com/79896604/212713831-2dcca700-2e31-4c8f-825d-adc68a24f891.png)


### Test 3
Reset the transaction
![333](https://user-images.githubusercontent.com/79896604/212713855-7fe00d91-defd-4955-97b3-7ce4b451639d.png)

### Test 4
Count the total price
![4444](https://user-images.githubusercontent.com/79896604/212713874-568c9d94-3500-495e-84cc-5e1b1f5a41a6.png)


## Conclusion
The super cashier program can run well in the python programming language. In this super cashier program, there is one class, namely transaction which holds several methods such as add_item, update_item, delete_item, and others. In addition, there is a feature to calculate discounts if the customer has a total purchase according to the terms and conditions that apply.
