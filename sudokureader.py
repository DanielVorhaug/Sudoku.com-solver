import pyautogui
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

def testerino():
    img = Image.open("ni.png")
    output = pytesseract.image_to_string(img)

    
    return output



def read_from_webpage(X, Y, square_side):
    sudoku = [[None for i in range(9)] for j in range(9)]

    return sudoku