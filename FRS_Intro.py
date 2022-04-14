
import time
import FRS_SCAN_ID

def FRS_RUN():
    FRS_Intro()

def FRS_Intro():
    User1 = Customer('Name', 'Surname', 18, 'Film')
    print('Welcome! Please enter your first name:')
    User1.edit_first_name(input())
    time.sleep(1)
    print('Thanks! Please enter your last name.')
    time.sleep(1)
    User1.edit_last_name(input())
    print(f'Welcome, {User1.first_name} {User1.last_name}! \nHere are the films currently available for viewing.')
    # displays movies currently showing
    print('NOW SHOWING:\n')
    for i in range (0,8):
        print(f'{film_list[i]}\n')
    time.sleep(0)
    print('\n\n')
    FRS_Film_Selection()

def FRS_Film_Selection():
    print('Which film would you like to watch?\nPlease select the screen number of the film you would like to watch.')
    Selected_Film = User1.select_film(input())
    Selected_Film=int(Selected_Film) # converts user input into integer data type for comparison
    time.sleep(0)

    for j in range (0,7):
        # print(j)
        if Selected_Film == film_list[j][0]:
            print(f'You have selected: \"{film_list[j][1]}\".\n Is this correct?\n\nPress \'y\' to continue,or press \'n\' to reselect.')
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


