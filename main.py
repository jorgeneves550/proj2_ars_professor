def on_button_pressed_a():
    radio.send_value("ambAula", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("ambAula", 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global numAleatorio
    numAleatorio = randint(1, totalAlunos)
    basic.show_number(numAleatorio)
    radio.send_value("alunoAlt", numAleatorio)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_received_value(name, value):
    global alunoLed, linha, coluna
    alunoLed = value - 1
    linha = int(alunoLed / 5)
    coluna = alunoLed % 5
    if name == "A":
        led.plot(linha, coluna)
        music.play(music.tone_playable(784, music.beat(BeatFraction.SIXTEENTH)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        led.unplot(linha, coluna)
radio.on_received_value(on_received_value)

coluna = 0
linha = 0
alunoLed = 0
numAleatorio = 0
totalAlunos = 0
radio.set_group(1)
totalAlunos = 3