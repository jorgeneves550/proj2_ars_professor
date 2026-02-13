input.onButtonPressed(Button.A, function () {
    radio.sendValue("ambAula", 1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendValue("ambAula", 2)
})
input.onGesture(Gesture.Shake, function () {
    numAleatorio = randint(1, totalAlunos)
    basic.showNumber(numAleatorio)
    radio.sendValue("alunoAlt", numAleatorio)
    basic.clearScreen()
})
radio.onReceivedValue(function (name, value) {
    alunoLed = value - 1
    linha = Math.trunc(alunoLed / 5)
    coluna = alunoLed % 5
    if (name == "A") {
        led.plot(linha, coluna)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
    } else {
        led.unplot(linha, coluna)
    }
})
let coluna = 0
let linha = 0
let alunoLed = 0
let numAleatorio = 0
let totalAlunos = 0
radio.setGroup(1)
totalAlunos = 3
