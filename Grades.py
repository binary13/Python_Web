from statistics import *
#from bs4 import *

admins = {'user1':'passw123@'}


def main():
    print("""
        Welcome to Grade Central

        [1] Enter Grades
        [2] Add a Student
        [3] Remove a Student
        [4] Print Average Grades
        [5] Exit
    """)

    option = input('What would you like to do today? (Enter a number: )')

    if option == '1':
        print('1')
    elif option == '2':
        print('2')
    elif option == '3':
        print('3')
    elif option == '4':
        print('4')
    elif option == '5':
        print("Exiting the program!")
    else:
        print('Invalid input, try again.')


user = input('Enter username: ')
passw = input('Enter password: ')

if user in admins:
    if admins[user] == passw:
        print("Welcome, ", user, "!")
        while True:
            main()
    else: print("Invalid password.")
else: print("Invalid username.")
