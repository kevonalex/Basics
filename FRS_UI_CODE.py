# This file demonstrates familiarity with creating class objects, and the
# necessity of using class objects to optimise specific tasks.
import FRS_Intro


class Film(object):
    # constructor - (if no input given calling class will return this information)
    def __init__(self, screen_no=0, title='The Batman', age_restriction=15, runtime=0,
                 rating=8, ):  # sets default film to 'The Batman' with rating'8' and age restriction of '15'
        self.screen = screen_no  # sets screen number
        self.title = title  # sets instance of film title to 'title' input argument
        self.age_restriction = age_restriction  # sets age restriction of film to 15+
        self.runtime = runtime  # sets film runtime in minutes
        self.rating = rating  # sets rating of instance to 8

    # method to edit screen number
    def edit_screen(self, new_screen_no):  # defines method to edit film screen no.
        self.screen = new_screen_no  # sets new screen number to input
        return (self.screen)  # returns the new screen number

    # method to change title
    def edit_title(self, new_title):  # defines method to edit film title
        self.title = new_title  # declares a variable to replace the film title
        return (self.title)  # returns the new film title

    # method to change runtime
    def edit_runtime(self, new_runtime):  # defines method to edit runtime
        self.runtime = new_runtime  # declares a variable to replace the runtime
        return (self.runtime)  # returns the new runtime

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


Film_Ratings = (0, 1, 2, 3, 4, 5)  # lists the potential ratings for a film on a 0-5 scale
Ext_Film_Ratings = Film_Ratings + (6, 7, 8, 9, 10)  # lists the potential ratings for a film on a 6-10 scale

# list of films showing in cinema
film_list = []
film_list.append(['SCREEN NO.', 'TITLE', 'AGE RATING', 'RUNTIME', 'RATING'])
film_list.append([1, 'The Batman', 15, '2hr56mins', 8])
The_Batman = Film([1, 'The Batman', 15, '2hr56mins', 8])
film_list.append([2, 'Fantastic Beasts: The Secrets of Dumbledore', 12, '1hr56mins', 'TBC'])
film_list.append([3, 'Sonic The Hedgehog 2', 'PG', '1hr56', 'TBC'])
film_list.append([4, 'Morbius', 15, '1hr56mins', 'TBC'])
film_list.append([5, 'The Bad Guys', 'U', '1hr56mins', 'TBC'])
film_list.append([6, 'Rabbit Academy', 'U', '1hr56mins', 'TBC'])
film_list.append([7, 'Superworm and Dog', 'U', '1hr56mins', 'TBC'])

#print(User1.age)
FRS_Intro.FRS_RUN()
