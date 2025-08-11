from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+7(995)9876543"),
    Smartphone("Apple", "iPhone 15", "+7(900)8891234"),
    Smartphone("Xiaomi", "14", "+7(950)3457698"),
    Smartphone("Huawei", "Pura 70 Pro+", "+7(920)4086734"),
    Smartphone("Google", "Pixel 8 Pro", "+7(915)6784513"),
    Smartphone("Motorola", "Edge 40 Neo", "+7(901)3459087")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.subscrider_number}")