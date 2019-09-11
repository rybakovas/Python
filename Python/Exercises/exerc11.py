# Task
# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters,
# digits, lowercase and uppercase characters.
# Input Format
# A single line containing a string S.
# Output Format
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

s = input()
check2 = []
item1 = []
item2 = []
item3 = []
item4 = []
item5 = []
i = 0
for element in s:
    check = [element.isalnum(), element.isalpha(), element.isdigit(), element.islower(), element.isupper()]
    check2.append(check)

for element in check2:
    item1.append(element[0])
    item2.append(element[1])
    item3.append(element[2])
    item4.append(element[3])
    item5.append(element[4])

print(any(item1))
print(any(item2))
print(any(item3))
print(any(item4))
print(any(item5))