import requests
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

TEQUILA_SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_SEARCH_HEADERS = {
    "apikey": "2PRdq-QcpJSJNN-uffDK-SzkxXdQJRup",
}

now = datetime.now()
six_months = date.today() + relativedelta(months=+6)

tequila_search_parmas = {
    "fly_from": "DAM",
    "fly_to": None,
    "date_from": f"{now.strftime('%d/%m/%Y')}",
    "date_to": f"{six_months.strftime('%d/%m/%Y')}",
}


def find_the_cheapest_flight(cities_list):
    """ This function checks for the cheapest flights from tomorrow to 6 months later
    for all the cities in the provided 'cities_list', using data retrieved from the tequila api"""
    
    cities_cheapest_price_dict = {}
    for city_num in range(len(cities_list)):
        city_code = cities_list[city_num]["iataCode"]
        tequila_search_parmas["fly_to"] = city_code
        tequila_search_response = requests.get(url=TEQUILA_SEARCH_API_ENDPOINT, params=tequila_search_parmas,
                                               headers=TEQUILA_SEARCH_HEADERS)
        city_flights_list = tequila_search_response.json()["data"]
        cheapest_flight_price = city_flights_list[0]["price"]
        cheapest_flight_num = 0
        for flight in city_flights_list:
            if flight["price"] < cheapest_flight_price:
                cheapest_flight_price = flight["price"]
                cheapest_flight_num = city_flights_list.index(flight)

        city_name = tequila_search_response.json()["data"][0]["cityTo"]
        price = cheapest_flight_price
        flight_num = cheapest_flight_num
        cities_cheapest_price_dict[city_name] = {
            "price": price,
            "flight_num": flight_num,
            "flight_details": city_flights_list[flight_num]
        }
    return cities_cheapest_price_dict
        

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, cities_list: list):
        self.cities_cheapest_price_dict = find_the_cheapest_flight(cities_list)
