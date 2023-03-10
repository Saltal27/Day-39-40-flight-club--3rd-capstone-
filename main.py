# This file will need to use the
# DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch(data_manager.sheety_data_list)
# print(data_manager.sheety_data_list)
# print(flight_search.cities_cheapest_price_dict)
flight_data = FlightData(data_manager.sheety_data_list, flight_search.cities_cheapest_price_dict)
# print(flight_data.there_is_good_deals)
notification_manager = NotificationManager(flight_data.there_is_good_deals,
                                           flight_data.best_deals_dict)
