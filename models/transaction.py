class Transaction:
    def __init__(self, tx_value, merchant, category, time_stamp, id = None):
        self.tx_value = tx_value
        self.merchant = merchant
        self.category = category
        self.time_stamp = time_stamp
        self.id = id
