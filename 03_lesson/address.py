class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apart = apartment

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house}-{self.apart}"


#Класс должен содержать в себе поля:
# «индекс»,
# «город»,
# «улица»,
# «дом»,
# «квартира».