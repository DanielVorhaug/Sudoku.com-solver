import pyautogui
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

import sudokureader as reader
import misc


X = 26
Y = 264
square_side = 66



#print(sr.testerino())
nines = pyautogui.locateAllOnScreen("ni.png", grayscale=True, confidence=0.8)



def main():
    unsolved_sudoku = reader.read_from_webpage(X, Y, square_side)
    unsolved_sudoku[1][1] = 2
    misc.printSudoku(unsolved_sudoku)

main()
