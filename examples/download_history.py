import requests
from secrets import elevenlabs_key
import json, os, time, base64, sys, rich
from overall_imports import *

def download_history_item(item_id):
    """Download a single history item."""

    url = f'https://api.elevenlabs.io/v1/history/download'
    headers = {
        'Content-Type': 'application/json',
        'xi-api-key': elevenlabs_key,
    }
    data = {
        "history_item_ids": [
            item_id,
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    out_path = time.time()+'.mp3'
    with open(out_path, mode='bx') as f:
        f.write(response.content)

def get_full_history():
    """Get the full gen history's info. (not download)"""

    url = 'https://api.elevenlabs.io/v1/history'
    headers = {
        'xi-api-key': elevenlabs_key,
    }
    response = requests.get(url, headers=headers)
    response_b = response.content
    decoded = json.loads(response_b)
    return decoded['history']

def download_full_history():
    """Downloads the full generation history as a zip."""

    # get item ids, using v1/history endpoint
    history = get_full_history()
    all_items = [item['history_item_id'] for item in history]

    url = f'https://api.elevenlabs.io/v1/history/download'
    headers = {
        'Content-Type': 'application/json',
        'xi-api-key': elevenlabs_key,
    }
    data = {
        "history_item_ids": [
            *all_items
        ]
    }
    # get path
    if 'history.zip' not in os.listdir():
        out_path = 'history.zip'
    else:
        out_path = 'hist_' + str(time.time()) + '.zip'
    # download
    response = requests.post(url, headers=headers, data=json.dumps(data))
    with open(out_path, mode='bx') as f:
        f.write(response.content)

download_full_history()