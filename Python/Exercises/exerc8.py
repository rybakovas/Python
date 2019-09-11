# You are given a spreadsheet that contains a list of  athletes and their details
# (such as age, height, weight and so on).
# You are required to sort the data based on the th attribute and print the final resulting table.
# Input Format
#
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
# Output Format
#
# Print the N lines of the sorted table. Each line should contain the space separated elements.

from operator import itemgetter

N, M = map(int, input().split())

lst = [[int(i) for i in input().split()] for _ in range(N)]

for i in sorted(lst, key=itemgetter(int(input()))):
    print(*i)

# Sample Input
#
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
