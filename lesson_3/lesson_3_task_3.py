from address import Address
from mailing import Mailing

to_address = Address("123456", "Voronez", "Antokolskogo", "4", "60")
from_address = Address("456789", "Yalta", "Timiryazeva", "14", "51")
mailing = Mailing(to_address, from_address, "30000", "156")

print(mailing)