import requests
import json

API_KEY = '22909732ad99c8ca2f1d382efbf03ed4'


def get_weather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    response = requests.get(url).json()
    weather_info = response.get('main')
    pressure = weather_info.get('pressure')
    humidity = weather_info.get('humidity')
    temp = weather_info.get('temp')
    desc = f'''    Weather in {city_name}
    Temperature: {temp}
    Humidity: {humidity}
    Pressure: {pressure}
    '''
    print(desc)


def rick_morty_characters(name=None, status=None, species=None, type=None, gender=None):
    url = 'https://rickandmortyapi.com/api/character'
    params = []
    if name:
        params.append(f'name={name}')
    if status:
        params.append(f'status={status}')
    if species:
        params.append(f'species={species}')
    if type:
        params.append(f'type={type}')
    if gender:
        params.append(f'gender={gender}')

    if len(params) != 0:
        url += '/?' + '&'.join(params)

    response = requests.get(url).json()
    info = response.get('info')
    results = response.get('results')
    if info:
        print('Basic info about your request')
        print(json.dumps(info, indent=4))
        print('Exist characters on first page')
        names = [p['name'] for p in results]
        print(names)
    else:
        print('There arent any character with this parameters')


def rick_morty_locations(id):
    url = f'https://rickandmortyapi.com/api/location/{id}'
    response = requests.get(url)
    print(f'Location ID: {id}')
    print(f"Name of location: {response.json().get('name')}")
    print(f"Type of location: {response.json().get('type')}")
    print(f"Dimension of location: {response.json().get('dimension')}")


def rick_morty_episodes(id):
    url = f'https://rickandmortyapi.com/api/episode/{id}'
    response = requests.get(url)
    episode_id = response.json().get('episode')
    print(f'Episode ID: {id} / {episode_id}')
    print(f"Name of episode: {response.json().get('name')}")
    print(f"Air date of episode: {response.json().get('air_date')}")
    print(f"The number of characters: {len(response.json().get('characters'))}")


if __name__ == "__main__":
    get_weather('Moscow')
    rick_morty_characters(gender='Male', species='Human', type='Genetic experiment', status='unknown')
    rick_morty_characters(gender='Female', status='dead', species='Alien')
    rick_morty_locations(10)
    rick_morty_episodes(30)