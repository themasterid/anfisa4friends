import requests

ERR_WATHER = '<ошибка на сервере погоды. попробуйте позже>'
ERR_CONNEC = '<сетевая ошибка>'


def what_weather(city):
    weather_parameters = {
        'format': 2,
        'M': ''}
    try:
        response = requests.get(
            f'http://wttr.in/{city}',
            params=weather_parameters)
    except requests.ConnectionError:
        return ERR_CONNEC
    if response.status_code == 200:
        return response.text.strip()
    return ERR_WATHER

def what_temperature(weather):    
    if weather == ERR_CONNEC or weather == ERR_WATHER:
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

def what_conclusion(parsed_temperature):
    try:
        int(parsed_temperature)
        temperature = int(parsed_temperature)
        if temperature < 18:
            return 'Берегись простуды, слишком холодно, не сезон для мороженого!'
        elif  18 <= temperature <= 27:            
            return 'Порция мороженого сейчас будет в самый раз!'
        else:            
            return 'Жарко, как в Африке, нужны две порции!'
    except ValueError:
        return 'Не могу узнать погоду'
