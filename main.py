# Welcome to the real world, I hope you'll enjoy it!
# author: Steve-P42
# creation date: 2021-02-10 12:47:57
# purpose: initial sequence of a scene in The Matrix, when Trinity contacts Neo
# status: done
# %% ########### Imports ########### - START
# required for setting the terminal to fullscreen (only necessary if you crate a standalone exe)
import os  # also for getting the username
import ctypes
import msvcrt
import subprocess
# for sleep functionality
import time
# for coloring the output on the terminal:
from colorama import init
from termcolor import colored
import random

# further libraries required
# pip install pafy
# pip install python-vlc
# pip install youtube-dl
import vlc
import pafy
# %% ########### Imports ########### - END


# ######## Setting cmd to fullscreen ######### - START
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
# ######## Setting cmd to fullscreen ######### - END

# ######## main section for the messages ###################### - START
# waiting two seconds for the text sequence to start, there are various sleep statements following
time.sleep(2)

# messages to show to the user, which can be renamed:
name = os.getlogin().upper()
# name = 'Neo'

message = f'Wake up, {name}...'
message2 = 'The Matrix has you...'
message3 = 'Follow the white rabbit.'
message4 = f'Knock, knock, {name}.'

print('', end='')

# first message appears
for c in message:
    print(c, end='')
    time.sleep(0.1)

time.sleep(4)


# generator function for the next message, to make it look more like being typed in real time
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

# third message
for c in message3:
    print(c, end='')
    time.sleep(0.1)

time.sleep(3)

print(" ", end="\r", flush=True)

# forth message
print(message4)
# ######## main section for the messages ###################### - END

time.sleep(5)


# ######## 'Matrix' rain, kind of haha ############ - START
# letters to be displayed
letters = "!#$%&'() *+,-./0123 456 789:;<=>?@ABCDEFGH IJKLMNOPQRSTUVWXYZ[]^_`abcde fghijklmno pqrstuvwx yz{|}~"

# required initialization for colorama:
init()

# dependent on number of loops, duration of rain
for i in range(1000000):
    print(colored(f'{letters[random.randint(0, 98)]}', 'green'), end='')


print(' ', colored(' System Failure ', None, 'on_green', ['bold']))


# ###### Audio - Section ##### - START
# %% since a multisensory experience adds to the immersion, we will also add some sound :D

url = "https://www.youtube.com/watch?v=4lzqUe1Qfec&ab_channel=RATMVEVO"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()
# ###### Audio - Section ##### - END

# keep the terminal open until the track is done
time.sleep(365)  # length of track



