

def printSudoku(sudoku):
    fulline = "-------------------------\n"
    output = fulline
    for c in range(3):
        for l in range(3):
            for ch in range(3):
                output += "| "
                for lh in range(3):
                    if sudoku[(c)*3+l][(ch)*3+lh] == None:
                        output += "  "
                    else:
                        output += str(sudoku[(c)*3+l][(ch)*3+lh]) + " "
            output += "|\n"
        output += fulline
    print(output[:-1])