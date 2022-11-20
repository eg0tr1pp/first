import requests

city = "Moscow, RU"
appid = "3e3d75cbea9e15fc7f2ade92e03d045f"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("____________________________")
print("Москва:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'], "метров в секунду")
print("Видимость:", data['visibility'], "метров")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("____________________________")
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <<", i['dt_txt'], ">> \r\nТемпература <<",
          '{0:+3.0f}'.format(i['main']['temp']), ">> \r\nПогодные условия <<",
          i['weather'][0]['description'], ">> \r\nСкорость ветра <<",
          i['wind']['speed'], "метров в секунду", ">> \r\nВидимость <<",
          i['visibility'], "метров", ">>")
print("____________________________")
