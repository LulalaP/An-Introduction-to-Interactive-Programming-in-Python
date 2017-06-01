# template for "Stopwatch: The Game"

import simplegui

# define global variables
total_tick = 0
total_stops = 0
successful_stops = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(total_tick):
    D = total_tick % 10
    C = ( total_tick - D ) / 10 % 10
    B = ( total_tick - D - C * 10 ) /100 % 6
    A = ( ( total_tick - D - C * 10 ) / 100 - B )/6
    return str(A) + ':' + str(B) + str(C) + '.' + str(D) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start() :
    timer.start()
    global is_running
    is_running = True

def stop() :
    timer.stop()
    global successful_stops, total_stops, is_running
    if is_running == True:
        if total_tick % 10 == 0:
            successful_stops = successful_stops + 1
        total_stops = total_stops + 1
    is_running = False
    
def reset() :
    global total_tick, successful_stops, total_stops, is_running
    total_tick = 0
    successful_stops = 0
    total_stops = 0
    timer.stop()
    is_running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global total_tick
    total_tick = total_tick + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(total_tick), [80, 160], 60, 'White')
    canvas.draw_text(str(successful_stops) + '/' + str(total_stops),[240,40], 40, "White")
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 300,300)
timer = simplegui.create_timer(100, tick)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
