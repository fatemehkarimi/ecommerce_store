from decimal import Decimal
from users.models import UserAddress

ADDRESS_ID = 'ADDRESS_ID'

class ShippingCost:
    CITY_COST ={
    'isfahan': Decimal(0),
    'tehran': Decimal(10.00),
    'mashhad': Decimal(12.5),
    'shiraz': Decimal(7.5),
    }

    def get_city_cost(self, city_name):
        return self.CITY_COST.get(city_name.lower(), Decimal(15))
