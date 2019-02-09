"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary
entries. It shows the entry. After the user presses return, the
program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])
    # ask user if they know the definition
    user_input = input('Did you know the definition? Enter y for yes:')
    #if user inputs y then do somthing
    if user_input == 'y':
        #delete card
        del glossary[random_key]
        #print cards remaining, length of dictionary
        print(len(glossary),' cards remain')

# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    if len(glossary) == 0:
        exit = True
    else:
        user_input = input('Enter s to show a flashcard and q to quit: ')
        if user_input == 'q':
            exit = True
        elif user_input == 's':
            show_flashcard()
        else:
            print('You need to enter either q or s.')
                       
