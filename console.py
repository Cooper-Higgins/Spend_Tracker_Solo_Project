from models.user import User
from models.category import Category
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.user_repository as user_repository
import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

user_repository.delete_all()
category_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

user_1 = User('Sam', 'Fire', '01/01/1990', 'Glasgow', 'sam.fire@gmail.com', 1000.00)
user_repository.create(user_1)

category_gaming = Category('Gaming')
category_repository.create(category_gaming)
category_supermarkets = Category('Supermarkets')
category_repository.create(category_supermarkets)
category_transport = Category('Transport')
category_repository.create(category_transport)
category_cafes = Category('Cafés')
category_repository.create(category_cafes)
category_subscriptions = Category('Subscriptions')
category_repository.create(category_subscriptions)
category_leisure = Category('Leisure')
category_repository.create(category_leisure)
category_finances = Category('Finances')
category_repository.create(category_finances)
category_utilities = Category('Utilities')
category_repository.create(category_utilities)
category_travel = Category('Travel')
category_repository.create(category_travel)

merchant_fanduel = Merchant('FanDuel', False)
merchant_repository.create(merchant_fanduel)
merchant_lidl = Merchant('Lidl', False)
merchant_repository.create(merchant_lidl)
merchant_spt = Merchant('SPT', False)
merchant_repository.create(merchant_spt)
merchant_andina = Merchant('Andina', False)
merchant_repository.create(merchant_andina)
merchant_spotify = Merchant('Spotify', False)
merchant_repository.create(merchant_spotify)
merchant_glasgow_life = Merchant('Glasgow Life', False)
merchant_repository.create(merchant_glasgow_life)
merchant_barclays = Merchant('Barclays', False)
merchant_repository.create(merchant_barclays)
merchant_octopus = Merchant('Octopus', False)
merchant_repository.create(merchant_octopus)
merchant_skyscanner = Merchant('Skyscanner', False)
merchant_repository.create(merchant_skyscanner)

transaction_1 = Transaction(35.00, 'FanDuel', 'Gaming', '04/01/2023 16:58:01', user_1)
transaction_repository.create(transaction_1)
transaction_2 = Transaction(10.00, 'Lidl', 'Supermarkets', '04/01/2023 17:48:59', user_1)
transaction_repository.create(transaction_2)
transaction_3 = Transaction(3.00, 'SPT', 'Transport', '04/01/2023 21:05:10', user_1)
transaction_repository.create(transaction_3)
transaction_4 = Transaction(2.50, 'Andina', 'Cafés', '04/01/2023 08:31:45', user_1)
transaction_repository.create(transaction_4)
transaction_5 = Transaction(13.99, 'Spotify', 'Subscriptions', '04/02/2023 08:00:00', user_1)
transaction_repository.create(transaction_5)
transaction_6 = Transaction(27.00, 'Glasgow Life', 'Leisure', '04/03/2023 05:00:00', user_1)
transaction_repository.create(transaction_6)
transaction_7 = Transaction(450.00, 'Barclays', 'Finances', '04/03/2023 06:00:00', user_1)
transaction_repository.create(transaction_7)
transaction_8 = Transaction(120.00, 'Octopus', 'Utilities', '04/04/2023 02:00:00', user_1)
transaction_repository.create(transaction_8)
transaction_9 = Transaction(242.68, 'Skyscanner', 'Travel', '04/04/2023 12:01:58', user_1)
transaction_repository.create(transaction_9)
