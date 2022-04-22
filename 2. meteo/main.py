import requests
s_city="Moscow,RU"
appid="02ae04b25a2f13d1de8b31ae2f7a9b1a"
varia=0
while varia!=int(1) and varia!=int(2):
    varia=int(input("Выберите прогноз погоды:\n1. Сейчас.\n2. На неделю.\n"))
if varia==1:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Город:", s_city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'],"градусов Цельсия")
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])
    print("Видимость:", data['visibility'],"метров")
    print("Скорость ветра:",data['wind']['speed'],"м/с")
else:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
 
    print("Прогноз погоды на 5 дней:")
    for i in data['list']:
        print("Дата <", i['dt_txt'], "> \r\nТемпература: ",
        '{0:+3.0f}'.format(i['main']['temp']), "градусов Цельсия\r\nПогодные условия <",
        i['weather'][0]['description'], "> \r\nВидимость:",i["visibility"]," метров. \r\nСкорость ветра:",i["wind"]["speed"]," м/с")
        print("____________________________")