import requests
import json

url = "https://currency-converter241.p.rapidapi.com/convert"

currency_1 = "INR"
currency_2 = "USD"
amount = "1000"


querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
    "x-rapidapi-host": "currency-converter241.p.rapidapi.com",
	"x-rapidapi-key": "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads(response.text)

total_amount = data["total"]
formatted = "{:,.2f}".format(total_amount)

print(formatted)