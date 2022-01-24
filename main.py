def on_button_pressed_a():
    pins.analog_write_pin(AnalogPin.P0, 100)
    pins.analog_write_pin(AnalogPin.P1, 1)
    images.create_big_image("""
        . # # # . . . . . .
                # # # # # . . . . .
                . . . # # . . . . .
                # # # # # . . . . .
                . # # # . . . . . .
    """).scroll_image(1, 200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.analog_write_pin(AnalogPin.P0, 100)
    images.create_big_image("""
        . . . # # # . . . .
                . . # # # # # . . .
                . . . . . # # . . .
                . . # # # # # . . .
                . . . # # # . . . .
    """).scroll_image(1, 200)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Wakka")

def on_forever():
    basic.show_icon(IconNames.GHOST)
basic.forever(on_forever)
