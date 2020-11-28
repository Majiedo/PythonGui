import eel
import requests


eel.init('Page')

api_url = "http://api.openweathermap.org/data/2.5/weather?q=Riyadh&appid=7c2b080aa5216618bbe3fe37a386af3a"
res = requests.get(api_url)
output = res.json()

api_url2 = "http://api.openweathermap.org/data/2.5/weather?q=Dubai&appid=7c2b080aa5216618bbe3fe37a386af3a"
res2 = requests.get(api_url2)
output2 = res2.json()

api_url3 = "http://api.openweathermap.org/data/2.5/weather?q=Jeddah&appid=7c2b080aa5216618bbe3fe37a386af3a"
res3 = requests.get(api_url3)
output3 = res3.json()

api_url4 = "http://api.openweathermap.org/data/2.5/weather?q=Egypt&appid=7c2b080aa5216618bbe3fe37a386af3a"
res4 = requests.get(api_url4)
output4 = res4.json()


@eel.expose
def get_weather_egypt():
    city = output4['name']
    return city


@eel.expose
def get_weather_egypt2():
    country = output4['sys']['country']
    return country


@eel.expose
def get_weather_egypt3():
    temp = output4['main']['temp'] - 273.15
    temp2 = int(str(temp)[:2])
    return temp2


@eel.expose
def get_weather_egypt4():
    main = output4['weather'][0]['main']
    return main


@eel.expose
def get_weather_jeddah():
    city = output3['name']
    return city


@eel.expose
def get_weather_jeddah2():
    country = output3['sys']['country']
    return country


@eel.expose
def get_weather_jeddah3():
    temp = output3['main']['temp'] - 273.15
    temp2 = int(str(temp)[:2])
    return temp2


@eel.expose
def get_weather_jeddah4():
    main = output3['weather'][0]['main']
    return main


@eel.expose
def get_weather_dubai():
    city = output2['name']
    return city


@eel.expose
def get_weather_dubai2():
    country = output2['sys']['country']
    return country


@eel.expose
def get_weather_dubai3():
    temp = output2['main']['temp'] - 273.15
    temp2 = int(str(temp)[:2])
    return temp2


@eel.expose
def get_weather_dubai4():
    main = output2['weather'][0]['main']
    return main


@eel.expose
def get_weather_riyadh():
    city = output['name']
    return city


@eel.expose
def get_weather_riyadh2():
    country = output['sys']['country']
    return country


@eel.expose
def get_weather_riyadh3():
    temp = output['main']['temp'] - 273.15
    temp2 = int(str(temp)[:2])
    return temp2


@eel.expose
def get_weather_riyadh4():
    main = output['weather'][0]['main']
    return main


eel.start('index.html', size=(900, 1200))
