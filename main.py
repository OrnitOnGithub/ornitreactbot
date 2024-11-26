import os
from gtts import gTTS
import random

def betterchoice(options, previous_choice_skip_count, buffer):
    """
    Like random.choic()) but won't pick the last X choices twice.
    """
    # How many choices to remember not to pick them again
    # Holds previous choices
    length = len(options) -1
    number = 0
    while True:
        number = random.randint(0, length)
        if number not in buffer:
            buffer.append(number)
            if len(buffer) > previous_choice_skip_count:
                buffer.pop(0)
            break
    return options[number]

ascii_dog_thing_1 = "\
⠀⠀⢀⡞⠐⣦⣀⣰⡏⠢⡀⠀⠀⣀⡤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⢸⠀⠈⠛⠤⠈⠁⠀⠈⠖⠋⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⠘⡄⣠⢤⡄⠀⠀⡀⢀⡀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⢰⠻⢣⣾⠇⠀⠘⠇⣾⡗⠀⠀⡧⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⠰⣀⠀⠉⣁⠀⠀⠀⠈⠁⠀⠀⠹⡋⠀⠀⠀⠀⢀⡀⠀⠀⠀\n\
⠀⠀⠀⠈⢛⡒⠉⠙⠁⠀⠀⠶⣿⠏⠋⠁⠀⠀⠀⠀⡸⢳⠀⡿⡀\n\
⣠⠤⠒⠚⣹⣋⡀⣠⠄⠀⠀⢔⠛⠂⠀⠀⠀⠀⠀⣰⠁⠀⡞⠀⡆\n\
⠧⢀⣀⠤⠖⣺⠞⠁⠀⠀⠀⠈⠣⡀⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⡅\n\
⠀⠀⠀⠀⠸⣄⣀⣠⠔⠃⠀⠀⠀⢹⠁⠀⠀⠀⠀⠀⠀⠀⢀⡼⠀\n\
⠀⠀⠀⠀⢠⠇⠀⠀⠀⣀⢠⠀⠀⢸⡀⠀⠀⠀⠀⠀⢠⣴⣿⠀⠀\n\
⠀⠀⠀⠀⠸⠀⠀⠀⡼⠀⡜⠀⠀⠘⡗⠤⠀⠀⠠⠤⠚⠋⠁⠀⠀\n\
⠀⠀⠀⠀⠸⡀⠀⠀⠘⡀⡇⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠀⢱⡀⠀⣀⠃⠈⢦⡀⣠⠶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"

ascii_dog_thing_2 = "\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠠⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
⡴⠒⠒⠒⠒⠒⠶⠦⠄⢹⣄⠀⠀⠑⠄⣀⡠⠤⠴⠒⠒⠒⠀⠀\n\
⢇⠀⠀⠀⠀⠀⠀⠐⠋⠀⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀\n\
⠈⢆⠀⠀⠀⠀⡤⠤⣄⠀⠀⠀⠀⡤⠤⢄⠀⠀⠀⠀⠀⣠⠃⠀\n\
⠀⡀⠑⢄⡀⡜⠀⡜⠉⡆⠀⠀⠀⡎⠙⡄⠳⡀⢀⣀⣜⠁⠀⠀\n\
⠀⠹⣍⠑⠀⡇⠀⢣⣰⠁⠀⠀⠀⠱⣠⠃⠀⡇⠁⣠⠞⠀⠀⠀\n\
⠀⠀⠀⡇⠔⣦⠀⠀⠀⠈⣉⣀⡀⠀⠀⠰⠶⠖⠘⢧⠀⠀⠀⠀\n\
⠀⠀⠰⠤⠐⠤⣀⡀⠀⠈⠑⣄⡁⠀⡀⣀⠴⠒⠀⠒⠃⠀⠀⠀\n\
⠀⠀⠀⠀⠀⠀⠘⢯⡉⠁⠀⠀⠀⠀⠉⢆⠀⠀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠀⠀⢀⣞⡄⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀\n\
\n\
\n\
\n"

ascii_dog_thing_3 = "\
⠀⠀⠀⠰⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⡄⠀⠀⠀\n\
⠀⠀⠀⡇⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠁⠀⢡⠀⠀\n\
⠀⠀⢰⠁⠀⠀⠀⠑⢄⠀⠏⠐⠠⢀⠀⢀⠎⠀⠀⠀⠀⢸⠀⠀\n\
⠀⠀⢸⠀⠀⠀⠀⠀⢀⡡⠼⠀⠀⠀⠈⠪⠀⠀⠀⠀⠀⠘⡀⠀\n\
⠀⠀⢸⠀⠀⠀⠀⠀⠉⠁⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀\n\
⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⡰⠀⠀\n\
⠀⠠⡀⢑⣄⢠⠁⢸⣿⣿⡇⠀⠀⠀⣿⣿⠇⠈⡄⠀⠴⠤⡄⠀\n\
⠀⠀⠈⢠⠀⢸⡀⠀⠻⠟⠀⠀⠀⠀⠙⠛⠀⢀⢇⠀⡄⠃⠀⠀\n\
⠀⠀⠀⡌⠐⠙⠈⠀⠀⠠⣄⡰⠤⠤⠂⠀⠀⠘⠁⠀⠘⡄⠀⠀\n\
⠀⠀⠀⠉⠉⠁⠒⡠⣄⣀⠀⠀⠀⠀⠀⠠⡄⠒⠀⠀⠉⠀⠀⠀\n\
⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠑⡀⠀⠀⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠀⠀⠀⠒⠓⠆⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀\n\
\n"

speech_bubble_bottom = ".,______________,.\n\
     \\|"
speech_bubble_top = ",.--------------.,"

# Read the phrase file
file = open("phrases.txt", "r")
lines = file.readlines()
# Clear the terminal

buffer_1 = []
buffer_2 = []
while True:
    # Wait until input (it blinks by the way)
    input("\033[5mPress enter for a reaction: \033[0m")
    print("\033[2J")
    # Pick a phrase
    mytext = betterchoice(lines, 10, buffer_1)
    # Get google TTS to say it
    language = 'en'
    file = "speech.mp3"
    speech = gTTS(text=mytext, lang=language, slow=False)
    # Save it to a file
    speech.save(file)
    # Display random shit
    print("\n" + speech_bubble_top)
    print(f'\033[31;3m{mytext[:-1]}\033[0m')
    print(speech_bubble_bottom)
    print(betterchoice([ascii_dog_thing_1, ascii_dog_thing_2, ascii_dog_thing_3], 1, buffer_2))
    # Run command to play the file
    os.system("afplay " + file)
    # Remove the file.
    os.system("rm " + file)
