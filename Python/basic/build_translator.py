# change all vowel we will change for g
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))


def translate2(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate2(input("Enter a phrase: ")))


def translate3(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate3(input("Enter a phrase: ")))

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor