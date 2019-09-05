#  Give the average of n numbers what user whats to put

yes_i_want = True
num = []
result = 0
i = 0

num.insert(i, input("Enter the a number: "))

while yes_i_want:
    i += 1
    num.insert(i, input("Enter the a number: "))
    cont = input("Do you want more numbers? [Y / N]: ")
    if cont in "Yy":
        yes_i_want = True
    else:
        yes_i_want = False


for element in num:
    result += (float(element))


print(result / len(num))

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor