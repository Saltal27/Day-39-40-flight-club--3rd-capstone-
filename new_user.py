import requests

USERS_SHEETY_POST_API_ENDPOINT = "https://api.sheety.co/6f99efa404162352318a74763b1e629c/flightDeals/users"

print("Welcome to Omar's flight club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_verification = input("Type your email again:\n")

match = False
while not match:
    if email == email_verification:
        print("You're in the club!")
        match = True
    else:
        print("the two emails you entered doesn't match.")
        email_verification = input("Type your email again:\n")

users_sheety_post_body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}

sheety_response = requests.post(url=USERS_SHEETY_POST_API_ENDPOINT, json=users_sheety_post_body)
# print(sheety_response.status_code)
