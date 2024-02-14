import random
import http.client
import json
from urllib.parse import quote

stocks_data = []


# Initialize jokes
def initStock():
    stocks_data = []
        
# Return weather_data from external api


def getStockAPIData(stocks):
    conn = http.client.HTTPSConnection("api.stocks.com")
    payload = ''
    headers = {}
    encodedStock = quote(stocks)
    conn.request("GET", "/v1/current.json?key=52f6bc918dmshd7d38b943f1d743p199df3jsna0bcad0b8f11" + encodedStock +"&aqi=no", payload, headers)
    res = conn.getresponse()
    data = res.read()
    decodedString = data.decode("utf-8")
    j = json.loads(decodedString)
    temp_f= j['current']["feelslike_f"]
    weatherIcon_url = ""
    if temp_f<=60:
        weatherIcon_url= "https://backend.stu.nighthawkcodingsociety.com/static/assets/cloud_clipart.png"
    elif temp_f < 70 and temp_f>60:
        weatherIcon_url= "https://backend.stu.nighthawkcodingsociety.com/static/assets/partly_sunny.png"
    else:
        weatherIcon_url= "https://backend.stu.nighthawkcodingsociety.com/static/assets/sunny_weather.png"
    print(weatherIcon_url)
    j['current']['weatherIcon_url'] = weatherIcon_url
    return j

# Test Joke Model
if __name__ == "__main__": 
    initStock()  # initialize jokes
    
