# elevenlabs-usage

## warning
this repo is not fully tested yet (tho mostly). please use with a note in the back of your mind that things may not work, to protect against disappointment.


## index, the juice, the point
```
crop an audio:
  crop.py

download gen history:
  download_history.py

generate and download audio:
  eleven_labs.py -> use_tts(voice_id, string)

get voice ID for each name:
  eleven_labs.py -> get_name_ID_mapping()

get settings for a given voice ID:
  eleven_labs.py -> get_settings(ID)

get settings for each voice:
  eleven_labs.py -> get_all_settings()

edit a voice's labels and settings:
  eleven_labs.py -> edit_voice(name, new_settings)
```

## things i want

### API related
- easy, clean access to all data, meaning:
  + there is history, voice names, training samples, generated audio and associated text for a voice, settings for a specific audio;
    - i want some representation of data where i can access and search over all of that in an easy way

### general audio related
- crop audios using text
  + get speech tagger, use timestamps to crop
    - OpenAI Whisper is strong, but requires GPU to run
- picking and playing audios with some interface that is good  (as opposed to normal Windows stuff)

### misc
- all this in a nice interface, probably with tkinter.
- not guaranteeing i will do this. this is just what i want.
