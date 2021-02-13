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
# maximize_console()

time.sleep(2)

#%%
message = 'Wake up, Neo...'
message2 = 'The Matrix has you...'
message3 = 'Follow the white rabbit.'
message4 = 'Knock, knock, Neo.'

for c in message:
    print(c, end='')
    time.sleep(0.1)

time.sleep(4)


def my_string_gen():
    for character in message2:
        yield character


g = my_string_gen()

print(" ", end="\r", flush=True)

while g:
    try:
        print(next(g), end='')
        time.sleep(.2)
        print(next(g), end='')
        time.sleep(.4)
        print(next(g), end='')
        time.sleep(.1)
    except StopIteration:
        break

time.sleep(3)

print(" ", end="\r", flush=True)

for c in message3:
    print(c, end='')
    time.sleep(0.1)

time.sleep(3)

print(" ", end="\r", flush=True)

print(message4)

time.sleep(5)
# %% 'Matrix' rain, kind of haha

# for coloring the output on the terminal:
from colorama import init
from termcolor import colored
import random

letters = "!#$%&'() *+,-./0123 456 789:;<=>?@ABCDEFGH IJKLMNOPQRSTUVWXYZ[]^_`abcde fghijklmno pqrstuvwx yz{|}~"

# required initialization for colorama:
init()

for i in range(200000):
    print(colored(f'{letters[random.randint(0, 98)]}', 'green'), end='')


print(colored(' System Failure ', None, 'on_green', ['bold']))



# %% since a multisensory experience adds to the immersion, we will also add some sound :D
# %% further libraries required
# pip install pafy
# pip install python-vlc
# pip install youtube-dl


import vlc
import pafy
url = "https://www.youtube.com/watch?v=4lzqUe1Qfec&ab_channel=RATMVEVO"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()

time.sleep(365)  # length of track

