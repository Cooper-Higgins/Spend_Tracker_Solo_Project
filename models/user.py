class User:
    def __init__(self, first_name, last_name, dob, city, email, budget, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.city = city
        self.email = email
        self.budget = budget
        self.id = id