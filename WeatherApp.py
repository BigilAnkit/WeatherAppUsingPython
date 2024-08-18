import requests
import json
import pyttsx3

engine = pyttsx3.init()
city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=667403063f0b48b0928113604241808&q={city}"

r = requests.get(url)
# print(r.text)
# print(type(r.text))

wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
print(wdic["current"]["cloud"])
# engine.say(f"{city}")
engine.say(f"{city}temperature{wdic["current"]["temp_c"]}")
engine.say(f"cloude{wdic["current"]["cloud"]}")
engine.runAndWait()
