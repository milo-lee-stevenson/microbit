work_secs = 5
rest_msecs = 30000

def on_button_pressed_b():
    timer = 0
    for index in range(2):
        basic.show_string("do exercise")
        while timer < work_secs:
            timer += 1
            basic.show_number(timer)
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_string("take a break!!!")
        basic.pause(rest_msecs)
    while timer < work_secs:
        timer += 1
        basic.show_number(timer)
        basic.show_string("ur nice and healthy")

input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("B to start")
