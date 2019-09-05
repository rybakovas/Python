# Simulate an ATM System, Cash withdrawal with different bills value
from random import *

bills = (100, 50, 20, 10, 5)
i = 0
p = 0
b = 1
cash = True
sum = 0
billu = []
divlist = []
rangtotal = []
mult = 0

print("==============================================")
print("|| Hello to Rybakovas ATM Withdrawal System ||")
print("==============================================")
try:
    withdrawal = (input("    How much do you want to withdrawal? : R$"))
    if withdrawal[-1] != "0" and withdrawal[-1] != "5":
        raise ValueError
    else:
        withdrawal = int(withdrawal)




    while cash:

        for bill in bills:
            divlist = divmod(withdrawal, bill)

            if divlist[1] != 0 or bill == bills[-1]:
                if divlist[0] == 0:
                    withdrawal = withdrawal - (divlist[0] * bill)
                else:
                    withdrawal = withdrawal - (divlist[0] * bill)
                    print("{} bill {}".format(divlist[0], bill))
                #print(withdrawal)

        #print(withdrawal)
        cash = False

except ValueError:
    print("\nPlease enter a valid value\n"
          "We just have bills of 5, 10, 20, 50 and 100\n"
          "Restart the operation!")

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor