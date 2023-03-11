import requests

TEQUILA_LOCATIONS_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_LOCATIONS_HEADERS = {
    "apikey": "2PRdq-QcpJSJNN-uffDK-SzkxXdQJRup",
}
GET_SHEETY_PRICES_URL = "https://api.sheety.co/6c032614643505580fd6287f06c112a2/flightDeals/prices"
GET_SHEETY_USERS_URL = "https://api.sheety.co/6c032614643505580fd6287f06c112a2/flightDeals/users"

tequila_locations_parmas = {
    "term": None,
    "location_types": "city",
}


def fill_iata_codes():
    """This function checks your Google Sheet 'FLIGHT DEALS', and fills the empty 'IATA Code' cells with data
    retrieved from the tequila api"""

    # getting sheety prices data
    get_sheety_prices_response = requests.get(url=GET_SHEETY_PRICES_URL)
    # print(get_sheety_prices_response.text)
    sheety_data_list = get_sheety_prices_response.json()["prices"]

    for city_num in range(len(sheety_data_list)):
        # acquiring each city name
        city_name = sheety_data_list[city_num]["city"]
        # replacing the 'term' in tequila parmas with the city name
        tequila_locations_parmas["term"] = city_name

        # getting the tequila data correspondent to the city name
        tequila_response = requests.get(url=TEQUILA_LOCATIONS_API_ENDPOINT, params=tequila_locations_parmas,
                                        headers=TEQUILA_LOCATIONS_HEADERS)
        # acquiring the city code
        city_code = tequila_response.json()["locations"][0]["code"]

        # inserting the city code in its cell if it's empty
        if sheety_data_list[city_num]["iataCode"] == "":
            row_num = city_num + 2
            edit_sheety_url = \
                f"https://api.sheety.co/6f99efa404162352318a74763b1e629c/flightDeals/prices/{row_num}"
            edit_sheety_body = {
                "price": {
                    "iataCode": city_code,
                }
            }
            edit_sheety_response = requests.put(url=edit_sheety_url, json=edit_sheety_body)


class DataManager:
    """This class checks your Google Sheet 'FLIGHT DEALS', and fills the empty 'IATA Code' cells with data
    retrieved from the tequila api"""
    def __init__(self):
        fill_iata_codes()
        get_sheety_response = requests.get(url=GET_SHEETY_PRICES_URL)
        self.sheety_data = get_sheety_response.json()
        self.sheety_cities_list = self.sheety_data["prices"]
        self.customers_list = []
        self.get_customers_data()

    def get_customers_data(self):
        # getting sheety users data
        get_sheety_users_response = requests.get(url=GET_SHEETY_USERS_URL)
        # print(get_sheety_users_response.text)
        sheety_users_list = get_sheety_users_response.json()["users"]
        self.customers_list = sheety_users_list
