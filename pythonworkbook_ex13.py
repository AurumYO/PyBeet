#Ex13:Making Change. Consider software that runs on a self-checkout machine. One task that it must be able to perform
# is to determine how much change to provide when the shopper pays for a purchase with cash.
#Write a program that begins by reading a number of cents from the user as an integer.
# Then your program should compute and display the denominations of the coins that should be used to give that amount
# of change to the shopper. The change should be given using as few coins as possible. Assume that the machine is loaded
#with pennies, nickels, dimes, quarters, loonies and toonies.
#A one dollar coin was introduced in Canada in 1987 == loonie. The two dollar coin == toonie
#MY SOLUTION
cash_in = float(input("Please enter your amount of payment in cash: "))
cash_cent = int(cash_in*100)
print(cash_cent)
cent, nickel, dime, quarter, loonie, toonie = 1, 5, 10, 25, 100, 200

print ("Solution number 1:")
def cash_t (cash_cent):
    if cash_cent >= toonie:
        cash_toonie = int(cash_cent / toonie)
        remainder = cash_cent - (cash_toonie * toonie)
        return cash_toonie, remainder;
    else:
        cash_toonie = 0
        remainder = cash_cent
        return cash_toonie, remainder;
cash_toonie, remainder1 = cash_t(cash_cent)
def cash_l (remainder1):
    if remainder1 >= loonie:
        cash_loonie = int(remainder1 / loonie)
        remainder = remainder1 - (cash_loonie * loonie)
        return cash_loonie, remainder;
    else:
        cash_loonie = 0
        remainder = remainder1
        return cash_loonie, remainder;
cash_loonie, remainder2 = cash_l(remainder1)
def cash_q (remainder2):
    if remainder2 >= quarter:
        cash_quarter = int(remainder2 / quarter)
        remainder = remainder2 - (cash_quarter * quarter)
        return cash_quarter, remainder;
    else:
        cash_quarter = 0
        remainder = remainder2
        return cash_quarter, remainder;
cash_quarter, remainder3 = cash_q(remainder2)
def cash_d (remainder3):
    if remainder3 >= dime:
        cash_dime = int(remainder3 / dime)
        remainder = remainder3 - (cash_dime * dime)
        return cash_dime, remainder;
    else:
        cash_dime = 0
        remainder = remainder3
        return cash_dime, remainder;
cash_dime, remainder4 = cash_d(remainder3)
def cash_n (remainder4):
    if remainder4 >= nickel:
        cash_nickel = int(remainder4 / nickel)
        remainder = remainder4 - (cash_nickel * nickel)
        return cash_nickel, remainder;
    else:
        cash_nickel = 0
        remainder = remainder4
        return cash_nickel, remainder;
cash_nickel, remainder5 = cash_n(remainder4)
def cash_c (remainder5):
    if remainder5 >= cent:
        cash_cen = int(remainder5 / cent)
        return cash_cen
    else:
        cash_cen = 0
        return cash_cen
cash_cen = cash_c(remainder5)
print("Please, recieve your change:\n", cash_toonie, cash_loonie, cash_quarter, cash_dime, cash_nickel,cash_cen)

print ("Solution number 2:")
cash_toonies = cash_cent // toonie
rem1 = cash_cent  - (cash_toonies * toonie)
cash_loonies = rem1 // loonie
rem2 = rem1 - (cash_loonies * loonie)
cash_quarters = rem2 // quarter
rem3 = rem2 - (cash_quarters * quarter)
cash_dimes = rem3 // dime
rem4 = rem3 - (cash_dimes * dime)
cash_nickels = rem4 // nickel
rem5 = rem4 - (cash_nickels * nickel)
cash_cents = rem5 // cent
change_li = [cash_toonies, cash_loonies, cash_quarters,cash_dimes,cash_nickels,cash_cents]
#gives change
print("Please take your change:")
if change_li[0] > 0 :
    print(change_li[0], "toonies")
if change_li[1] > 0:
    print(change_li[1], "loonies")
if change_li[2] > 0:
    print(change_li[2], "quarters")
if change_li[3] > 0:
    print(change_li[3], "dimes")
if change_li[4] > 0:
    print(change_li[4], "nickels")
if change_li[5] > 0:
    print(change_li[5], "cents")

print ("Solution from Python Workbook:")
#Compute the minimum collection of coins needed to represent a number of coins
cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarters = 25
cents_per_dime = 10
cents_per_nickle = 5
#Read the number of cents from user
cents = int(input("Please enter the number of cents: "))
#Determine the number of toonies by performing an integer division by 200. Than compute
#the amount of change that still needs to be concidered by computing the remainder
#after deviding by 200
print(" ", cash_cent // cents_per_toonie, "toonies")
cents = cash_cent % cents_per_toonie

#repeat process for loonies, quarters, dimes and nickels
print(" ", cents // cents_per_loonie, "loonies")
cents = cents % cents_per_loonie

print(" ", cents // cents_per_quarters, "quarters")
cents = cents % cents_per_quarters

print(" ", cents // cents_per_dime, "dimes")
cents = cents % cents_per_dime

print(" ", cent // cents_per_nickle, "nickels")
cents = cent % cents_per_nickle
print(cents) # QUESTION = why the result is '1"?????

#display the number of pennies
print(" ", cents, "pennies")