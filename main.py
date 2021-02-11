# Welcome to the real world, I hope you'll enjoy it
# author: Steve-P42
# creation date: 2021-02-10 12:47:57
# purpose: initial sequence of The Matrix
# status: in progress
# %%
import os
import ctypes
import msvcrt
import subprocess
import time



# subprocess.Popen('cmd.exe')
#
# from ctypes import wintypes
#
# kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
# user32 = ctypes.WinDLL('user32', use_last_error=True)
#
# SW_MAXIMIZE = 3
#
# kernel32.GetConsoleWindow.restype = wintypes.HWND
# kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
# kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
# user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)
#
#
# def maximize_console(lines=None):
#     fd = os.open('CONOUT$', os.O_RDWR)
#     try:
#         hCon = msvcrt.get_osfhandle(fd)
#         max_size = kernel32.GetLargestConsoleWindowSize(hCon)
#         if max_size.X == 0 and max_size.Y == 0:
#             raise ctypes.WinError(ctypes.get_last_error())
#     finally:
#         os.close(fd)
#     cols = max_size.X
#     hWnd = kernel32.GetConsoleWindow()
#     if cols and hWnd:
#         if lines is None:
#             lines = max_size.Y
#         else:
#             lines = max(min(lines, 9999), max_size.Y)
#         subprocess.check_call('mode.com con cols={} lines={}'.format(
#                                 cols, lines))
#         user32.ShowWindow(hWnd, SW_MAXIMIZE)
#
#
#maximize_console()

time.sleep(5)
print('Wake up, Neo.')
time.sleep(5)


# %%
import os
print('Hello, ' + os.getlogin() + '! How are you?')
# %%
import time
message = 'Wake up, Neo.'
for c in message:
    print(c, end='')
    time.sleep(0.5)



# %%
def mygen():
    x = 20
    yield ("C")
    yield ("G")
    yield ("A " + str(x))
    yield ("T")


gen = mygen()

print(next(gen))


for i in range(10000):
    try:
        print(next(gen), end='')
    except StopIteration:
        pass
        #gen = mygen()
# %%
import time
message = 'Wake up, Neo.'

def my_string_gen():
    for character in message:
        yield character

g = my_string_gen()

while g:
    try:
        print(next(g), end='')
        time.sleep(.1)
        print(next(g), end='')
        time.sleep(.2)
    except StopIteration:
        break

# %% 'Matrix' rain, kind of haha

# for coloring the output on the terminal:
from colorama import init
from termcolor import colored
import random

letters = "!#$%&'() *+,-./0123 456 789:;<=>?@ABCDEFGH IJKLMNOPQRSTUVWXYZ[]^_`abcde fghijklmno pqrstuvwx yz{|}~"

# required initialization for colorama:
init()

for i in range(10000000):
    print(colored(f'{letters[random.randint(0, 98)]}', 'green'), end='')

# %%
