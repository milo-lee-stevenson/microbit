from microbit import *

neutral_emoji = Image("99099:"
                      "99099:"
                      "00000:"
                      "09990:"
                      "00000")

happy_emoji = Image("99099:"
                    "99099:"
                    "90009:"
                    "09990:"
                    "00000")
       
sad_emoji = Image("99099:"
                  "99099:"
                  "00000:"
                  "09990:"
                  "90009")               

emojis = [neutral_emoji, happy_emoji, sad_emoji]

current_emoji_index = 0

while True:
    if button_a.was_pressed():
        current_emoji = emojis.pop(current_emoji_index)
        display.show(current_emoji)
        emojis.insert(current_emoji_index, current_emoji)
        if current_emoji_index == len(emojis) - 1:
            current_emoji_index = 0
        else:
            current_emoji_index = current_emoji_index + 1
