import requests   # this is for API.

url = "https://api.restful-api.dev/objects"

# response = requests.get(url)

# # result = response.json() #prints the whole json file sent by client.
# result = response.status_code

# print(result) 

api_key = "5884440b902ad1a0c3c69286352c34ee"

city_name = "Bangalore"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response= requests.get(url)
# print(response.json())

#print(response.json() ['main']['temp']) * 9/5 + 32  #pulling just the temperature information.
if response.status_code == 200: 
    temperature = int(response.json()['main']['temp'] - 273);
    print(f"{temperature} degree celsius")
else:
    print("Invalid request")