
def compare_prices(sheety_cities_list, flights_dict):
    """This function compares the provided tequila flight prices to the prices listed
     in Google Sheet 'Flight Deals' and returns a dictionary that contains all the cheap flights"""

    best_deals_dict = {}
    for city in sheety_cities_list:
        city_name = city["city"]
        cheapest_price_found = flights_dict[city_name]["price"]
        desired_price = city["lowestPrice"]

        if cheapest_price_found <= desired_price:
            best_deals_dict[city_name] = {
                "destination": city_name,
                "price": cheapest_price_found,
                "flight_num": flights_dict[city_name]["flight_num"],
                "from": flights_dict[city_name]["flight_details"]["local_departure"],
                "to": flights_dict[city_name]["flight_details"]["local_arrival"],
                # "flight_details": flights_dict[city_name]["flight_details"],
            }
    return best_deals_dict


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, sheety_cities_list: list, flights_dict: dict):
        self.best_deals_dict = compare_prices(sheety_cities_list, flights_dict)
        self.there_is_good_deals = False
        self.check_good_deals()

    def check_good_deals(self):
        if self.best_deals_dict == {}:
            pass
        else:
            self.there_is_good_deals = True
