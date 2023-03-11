from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# ---------------------------- FILLING IATA CODES IN GOOGLE SHEET ------------------------------- #
data_manager = DataManager()

# ---------------------------- SEARCHING FOR THE CHEAPEST FLIGHTS ------------------------------- #
flight_search = FlightSearch(data_manager.sheety_cities_list)
# print(data_manager.sheety_cities_list)
# print(flight_search.cities_cheapest_flight_dict)

# -------------------- COMPARING THE CHEAPEST FLIGHT WITH THE LOWEST PRICE ----------------------- #
flight_data = FlightData(data_manager.sheety_cities_list, flight_search.cities_cheapest_flight_dict)
print(flight_data.there_is_good_deals)
print(data_manager.customers_list)

# ---------------------------- SENDING ALERT EMAILS ------------------------------- #
notification_manager = NotificationManager(flight_data.there_is_good_deals,
                                           flight_data.best_deals_dict, data_manager.customers_list)
