#You are given a space separated list of integers.
# If all the integers are positive, then you need to check if any integer is a palindromic integer.
# Input Format
#
# The first line contains an integer N.N is the total number of integers in the list.
# The second line contains the space separated list of N integers.
# Output Format
# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

n = int(input())
numbers = []
list_int = input()
palindromic = False
positive = True
for number in list_int.split():
    number = int(number)
    if number < 0:
        positive = False
        break

    number = str(number)
    xnumber = number[::-1]

    if number == xnumber:
        palindromic = True
    numbers.append(number)

x = all([n > 0, n < 100, n == len(numbers), palindromic, positive])
print(x)


# Sample Input
#
# 5
# 12 9 61 5 14
# Sample output
# True

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
