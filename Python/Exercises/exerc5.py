#  Remove the duplicate itens in a list

numbers = [1, 4, 3, 2, 1, 5, 4, 10]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor

