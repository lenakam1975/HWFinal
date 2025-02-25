from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy A", "+79231231212"),
    Smartphone("Apple", "Watch Series 10", "+79244565656"),
    Smartphone("Huawei", "Mate 50", "+79137898989"),
    Smartphone("LG", "W41 Plus", "+79837535353"),
    Smartphone("Sony", "Xperia XZ1", "+79849635654")
]

for smartphone in catalog:
    print(f"{smartphone.br} - {smartphone.md}. {smartphone.num}")

