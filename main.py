import misc
import websiteinterface as web
import sudokusolver as solver
import pyautogui
from PIL import Image
from pytesseract import *
import time

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"



def main():
    unsolved_sudoku = web.read_from_webpage()

    
    solved_sudoku = [ line[:] for line in unsolved_sudoku ]
    solved_sudoku = solver.solve(solved_sudoku)
    
    #list_of_changes = solver.make_list_of_changes(unsolved_sudoku, solved_sudoku)
    #web.execute_list_of_changes(list_of_changes)



main()
