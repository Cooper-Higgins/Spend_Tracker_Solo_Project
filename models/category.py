class Category:
    def __init__(self, category_name, inactive = False, id = None):
        self.category_name = category_name
        self.inactive = inactive
        self.id = id

    def mark_inactive(self):
        self.inactive = True