# Dictionary is Store the information for a key; Jan is a key, and can be anything

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions)
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a Valid Key!"))
print("===================================")

customer = {
    "name": "Victor Rybakovas",
    "age": 30,
    "is_verified": True

}
print(customer["name"])
customer["name"] = "Jose da Silva"
print(customer["name"])


phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "☹"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)



# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
