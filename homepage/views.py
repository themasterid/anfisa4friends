from anfisa.models import friends_db
from anfisa.services import what_conclusion, what_temperature, what_weather
from django.shortcuts import render
from icecream.models import icecream_db


def index(request):
    icecreams = ''
    city_weather = ''
    friend_output = ''
    selected_icecream = ''
    conclusion = ''

    friends = ''.join(
        f'<input type="radio" name="friend" required value="{friend}">{friend}<br>'
        for friend in friends_db
    )
    for i in range(len(icecream_db)):
        ice_form = (f'<input type="radio" name="icecream" required'
                    f' value="{icecream_db[i]["name"]}">{icecream_db[i]["name"]}')

        ice_link = f'<a href="icecream/{i}/">Узнать состав</a>'
        icecreams += f'{ice_form} | {ice_link} <br>'

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        selected_icecream = request.POST['icecream']
        city = friends_db[selected_friend]
        weather = what_weather(city)
        parsed_temperature = what_temperature(weather)
        conclusion = what_conclusion(parsed_temperature)
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        city_weather = f'В городе {city} погода: {weather}'

    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
        'conclusion': conclusion,}
    return render(request, 'homepage/index.html', context)
