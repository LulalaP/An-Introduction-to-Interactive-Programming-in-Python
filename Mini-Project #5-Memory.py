# implementation of card game - Memory

import simplegui
import random
numbers = []
exposed = range(16)
ex_ind = [0, 0]
CARD_SIZE = 50
turn = 0

# helper function to initialize globals
def new_game():
    global numbers, state, exposed, turn
    numbers = range(8)
    numbers.extend(range(8))
    random.shuffle(numbers) 
    state = 0
    turn = 0
    label.set_text("Turns = " + str(turn))
    for i in range(len(numbers)):
        exposed[i] = False
        
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global CARD_SIZE, exposed, state, ex_ind, turn
    ind = pos[0] // CARD_SIZE
    if not exposed[ind]:
        exposed[ind] = True
        if state == 0:
            state = 1
            ex_ind[0] = ind
        elif state == 1:
            state = 2
            ex_ind[1] = ind
        else:
            state = 1
            if numbers[ex_ind[0]] != numbers[ex_ind[1]]:
                exposed[ex_ind[0]],exposed[ex_ind[1]] = False, False
            turn += 1
            ex_ind[0] = ind
            label.set_text("Turns = " + str(turn))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers,exposed
    i = 0
    for number in numbers:
        if exposed[i]:
            canvas.draw_text(str(number), [50 * i + 10, 75], 70, 'White')
        else:
            canvas.draw_polygon([(0 + i * 50, 0), (0+ i * 50, 100), (50 + i * 50, 100), (50 + i * 50 , 0)], 2, 'Black','Green')
        i = i + 1
    
    
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
