def hello_message(username):
    return f"Привет, {username}\nЯ бот, который скажет погоду в Бишкеке на сегодня"

def weather_message(d:dict):
    return f"""Сегодня в Бишкеке {d['main']}
Влажность - {d['humidity']}
Температура: {d['temp']} градусов Цельсия
Чувствуется, как: {d['feels_like']} градусов Цельсия
Ветер {d['wind_speed']} м/с
Направление ветра {d['wind_deg']} градусов"""
