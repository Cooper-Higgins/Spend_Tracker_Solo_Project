class Merchant:
    def __init__(self, merchant_name, inactive = False, id = None):
        self.merchant_name = merchant_name
        self.inactive = inactive
        self.id = id

    def mark_inactive(self):
        self.inactive = True