import requests, time, json, base64
from secrets import elevenlabs_key
from overall_imports import open_json, make_json

def use_tts(voice_id, string):
    output_folder = 'dump'
    output_name = str(time.time())
    output_path = f'{output_folder}/{output_name}.mp3'

    data = {
      "text": string,
      "voice_settings": {
        "stability": 0.10,
        "similarity_boost": 0.10,
      }
    }
    headers = {
        "Content-Type": "application/json",
        'xi-api-key': elevenlabs_key,
        }
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    r = requests.request(url=url, data=json.dumps(data), method='post', headers=headers)
    if r.status_code == 200:
        with open(output_path, mode='bx') as f:
            f.write(r.content)
        return output_path
    else:
        print(vars(r))

def get_name_ID_mapping():
    headers = {
        "Content-Type": "application/json",
        'xi-api-key': elevenlabs_key,
        }
    url = 'https://api.elevenlabs.io/v1/voices'
    r = requests.request(url=url, method='get', headers=headers)
    c = r.content
    d = json.loads(c)
    mapping = {}
    for item in d['voices']:
        mapping[item['name']] = item['voice_id']
    return mapping

def get_settings(ID):
    """Returns settings for a single voice."""

    headers = {
        "Content-Type": "application/json",
        'xi-api-key': elevenlabs_key,
        }
    url = f'https://api.elevenlabs.io/v1/voices/{ID}?with_settings=true'
    r = requests.request(url=url, method='get', headers=headers)
    return r.json()

def serialize(d):
    """Helper for the edit_voice function, which uses the f'https://api.elevenlabs.io/v1/voices/{ID}/edit' endpoint."""

    def make_pair(tup):
        return f'"{tup[0]}":"{tup[1]}"'
    return '{' + ', '.join(list(map(make_pair,d.items()))) + '}'

def edit_voice(name, new_settings):
    ID = mapping[name]
    url = f'https://api.elevenlabs.io/v1/voices/{ID}/edit'
    headers = {
        'accept': 'application/json',
        'xi-api-key': elevenlabs_key,
    }
    data = {
        'name':name,
        'labels': serialize(new_settings),
    }
    response = requests.post(url, headers=headers, data=data)
    print('edit_voice response:', response.json())

def get_all_settings():
    """
    Returns a list of dictionaries, each item containing info on one voice.

    dictionary keys:
        name
        id
        settings -- dict
    """

    # get all voice names and ids, then use ids to get settings about each voice.
    ## get api request
    headers = {
        "Content-Type": "application/json",
        'xi-api-key': elevenlabs_key,
        }
    url = 'https://api.elevenlabs.io/v1/voices'
    r = requests.request(url=url, method='get', headers=headers)
    ## parse api request
    c = r.content
    d = json.loads(c)
    info = []
    for item in d['voices']:
        info.append({
            'name':item['name'],
            'id':item['voice_id'],
        })
    ## use ids to get info. (api call to f'https://api.elevenlabs.io/v1/voices/{ID}?with_settings=true' endpoint)
    for n, item in enumerate(info):
        settings = get_settings(item['id'])
        info[n]['settings'] = settings
    return info

