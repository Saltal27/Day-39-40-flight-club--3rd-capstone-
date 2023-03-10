# This file will need to use the
# DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch(data_manager.sheety_data_list)
print(flight_search.cities_cheapest_price_dict)
