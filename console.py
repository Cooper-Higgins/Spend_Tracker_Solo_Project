from models.transaction import Transaction
from models.user import User
from models.category import Category
from models.merchant import Merchant

import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository

transaction_repository.delete_all()
user_repository.delete_all()
category_repository.delete_all()
merchant_repository.delete_all()

user_1 = User('Sam', 'Fire', '01/01/1990', 'Glasgow', 'sam.fire@gmail.com', 1000.00)
user_repository.create(user_1)

user_repository.select_all()

category_1 = Category('Travel')
category_repository.create(category_1)

merchant_1 = Merchant('British Airways')
merchant_repository.create(merchant_1)

transaction_1 = Transaction(10.00, 'Lidl', 'Supermarkets', '01/04/2023 17:48:59', user_1)
transaction_repository.create(transaction_1)
transaction_2 = Transaction(125.00, 'Glasgow City Council', 'Bills', '04/01/2023 07:00:00', user_1)
transaction_repository.create(transaction_2)
transaction_3 = Transaction(61.50, 'Porter & Rye', 'Restaurants', '03/28/2023 21:05:10', user_1)
transaction_repository.create(transaction_3)
transaction_4 = Transaction(2.50, 'Andina', 'Coffee', '03/10/2023 08:31:45', user_1)
transaction_repository.create(transaction_4)
transaction_5 = Transaction(9.99, 'Freetrade', 'Investing', '03/28/2023 08:00:00', user_1)
transaction_repository.create(transaction_5)
transaction_6 = Transaction(210.91, 'American Express', 'Finances', '04/01/2023 05:00:00', user_1)
transaction_repository.create(transaction_6)
transaction_7 = Transaction(450.00, 'Barclays', 'Finances', '04/01/2023 06:00:00', user_1)
transaction_repository.create(transaction_7)
transaction_8 = Transaction(120.00, 'Octopus', 'Utilities', '04/01/2023 02:00:00', user_1)
transaction_repository.create(transaction_8)