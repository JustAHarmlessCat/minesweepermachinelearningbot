import pyautogui
import keyboard
import torch
import time
import random

from screeninfo import get_monitors
pyautogui.PAUSE = 0.001


flags = []
monitor = get_monitors()[0]

def boardSize():
    img = pyautogui.screenshot(region=(0, 0, monitor.width, monitor.height))
    pixel = img.getpixel((470, 240))
    if img.getpixel((1200, 300)) == (0, 0, 0):
        return 9
    if pixel == (112, 128, 144):
        return 30
    else:
        return 16

colors = {
    (54, 75, 165): 1,
    (47, 147, 82): 2,
    (175, 44, 44): 3,
    (137, 54, 165): 4,
    (110, 58, 58): 5,
    (86, 156, 184): 6, 
    (48, 89, 105): 7,
    (98, 120, 142): 20, # 20 is nothing, so the grey
    (112, 128, 144): 9, # 9 is unclicked
}

cols = boardSize()
rows = 16
if cols == 9:
    rows = 9

def makeBoard(): 
    print("Making board...")
    board = []
    for _ in range(cols):
        col = [0] * rows
        board.append(col)
    print("Board made.")
    return board

def updateBoard(board):
    img = pyautogui.screenshot(region=(0, 0, monitor.width, monitor.height))  
    for i in range(len(board)):
        for j in range(len(board[i])):
            x, y = startpointx + fieldsize * i, startpointy + fieldsize * j
            pixel = img.getpixel((x, y))
          
            wert = colors.get(pixel)
            if wert is not None:
                board[i][j] = wert
            else:
                board = 0
                return board
    return board
            
            

board = makeBoard()

board = makeBoard()

resolution = monitor.width, monitor.height

if resolution == (2560, 1440):
    fieldsize = 56
    if cols == 30:
        startpointx = 444
        startpointy = 237
    elif cols == 16:
        startpointx = 840
        startpointy = 240
    else:
        startpointx = 1031
        startpointy = 438
else: 
    fieldsize = 42
    startpointx = 333
    startpointy = 177

print("Starting...")
pyautogui.click(1282, 665)
board = updateBoard(board)
while True:
    if keyboard.is_pressed('q'):
        print("Stopping...")
        break
    if keyboard.is_pressed('r') or board == 0:
        print("Restarting...")
        pyautogui.keyDown('ctrl')
        pyautogui.keyUp('ctrl')
        pyautogui.click(1282, 665)
        board = makeBoard()
        flags = []
    if board != 0:
        board = updateBoard(board)