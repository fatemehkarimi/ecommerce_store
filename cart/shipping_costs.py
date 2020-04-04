from decimal import Decimal

city_cost ={
    'isfahan': Decimal(0),
    'tehran': Decimal(10.00),
    'mashhad': Decimal(12.5),
    'shiraz': Decimal(7.5),
}

def get_city_cost(city_name):
    return city_cost.get(city_name.lower(), Decimal(15))