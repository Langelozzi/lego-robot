# pip install pynput in terminal

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

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')
# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

