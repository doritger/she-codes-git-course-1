from datetime import datetime
# imports current date and time

def details():
    first_name = input("Please enter your first name: ")
    surname = input("Please enter your surname: ")
    birth_year = input("Please enter the year of your birth: ")
    # asks the user to enter name, surname and year of birth
    print (first_name)
    print (surname)
    print (birth_year)
    # prints the name, surname and year of birth of the user
    currentYear = datetime.now().year
    # calcuates current year
    age = (int (currentYear)) - (int (birth_year))
    # changes the strings 'currentYear' & 'birth_year' to intergals
    # and calcuates the user's age according to current year
    print ("Your initials are " + first_name[0].upper()
           +surname[0].upper() + " and you are " + str (age)
           + " years old.")
    # changes the intergal 'currentYear' to a string
    # and prints the user's initials (first letter of the name & surname)
    # and the user's age
    # .upper() to have the initials in uppercase letters
details()
