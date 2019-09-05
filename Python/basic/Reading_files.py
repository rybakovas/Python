# Del Comment to test

employee_file = open("employees.txt", "r")  # r read, w write(change), a append (add) at the EOF, r+ Read/writing

#  print(employee_file.readable())  # check if the file is readable True or False
#  print(employee_file.read())  # read all the file
#  print(employee_file.readline())  # read the first the file and if repeat will print the next one
#  print(employee_file.readline())
#  print(employee_file.readlines())  # print each line as array
#  print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # Always closing the file


# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor