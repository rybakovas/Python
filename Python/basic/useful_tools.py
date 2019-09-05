import random
#  After pip installation we can use docx lib (python-docx)
import docx

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)


def get_emoji(msg):
    words = msg.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
