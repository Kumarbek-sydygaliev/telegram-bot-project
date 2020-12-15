def translite(d:dict): # Мини переводчик
    if d['main'] == 'Mist':
        d['main'] = 'туман'
    elif d['main'] == 'Smoke':
        d['main'] = 'смог'
    elif d['main'] == 'Fog':
        d['main'] = 'туман и дым'
    elif d['main'] == 'Snow':
        d['main'] = 'снег'
    elif d['main'] == 'Rain':
        d['main'] = 'дождь'
    elif d['main'] == 'Clear':
        d['main'] = 'ясно'

    if d['name'] == 'Bishkek':
        d['name'] = 'Бишкек'
    elif d['name'] == 'Osh Oblasty':
        d['name'] = 'Ош'
    elif d['name'] == 'Talas':
        d['name'] = 'Талас'

    return d


def reformat_weather(dicts):
    params = {
        'main': dicts['weather'][0]['main'],
        'description': dicts['weather'][0]['description'],
        'humidity': dicts['main']['humidity'],
        'temp': dicts['main']['temp'],
        'feels_like': dicts['main']['feels_like'],
        'wind_speed': dicts['wind']['speed'],
        'wind_deg': dicts['wind']['deg'],
        'name': dicts['name']}

    return translite(params)

