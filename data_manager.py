import requests

TEQUILA_LOCATIONS_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_LOCATIONS_HEADERS = {
    "apikey": "2PRdq-QcpJSJNN-uffDK-SzkxXdQJRup",
}
GET_SHEETY_URL = "https://api.sheety.co/6f99efa404162352318a74763b1e629c/flightDeals/prices"

tequila_locations_parmas = {
    "term": None,
    "location_types": "city",
}


def fill_iata_codes():
    """ This function checks your Google sheet 'FLIGHT DEALS', and fills the empty 'IATA Code' cells with data
    retrieved from the tequila api"""

    get_sheety_response = requests.get(url=GET_SHEETY_URL)
    sheety_data_list = get_sheety_response.json()["prices"]
    for city_num in range(len(sheety_data_list)):
        city_name = sheety_data_list[city_num]["city"]
        tequila_locations_parmas["term"] = city_name

        tequila_response = requests.get(url=TEQUILA_LOCATIONS_API_ENDPOINT, params=tequila_locations_parmas,
                                        headers=TEQUILA_LOCATIONS_HEADERS)
        city_code = tequila_response.json()["locations"][0]["code"]
        if sheety_data_list[city_num]["iataCode"] == "":
            row_num = city_num + 2
            edit_sheety_url = \
                f"https://api.sheety.co/6f99efa404162352318a74763b1e629c/flightDeals/prices/{row_num}"
            edit_sheety_body = {
                "price": {
                    "iataCode": city_code,
                }
            }
            post_sheety_response = requests.put(url=edit_sheety_url, json=edit_sheety_body)
            print(post_sheety_response.text)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        fill_iata_codes()


data_manager = DataManager()
