#ex1: A simple function. Create a simple function called favourite_movie, which takes a string containing the name
#of your favourite movie. The function should then print “My favourite movie is name”.
def myfavorite_movie(movie_name):
    print("My favorite movie is " + '"' + movie_name + '".')
#movie_name = str(input("Please enter the name of the movie you like:"))
#myfavorite_movie(movie_name)
myfavorite_movie("Max&Marry")

#ex2:Creating a dictionary. Create a function called make_country, which takes in a country’s name and
#capital as parameters. Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
#Make the function print out the values of the dictionary to make sure that it works as intended.
def make_country(c_name, c_capital):
    country_info = {}
    country_info['name'] = c_name
    country_info['capital'] = c_capital
    return print(country_info)

make_country('Ukraine', 'Kyiv')

#Ex.3: A simple calculator.Create a function called make_operation, which takes in a simple arithmetic operator
#as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments
#(only numbers) as second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
# For example:
#            the call make_operation(‘+’, 7, 7, 2) should return 16
#            The call make_operation(‘-’, 5, 5, -10, -20) should return 30
#            The call make_operation(‘*’, 7, 6) should return 42
def simple_calc(operation, *args):
    if operation == '+':
        res = sum(i for i in args)
    elif operation == '-':
        li = []
        li = list(args)

    for i in li:
            print(i)

simple_calc('-', 7, 7, 2)