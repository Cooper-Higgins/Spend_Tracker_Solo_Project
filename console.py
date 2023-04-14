import pdb
from models.user import User
from models.transaction import Transaction

import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
user_repository.delete_all()

user_1 = User('Sam', 'Fire', '01/01/1990', 'Glasgow', 'sam.fire@gmail.com', 1000.00)
user_repository.create(user_1)

transaction_1 = Transaction(10.00, 'Lidl', 'Supermarket', '01/04/2023')
transaction_repository.create(transaction_1)

pdb.set_trace()