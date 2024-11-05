#!/usr/bin/python3
from gpiozero import Button
import pyautogui as gui

class KeyHandler:
    def __init__(self, _pin, _output):
        self.output = _output
        self.button = Button(_pin)

    def Handle(self):
        if self.button.is_pressed:
            gui.keyDown(self.output)
        if self.button.is_released:
            gui.keyDown(self.output)


k1 = KeyHandler(4, 'q')
k2 = KeyHandler(17, 'w')
k3 = KeyHandler(18, 'a')
k4 = KeyHandler(27, 's')
k5 = KeyHandler(22, 'z')
k6 = KeyHandler(23, 'x')
k7 = KeyHandler(24, 'k')

keys = [k1, k2, k3, k4, k5, k6, k7]

while 1:
    for item in keys:
        item.Handle()
