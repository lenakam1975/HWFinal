from address import Address
from mailing import Mailing

to_address = Address("684000", "г.Елизово", "ул.Набережная", "25", "17")
from_address = Address("325689", "г.Краснодар", "ул.Сормовская", "17", "6")
mailing = Mailing("123GH", from_address, to_address, 150)

print(mailing)


#Распечатайте в консоль отправление в формате:
# Отправление <track>
# из <индекс>, <город>, <улица>, <дом> - <квартира>
# в <индекс>, <город>, <улица>, <дом> -<квартира>.
# Стоимость <стоимость> рублей.
