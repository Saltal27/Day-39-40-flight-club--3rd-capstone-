import smtplib

MY_EMAIL = "pythontest32288@gmail.com"
MY_PASSWORD = "gsrfzucledwimgqp"


def send_cheap_flights_mail(best_deals_dict):
    """THis function sends Alert emails if there is good deals"""
    for city in best_deals_dict:
        price = best_deals_dict[city]["price"]
        destination = best_deals_dict[city]["destination"]
        fr = best_deals_dict[city]["from"]
        to = best_deals_dict[city]["to"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="omarmobarak53@gmail.com",
                msg=f"Subject: LOW PRICE ALERT!\n\n"
                    f"Only ${price} to fly from Beirut to {destination},"
                    f"from: {fr}, to: {to}"
            )


class NotificationManager:
    """THis class sends Alert emails if there is good deals"""
    def __init__(self, there_is_good_deals: bool, best_deals_dict: dict):
        if there_is_good_deals:
            send_cheap_flights_mail(best_deals_dict)
