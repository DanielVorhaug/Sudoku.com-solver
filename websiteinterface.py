import pyautogui
import win32api
import win32con
import keyboard
import time
from PIL import Image
from pytesseract import *


pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"


pixelX_offset = 26      # X-coordinate of top-left corner of sudoku
pixelY_offset = 262     # Y-coordinate of top-left corner of sudoku
square_side = 65        # Width of a square in the sudoku

# Coorinates of the "new game" buttons
new_game_btn_1_X = 850
new_game_btn_1_Y = 172
new_game_btn_2_X = 770
new_game_btn_2_Y = 320


def read_from_webpage():
    image_of_sudoku = pyautogui.screenshot(
        region=(pixelX_offset, pixelY_offset, square_side*9, square_side*9))

    sudoku = [[None for i in range(9)] for j in range(9)]

    for x in range(9):
        for y in range(9):
            sudoku[y][x] = which_number_in_square(
                image_of_sudoku, x * square_side, y * square_side, square_side)

    return sudoku


def which_number_in_square(image_of_sudoku, pixelX, pixelY, square_side):

    for number in range(9, 0, -1):

        numImg = Image.open("Number_pictures\\" + str(number) + ".png")

        if (pyautogui.locate(numImg, image_of_sudoku, region=(pixelX, pixelY, square_side, square_side), grayscale=True, confidence=0.76)) != None:
            return number
    return None


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def square_to_pixel_coordinate(squareX, squareY):
    pixelX = int(pixelX_offset + squareX*square_side + square_side/2)
    pixelY = int(pixelY_offset + squareY*square_side + square_side/2)
    return pixelX, pixelY


def fill_square(number, squareX, squareY):
    pixelX, pixelY = square_to_pixel_coordinate(squareX, squareY)
    click(pixelX, pixelY)
    keyboard.press_and_release(str(number))
    time.sleep(0.05)


def new_game():
    click(new_game_btn_1_X, new_game_btn_1_Y)
    time.sleep(0.5)
    click(new_game_btn_2_X, new_game_btn_2_Y)
    time.sleep(2)


# def execute_list_of_changes(list_of_changes):
#     for change in list_of_changes:
#         fill_square(change[0], change[1], change[2])
