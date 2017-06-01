# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

number_of_guesses = 0
range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, number_of_guesses, range
    print "New game. Range is [0, " + str(range) + ")"
    secret_number = random.randrange (0, range)
    number_of_guesses = int( math.ceil( math.log(range, 2) ) )
    print "Number of remaining guesses is " + str(number_of_guesses)
    print

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, number_of_guesses, range
    range = 100
    secret_number = random.randrange (0, 100)
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, number_of_guesses, range 
    range = 1000
    secret_number = random.randrange (0, 1000)
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was " + str(guess)
    global number_of_guesses
    number_of_guesses -= 1
    
    if (number_of_guesses == 0 and int(guess) != secret_number):
        print "Number of remaining guesses is " + str(number_of_guesses)
        print "You ran out of guesses. The number was " + str(secret_number)
        print
        new_game()
    else:
        if int(guess) > secret_number :
            print "Number of remaining guesses is " + str(number_of_guesses)
            print "Lower!"
            print
        elif int(guess) < secret_number :
            print "Number of remaining guesses is " + str(number_of_guesses)
            print "Higher!"
            print
        else:
            print "Number of remaining guesses is " + str(number_of_guesses)
            print "Correct! "
            print
            new_game()
    
# create frame
f=simplegui.create_frame ( "Guess the number", 200, 200) 

# register event handlers for control elements and start frame
f.add_button ( "Range is [0, 100)", range100, 200)
f.add_button ( "Range is [0, 1000)", range1000, 200)
f.add_input ( "Enter a guess:",input_guess, 200)

# call new_game 
new_game()
f.start()
# always remember to check your completed program against the grading rubric
