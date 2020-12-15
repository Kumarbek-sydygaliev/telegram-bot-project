def hello_message(username):
    return f"Привет, {username}\nЯ бот, который скажет погоду на сегодня"

def weather_message(d:dict):
    return f"""Сегодня в городе {d['name']} {d['main']}
Влажность - {d['humidity']}
Температура: {d['temp']}'C
Чувствуется, как: {d['feels_like']}'C
Ветер {d['wind_speed']} м/с
Направление ветра {d['wind_deg']} градусов"""
