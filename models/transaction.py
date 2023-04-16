class Transaction:
    def __init__(self, tx_value, merchant_name, category_name, time_stamp, user, id = None):
        self.tx_value = tx_value
        self.merchant_name = merchant_name
        self.category_name = category_name
        self.time_stamp = time_stamp
        self.user = user
        self.id = id