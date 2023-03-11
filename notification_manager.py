import smtplib

MY_EMAIL = "pythontest32288@gmail.com"
MY_PASSWORD = "gsrfzucledwimgqp"


def send_cheap_flights_mail(best_deals_dict, users_list):
    """THis function sends Alert emails if there is good deals"""
    for city in best_deals_dict:
        price = best_deals_dict[city]["price"]
        destination = best_deals_dict[city]["destination"]
        fr = best_deals_dict[city]["from"]
        to = best_deals_dict[city]["to"]
        stop_overs_num = best_deals_dict[city]["stop_overs_num"]
        stop_over_city = best_deals_dict[city]["stop_overs_city"]
        origin_airport_iata = best_deals_dict[city]["origin_airport_iata"]
        destination_airport_iata = best_deals_dict[city]["destination_airport_iata"]

        for user in users_list:
            user_email = user['email']
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            if stop_overs_num == 0:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user_email,
                    msg=f"Subject: LOW PRICE ALERT!\n\n"
                        f"Only ${price} to fly from Beirut directly to {destination},"
                        f"from: {fr}, to: {to}\n"
                        f"https://www.google.com/flights?hl=en#flt="
                        f"{origin_airport_iata}.{destination_airport_iata}."
                        f"{fr}*{destination_airport_iata}.{origin_airport_iata}.{to}"
                )
                # print(f"Subject: LOW PRICE ALERT!\n\n"
                #       f"Only ${price} to fly from Beirut directly to {destination},"
                #       f"from: {fr}, to: {to}\n"
                #       f"https://www.google.com/flights?hl=en#flt="
                #       f"{origin_airport_iata}.{destination_airport_iata}."
                #       f"{fr}*{destination_airport_iata}.{origin_airport_iata}.{to}"
                #       )
            else:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user_email,
                    msg=f"Subject: LOW PRICE ALERT!\n\n"
                        f"Only ${price} to fly from Beirut to {destination},"
                        f"from: {fr}, to: {to}\n"
                        f"Flight has {stop_overs_num} stop over, via {stop_over_city} City.\n"
                        f"https://www.google.com/flights?hl=en#flt="
                        f"{origin_airport_iata}.{destination_airport_iata}."
                        f"{fr}*{destination_airport_iata}.{origin_airport_iata}.{to}"
                )
                # print(f"Subject: LOW PRICE ALERT!\n\n"
                #       f"Only ${price} to fly from Beirut to {destination},"
                #       f"from: {fr}, to: {to}\n"
                #       f"Flight has {stop_overs_num} stop over, via {stop_over_city} City.\n"
                #       f"https://www.google.com/flights?hl=en#flt="
                #       f"{origin_airport_iata}.{destination_airport_iata}."
                #       f"{fr}*{destination_airport_iata}.{origin_airport_iata}.{to}"
                #       )


class NotificationManager:
    """THis class sends Alert emails if there is good deals"""

    def __init__(self, there_is_good_deals: bool, best_deals_dict: dict, users_list: list):
        if there_is_good_deals:
            send_cheap_flights_mail(best_deals_dict, users_list)
