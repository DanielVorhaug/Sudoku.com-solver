import websiteinterface as web
import sudokusolver as solver
import pyautogui
from PIL import Image
from pytesseract import *
import time
import keyboard

# Make sure this is the same
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

###
### Made to solve sudokus on https://sudoku.com/
### On expert difficulty it typically reads the sudoku in 3 seconds and solves it in around 5.
### Adjusting the constants in websiteinterface.py might be needed to get it to work on other setups.
### Different rendering of the numbers might ruin the number recognition.
### Works in python 3.7.9, had some bugs in the libraries used when in python 3.9
###


def main():
    while keyboard.is_pressed("q") == False:
        print("Reading", end=" ")
        start_time = time.time_ns()
        unsolved_sudoku = web.read_from_webpage()

        print(f"took {(time.time_ns() - start_time)/1000000000} s")
        print("Solving", end=" ")

        start_time = time.time_ns()
        solved_sudoku = [line[:] for line in unsolved_sudoku]
        solved_sudoku = solver.solve(solved_sudoku)

        print(f"took {(time.time_ns() - start_time)/1000000000} s")

        print("Done\n")
        time.sleep(2)
        print("Starting new game")
        web.new_game()


main()
