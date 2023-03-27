sound_path = r'C:\Users\Gebruiker\Desktop\tts\dump\1679921949.7926407.mp3'

# 0 for vlc, 1 for pygame, 2 for pygame+tkinter
example_n = 0

# with vlc
if example_n == 0:
    import vlc, time

    p = vlc.MediaPlayer(sound_path)
    p.play()
    time.sleep(10)
# with pygame
elif example_n == 1:
    import time
    from pygame import mixer  # Load the popular external library
    mixer.init()
    mixer.music.load(sound_path)
    mixer.music.play()
    time.sleep(10)
# with pygame + tkinter
elif example_n == 2:
    # Import the required libraries
    from tkinter import *
    import pygame
    from PIL import Image, ImageTk

    # Create an instance of tkinter frame or window
    win = Tk()

    # Set the size of the window
    win.geometry("700x500")

    # Add a background image

    label = Label(win)
    label.place(x=0, y=0)

    # Initialize mixer module in pygame
    pygame.mixer.init()
    # Define a function to play the music
    def play_sound():
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

    # Add a Button widget
    b1 = Button(win, text="Play Music", command=play_sound)
    b1.pack(pady=60)

    win.mainloop()

