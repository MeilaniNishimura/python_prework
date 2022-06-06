# Question 1 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of code has been defined as: def hello_name(user_name):

def hello_name(user_name):
        """Display a greeting to user."""
        print("Hello " + user_name + "!")
hello_name("")

# Question 2
# Write a python function, first_odds that prints the odd number from 1-100 and returns nothing.

def first_odds():
    """Print odd numbers 1-100"""
    for number in range(1,100):
        if number % 2 == 1:
                print(number)
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Return the max number of a given list"""
    for number in a_list:
        if number == max(a_list):
                print(number)

max_num_in_list([1,2,3,14])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless is it also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Determine if given year is a leap year."""
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year())

# Question 5
# Write a function to see if all numbers in list are consecutive numbers. The return should be boolean Type,

def is_consecutive(a_list):
    """Determine whether a list of numbers is consecutive."""  
    sorted_list= sorted(a_list)
    if max(sorted_list)-min(sorted_list) == len(sorted_list)+1:
        return True
    else:
        return False

print(is_consecutive())





        

