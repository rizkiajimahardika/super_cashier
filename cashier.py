from modules import transaction
      
'''Test the program with a test_case'''   
test_case = transaction.Transaction()
test_case.add_item(['Ayam Goreng', 2, 220000])
test_case.add_item(['Pasta Gigi', 3, 150000])
test_case.delete_item('Pasta Gigi')
test_case.total_price()
test_case.reset_transaction()