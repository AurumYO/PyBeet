# #EX 1: program displays your name and complete mailing address formatted in
# #the manner that you would usually see it on the outside of an envelope. Your program
# #does not need to read any input from the user.
#print("""Yurii Osadchyi
#PJSC SEB CORPORATE BANK
#7 Mykhailivska str.
#Kyiv city
#01001
#Ukraine""")

## #Ex2: program that asks to enter name. The program should
## respond with a message that says hello to the user, using his or her name
#name = input("Please enter your name here: ")
#print("Hello, ", name,"!", sep='')

##Ex.3: Area of a Room. Program asks user enter the width and length of a room.
## program should compute and display the area of the room.
## The length and the width will be entered as floating point numbers. Include
#units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with.
#r_len = float(input("Please enter the length of the room in meters: "))
#r_width = float(input("Please enter the width of the room in meters: "))
#print("The area of the room with length {0} meters and width {1} meters is {2} square meters.".format(r_len, r_width, r_len * r_width))

##Ex4: Area of a Field. Create a program that reads the length and width of a farmer’s field from the user in
##feet. Display the area of the field in acres.
#f_length = int(input("Please enter the length of the farmer's field in feet: "))
#f_width = int(input("Please enter the width of the farmer's field in feet: "))
#field_area = float((f_length * f_width)/43560)
#print("The area of the farmer's field with length of {0} feet and width of {1} feet is {2:1.2f} acres!".format(f_length, f_width, field_area), sep='')

##Ex5: Bottle Deposits. drink containers holding one liter or less have a $0.10 deposit, and drink containers
# holding more than one liter have a $0.25 deposit. Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.
#cont_small = int(input("Enter the number of small drink containers you want to return (1 liter or less): "))
#cont_big = int(input("Enter the number of big drink containers you want to return (more than 1 liter): "))
#deposit_refund = float((cont_small*0.10)+(cont_big*0.25))
#print("Your refund for {0} small containers and {1} big containres is ${2:1.2f}.".format(cont_small, cont_big, deposit_refund))

##Exercise 6: Tax and Tip. The program will begin by reading the cost of a meal from the user.
# Then program will compute the tax and tip for the meal (22% tax rate, tip as 18% percent of the meal (without the taxa).
# The output from program should include the tax amount, the tip amount, and the grand total for
#the meal including both the tax and the tip. Format the output so that all of the values displayed using two decimal places.
#meal = float(input("Enter the cost of your meal: "))
#tax = meal * 0.22
#tip = (meal - tax) * 0.18
#gr_total = meal + tax + tip
#print("Your meal cost: {0:1.2f} for the meal, plus {1:1.2f} fof tax, plus {2:1.2f} of tips.And the Grand total for the meal is {3:1.2f}"
#      .format(meal, tax, tip, gr_total))

##Ex7: Sum of the First n Positive Integers.Write a program that reads a positive integer, n, from the user and displays the
##sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed using the formula:
## s = ((n *(n+1))/2
#n = int(input("Please enter positive integer: "))
#s = int(((n)*(n+1))/2)
#print("The sum of all integers from 1 to",n,"is",s,".")

##Ex8: Widgets and Gizmos. retailer sells two products: widgets and gizmos. Each widget weighs 75 gr.
## each gizmo weighs 112 gr. Write a program that reads the number of widgets and gizmos in an order from the user.
## Then program should compute and display the total weight of the order.
#widgets = int(input("Please enter the number of Widgets you'd like to order: "))
#gizmos = int(input("Please enter the number of Gizmos you'd like to order: "))
#weight_widgets = widgets * 75
#weight_gizmos = gizmos * 112
#tot_order = weight_widgets + weight_gizmos
#print("The total weight of your order  is",tot_order,"grams")

##Ex9:Compound Interest. Pretend you have just opened a new savings account that earns 4% per year. Interest  you earn is
##paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading
##the amount of money deposited into the account from the user. Then your program should compute and display the amount
##in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.
#deposit = float(input("Please enter the amount of the deposit you would like to place under 4% per year: "))
#interest = 1.04
#savacc_y1 = deposit * interest
#savacc_y2 = savacc_y1 * interest
#savacc_y3 = savacc_y2 * interest
#print("The balance of your savings account as of the end of the first year will be {0:1.2f}".format(savacc_y1))
#print("The balance of your savings account as of the end of the second year will be {0:1.2f}".format(savacc_y2))
#print("The balance of your savings account as of the end of the third year will be {0:1.2f}".format(savacc_y3))

##Ex10: Arithmetic. Create program that reads two int, a and b, from user. program should compute and display:
##The sum of a and b
##The difference when b is subtracted from a
##The product of a and b
##The quotient when a is divided by b
##The remainder when a is divided by b
##The result of log10 a
##The result of a
import math
a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
print("The sum of the",a,"and",b,"is",a+b,".")
print("The difference between",a,"and",b,"is",a-b,".")
print("The product of",a,"and",b,"is",a * b,".")
print("The quotient if ",a,"devided by ",b," is ",a // b,".", sep="")
print("The remainder if ",a," devided by ",b," is ",a % b,".", sep="")
print("The log10 of ",a," is ",math.log10(a),".", sep="")
print("The result of ",a," in power of ",b, " is ",math.pow(a,b) ,".", sep="")