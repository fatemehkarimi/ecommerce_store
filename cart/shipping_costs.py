city_cost ={
    'isfahan': 0,
    'tehran': 10000,
    'mashhad': 12500,
    'shiraz': 7500
}

def get_city_cost(city_name):
    return city_cost[city_name.lower()]