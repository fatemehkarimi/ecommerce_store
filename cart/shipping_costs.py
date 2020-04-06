from decimal import Decimal
from users.models import UserAddress

class ShippingCost:
    CITY_COST ={
    'isfahan': Decimal(0),
    'tehran': Decimal(10.00),
    'mashhad': Decimal(12.5),
    'shiraz': Decimal(7.5),
    }

    def __init__(self, ship_address_id=None):
        if ship_address_id:
            self.address = UserAddress.objects.get(pk=ship_address_id)
        else:
            self.address = None

    def change_ship_adderss(self, address_id):
        self.address = UserAddress.objects.get(pk=address_id)
        
    def get_city_cost(self):
        if self.address is None:
            return Decimal(15)
        return self.CITY_COST.get(self.address.city.lower(), Decimal(15))
