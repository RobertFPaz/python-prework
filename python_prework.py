# Question 1
# Write a function to print "hello_USERNAME!"  
# USERNAME is the input of the function. 

def hello_name(user_name):
    message = "hello " + user_name + "!"
    print(message)

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1, 101):
        if number % 2 == 1:
            print(number, end= " ")

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_nun_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
#  alternative solution but demonstrated less comprehension of loops and if statements. 
#  return max(a_list) 



# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if (a_year % 100 == 0) and (a_year % 400 != 0):
            return False
        else:
            return True
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#  The return should be boolean Type.
 
def is_consecutive(a_list):
    if len(a_list) < 2: 
        return False
    for index in range(len(a_list)):
        stop = len(a_list) - 1
        if index < stop:
            num_1 = a_list[index]
            num_2 = a_list[index + 1]
            if num_2 - num_1 != 1:
                return False
    return True
    
my_list = [3,4,5,6,7]
is_consecutive(my_list)




