class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def sayFirst_name(self):
        print(self.f_name)

    def sayLast_name(self):
        print(self.l_name)

    def sayUser_name(self):
        print(self.f_name, self.l_name)
