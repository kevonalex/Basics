# This file demonstrates familiarity with creating class objects, and the
# necessity of using class objects to optimise specific tasks.
import FRS_SCAN_ID
import FRS_Intro
import FRSdatabase
import time
import sqlite3

Film_Ratings = (0, 1, 2, 3, 4, 5)  # lists the potential ratings for a film on a 0-5 scale
Ext_Film_Ratings = Film_Ratings + (6, 7, 8, 9, 10)  # lists the potential ratings for a film on a 6-10 scale



# list of films showing in cinema
film_list = []
film_list.append(['SCREEN NO.', 'TITLE', 'AGE RATING', 'RUNTIME', 'RATING'])
film_list.append([1, 'The Batman', 15, '2hr56mins', 8])
film_list.append([2, 'Fantastic Beasts: The Secrets of Dumbledore', 12, '1hr56mins', 'TBC'])
film_list.append([3, 'Sonic The Hedgehog 2', 'PG', '1hr56', 'TBC'])
film_list.append([4, 'Morbius', 15, '1hr56mins', 'TBC'])
film_list.append([5, 'The Bad Guys', 'U', '1hr56mins', 'TBC'])
film_list.append([6, 'Rabbit Academy', 'U', '1hr56mins', 'TBC'])
film_list.append([7, 'Superworm and Dog', 'U', '1hr56mins', 'TBC'])


class Film(object):
    # constructor - (if no input given calling class will return this information)
    def __init__(self, title='The Batman', age_restriction=15,
                 rating=8):  # sets default film to 'The Batman' with rating'8' and age restriction of '15'
        self.title = title  # sets instance of film title to 'title' input argument
        self.age_restriction = age_restriction  # sets age restriction of film to 15+
        self.rating = rating  # sets rating of instance to 8

    # method to change title
    def edit_title(self, new_title):  # defines method to edit film title
        self.title = new_title  # declares a variable to replace the film title
        return (self.title)  # returns the new film title

    # method to change film rating
    def edit_rating(self, new_rating):  # defines method to edit film's rating
        self.rating = new_rating  # declares a variable to replace the film's previous rating
        return (self.rating)  # returns the new film rating


class Customer(object):
    # constructor
    def __init__(self, first_name='John', last_name='Doe', age=18,
                 film='input'):  # sets placeholder details for customer information
        self.first_name = first_name  # sets instance of customer information to customer input
        self.last_name = last_name  # sets instance of customer information to customer input
        self.age = age  # sets instance of customer information to customer input
        self.film = film  # sets instance of customer's chosen film

    def edit_first_name(self, new_first_name):
        self.first_name = new_first_name
        return (new_first_name)

    def edit_last_name(self, new_last_name):
        self.last_name = new_last_name
        return (new_last_name)

    def scan_age(self, scanned_age):
        self.age = scanned_age
        return (scanned_age)

    def select_film(self, select_film):
        self.film = select_film
        return (select_film)


User1 = Customer() # initialises user

# Required functions:
# 1)FRS_RUN
# 1a)FRS_Intro
# 1b)FRS_Film_Selection
# 1c)FRS_ID_Scan
# 2)FRS_ID SCAN

def FRS_RUN():
    FRS_Intro()

def FRS_Intro():
    print('Welcome! Please enter your first name:')
    User1.edit_first_name(input())
    time.sleep(1)
    print('Thanks! Please enter your last name.')
    time.sleep(1)
    User1.edit_last_name(input())
    print(f'Welcome, {User1.first_name} {User1.last_name}! \nHere are the films currently available for viewing.')
    # displays movies currently showing
    print('NOW SHOWING:\n')
    for i in range(0, 8):
        print(f'{film_list[i]}\n')
    time.sleep(0)
    FRS_Film_Selection()

def FRS_Film_Selection():
    print('Which film would you like to watch?\nPlease select the screen number of the film you would like to watch.')
    Selected_Film = User1.select_film(input())
    Selected_Film = int(Selected_Film)  # converts user input into integer data type for comparison
    time.sleep(0)

    for j in range(0, 7):
        # print(j)
        if Selected_Film == film_list[j][0]:
            print(
                f'You have selected: \"{film_list[j][1]}\".\n Is this correct?\n\nPress \'y\' to continue,or press \'n\' to reselect.')
            selection_confirm = input()
            if selection_confirm == ('y' or 'Y'):
                FRS_SCAN_ID()
                break
            elif selection_confirm == ('n' or 'N'):
                FRS_Film_Selection()
            else:
                print('Please select a valid option.\n')
                FRS_Film_Selection()
    film_list[j][0] = film_list[j + 1][0]

def FRS_SCAN_ID():
    print('To continue, please scan your ID card.')
    User1.scan_age = input()

    if User1.scan_age == 'id':
        print('Processing scan...')
        time.sleep(3)
        print('Thank you. Please provide payment method.')
    else:
        print('Sorry, something went wrong. Please scan your ID again now.')
        FRS_SCAN_ID()

# run program
FRS_RUN()
