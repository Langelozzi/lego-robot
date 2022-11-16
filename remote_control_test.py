# pip install pynput in terminal
# https://pynput.readthedocs.io/en/latest/keyboard.html

from pynput import mouse, keyboard
from pynput.keyboard import Controller, Key
import time

from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import not_equal_to, greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to
import math

# Objects
hub = MSHub()

# Motors
m_back_right = Motor('A')
m_back_left = Motor('B')
m_front_right = Motor('E')
m_front_left = Motor('F')

back_pair = MotorPair('A', 'B')
front_pair = MotorPair('E', 'F')

keyboard = Controller()

def right_turn():
    front_pair.start(100)

def left_turn():
    front_pair.start(-100)

# Press and release space
with keyboard.press(Key.space):
    front_pair.start(5, 50)
with keyboard.release(Key.space):
    front_pair.stop()

# Press and release shift
with keyboard.press(Key.ctrl):
    right_turn()
with keyboard.release(Key.ctrl):
    front_pair.stop()

with keyboard.press(Key.shift):
    left_turn()
with keyboard.release(Key.shift):
    front_pair.stop()
