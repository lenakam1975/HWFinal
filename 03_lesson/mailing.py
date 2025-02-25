class Mailing:
    def __init__(self, track, from_address, to_address, cost):
        self.Address1 = to_address
        self.Address2 = from_address
        self.String = track
        self.Numbers = cost

    def __str__(self):
        return f"{self.String} из {self.Address2} в {self.Address1}. Стоимость {self.Numbers} рублей."


#В классе должно быть четыре поля:
# to_address (тип данных Address );
# from_address (тип данных Address );
# cost (тип данных число);
# track (тип данных строка).