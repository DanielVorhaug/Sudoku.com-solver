import websiteinterface as web

def solve(sudoku):
    sudoku = logicsolve(sudoku, True)

    if not sudoku_is_solved(sudoku):
        sudoku = guessolve(sudoku)

    return sudoku


def logicsolve(sudoku, fill_continously):
    while not sudoku_is_solved(sudoku):
        a_square_has_been_filled = False

        for y in range(9):
            for x in range(9):
                if sudoku[y][x] == None:
                    number = can_only_one_number_can_be_in_square(sudoku, x, y)
                    if number:
                        sudoku[y][x] = number
                        #print_sudoku(sudoku)
                        if fill_continously:
                            web.fill_square(number, x, y)
                        a_square_has_been_filled = True

        if not a_square_has_been_filled:
            break
    return sudoku


def guessolve(sudoku):
    unsolved_sudoku = [ line[:] for line in sudoku ]

    sudoku = add_possible_numbers(sudoku)
    
    print(sudoku)

    return unsolved_sudoku



def add_possible_numbers(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == None: 
                sudoku[y][x] = numbers_that_can_be_in_square(sudoku, x, y)
    return sudoku



def sudoku_is_solved(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[y][x] == None:
                return False
    return True


def can_only_one_number_can_be_in_square(sudoku, squareX, squareY):
    numbers = numbers_that_can_be_in_square(sudoku, squareX, squareY)
    if len(numbers) == 1:
        return numbers[0]
    else:
        return 0

def numbers_that_can_be_in_square(sudoku, squareX, squareY):
    numbers = []
    for number in range(1, 10):
        if number_can_be_in_square(number, sudoku, squareX, squareY):
            numbers.append(number)
    return numbers


def number_can_be_in_square(number, sudoku, squareX, squareY):
    boxX, boxY = box_coordinates_of_square(squareX, squareY)

    if number_in_box(number, sudoku, boxX, boxY) or number_on_lines(number, sudoku, squareX, squareY):
        return False
    else:
        return True


def number_in_box(number, sudoku, boxX, boxY):

    for y in range(3):
        for x in range(3):
            if sudoku[y + 3*boxY][x + 3*boxX] == number:
                return True
    return False


def number_on_lines(number, sudoku, squareX, squareY):
    for x in range(9):
        if sudoku[squareY][x] == number:
            return True

    for y in range(9):
        if sudoku[y][squareX] == number:
            return True

    return False


def box_coordinates_of_square(squareX, squareY):
    return (squareX // 3), (squareY // 3)







def print_sudoku(sudoku):
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


def make_list_of_changes(unsolved_sudoku, solved_sudoku):
    list_of_changes = []
    for y in range(9):
        for x in range(9):
            if unsolved_sudoku[y][x] != solved_sudoku[y][x]:
                list_of_changes.append([solved_sudoku[y][x], x, y])
    return list_of_changes
