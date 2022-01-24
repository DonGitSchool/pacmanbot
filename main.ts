input.onButtonPressed(Button.A, function () {
    pins.analogWritePin(AnalogPin.P0, 100)
    pins.analogWritePin(AnalogPin.P1, 1)
    images.createBigImage(`
        . # # # . . . . . .
        # # # # # . . . . .
        . . . # # . . . . .
        # # # # # . . . . .
        . # # # . . . . . .
        `).scrollImage(1, 200)
})
input.onButtonPressed(Button.AB, function () {
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.analogWritePin(AnalogPin.P0, 100)
    images.createBigImage(`
        . . . # # # . . . .
        . . # # # # # . . .
        . . . . . # # . . .
        . . # # # # # . . .
        . . . # # # . . . .
        `).scrollImage(1, 200)
})
basic.showString("Wakka")
basic.forever(function () {
    basic.showIcon(IconNames.Ghost)
})
