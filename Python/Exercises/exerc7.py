if __name__ == '__main__':
    n = int(input())
i = 0
numbers = []
result = ""
for i in range(n):
    numbers.append(i + 1)
    i += 1
i = 0
for number in numbers:
    result = result + str(numbers[i])
    i += 1

print(result)

# Read an integer N.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the values in between.
# Input Format
# The first line contains an integer n.
# Output Format:
# Output the answer as explained in the task.
# Sample Input 0
# 3
# Sample Output 0
# 123

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor