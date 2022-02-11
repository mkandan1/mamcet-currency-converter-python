import requests

api_link = 'https://v6.exchangerate-api.com/v6/API_KEY/latest/'

From = input("Convert from (From): ").upper()
api = api_link + From

response = requests.get(api)
data = response.json()   
    
currency = input("Convert to (TO): ").upper()
if currency in data['conversion_rates']:
    user_Input = float(input("Enter ammount: "))
    total = data['conversion_rates'][currency] * user_Input
    print("\nCurrency Exchange Rate")
    print("-----------------------\n")
    print(From, user_Input)
    print(currency,format(total, '.2f'))
else:
    print("We don't have this type of Currency data or Invalid")
