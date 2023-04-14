from models.transaction import Transaction
from models.user import User

import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

transaction_repository.delete_all()
user_repository.delete_all()

user_1 = User('Sam', 'Fire', '01/01/1990', 'Glasgow', 'sam.fire@gmail.com', 1000.00)
user_repository.create(user_1)

user_repository.select_all()

transaction_1 = Transaction(10.00, 'Lidl', 'Supermarket', '01/04/2023', user_1)
transaction_repository.create(transaction_1)