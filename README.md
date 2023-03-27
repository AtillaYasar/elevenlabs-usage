# elevenlabs-usage

## testing
this repo is not fully tested yet (tho mostly). please use with a note in the back of your mind that things may not work.

## things i want

### API related
- easy, clean access to all data, meaning:
  + there is history, voice names, training samples, generated audio and associated text for a voice, settings for a specific audio;
    - i want some representation of data where i can access and search over all of that in an easy way

### general audio related
- crop audios using text
  + get speech tagger, use timestamps to crop
    - OpenAI Whisper is strong, but requires GPU to run
- picking and playing audios from some interface that is good  (as opposed to normal Windows stuff)

### misc
- all this in a nice interface, probably with tkinter.
- not guaranteeing i will do this. this is just what i want.
