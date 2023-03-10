def compare_prices(sheety_cities_list, flights_dict):
    """This function compares the provided tequila flight prices to the prices listed
     in Google Sheet 'Flight Deals' and returns a dictionary that contains all the cheap flights
     and returns a dictionary of the good deals"""

    best_deals_dict = {}
    for city in sheety_cities_list:
        city_name = city["city"]
        # getting the lowest flight price found using tequila
        cheapest_price_found = flights_dict[city_name]["price"]
        # getting the lowest flight price listed in the Google sheet
        desired_price = city["lowestPrice"]

        flight_details = flights_dict[city_name]["flight_details"]
        fr = str(flight_details["local_departure"]).split("T")[0]
        to = str(flight_details["local_arrival"]).split("T")[0]

        # comparing the prices
        if cheapest_price_found <= desired_price:
            # adding the good deals to the dictionary
            best_deals_dict[city_name] = {
                "destination": city_name,
                "price": cheapest_price_found,
                "flight_num": flights_dict[city_name]["flight_num"],
                "from": fr,
                "to": to,
                "flight_details": flight_details,
            }
    return best_deals_dict


class FlightData:
    """This class compares the provided tequila flight prices to the prices listed
     in Google Sheet 'Flight Deals' and returns a dictionary that contains all the cheap flights"""
    def __init__(self, sheety_cities_list: list, flights_dict: dict):
        self.best_deals_dict = compare_prices(sheety_cities_list, flights_dict)
        self.there_is_good_deals = False
        self.check_good_deals()

    def check_good_deals(self):
        """THis function changes the variable 'self.there_is_good_deals' to 'True' if there is good deals"""
        if self.best_deals_dict == {}:
            pass
        else:
            self.there_is_good_deals = True
