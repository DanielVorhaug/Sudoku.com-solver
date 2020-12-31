import websiteinterface as web


def solve(sudoku):
    sudoku = logicsolve(sudoku)

    if not sudoku_is_solved(sudoku):
        sudoku = guessolve(sudoku)

    return sudoku


def logicsolve(sudoku):
    while not sudoku_is_solved(sudoku):
        a_square_has_been_filled = False

        for y in range(9):
            for x in range(9):
                if sudoku[y][x] == None:
                    number = only_one_number_can_be_in_square(sudoku, x, y)
                    if number:
                        sudoku[y][x] = number
                        web.fill_square(number, x, y)
                        a_square_has_been_filled = True

        if not a_square_has_been_filled:
            break
    return sudoku


def guessolve(sudoku):
    #print(highest_amount_of_iterations(sudoku))
    iterations = 0
    changes = []
    place_in_list = -1
    while not sudoku_is_solved(sudoku):
        iterations += 1
        numbers, least_squareX, least_squareY = least_possible_numbers_square(
            sudoku)
        change = {
            "x": least_squareX,
            "y": least_squareY,
            "number": numbers[0],
            "tried": [],
            "untried": numbers[1:]
        }

        changes.append(change)
        place_in_list += 1

        sudoku[changes[place_in_list]["y"]][changes[place_in_list]
                                            ["x"]] = changes[place_in_list]["number"]

        while squares_have_no_solutions(sudoku):
            while not len(changes[place_in_list]["untried"]):
                sudoku[changes[place_in_list]["y"]
                       ][changes[place_in_list]["x"]] = None
                changes.pop(place_in_list)
                place_in_list -= 1

            changes[place_in_list]["tried"].append(
                changes[place_in_list]["number"])
            changes[place_in_list]["number"] = changes[place_in_list]["untried"].pop(
                0)
            sudoku[changes[place_in_list]["y"]][changes[place_in_list]
                                                ["x"]] = changes[place_in_list]["number"]
            iterations += 1

    #print(iterations)
    for change in changes:
        web.fill_square(change["number"], change["x"], change["y"])
    return sudoku


def highest_amount_of_iterations(sudoku):
    iterations = 1
    possibilities = possible_numbers(sudoku)
    for line in possibilities:
        for square in line:
            if square != None:
                iterations *= len(square)
    return iterations


def possible_numbers(sudoku):
    numbers = [[None for x in range(9)] for y in range(9)]
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == None:
                numbers[y][x] = numbers_that_can_be_in_square(sudoku, x, y)
    return numbers


def least_possible_numbers_square(sudoku):
    possible_numbers_in_sudoku = possible_numbers(sudoku)
    count = 10
    squareX = 0
    squareY = 0
    for y in range(9):
        for x in range(9):
            if possible_numbers_in_sudoku[y][x] != None and len(possible_numbers_in_sudoku[y][x]) < count:
                count = len(possible_numbers_in_sudoku[y][x])
                squareX = x
                squareY = y
    return possible_numbers_in_sudoku[squareY][squareX], squareX, squareY


def squares_have_no_solutions(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == None:
                if len(numbers_that_can_be_in_square(sudoku, x, y)) == 0:
                    return True
    return False


def sudoku_is_solved(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[y][x] == None:
                return False
    return True


def only_one_number_can_be_in_square(sudoku, squareX, squareY):
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


# def make_list_of_changes(unsolved_sudoku, solved_sudoku):
#     list_of_changes = []
#     for y in range(9):
#         for x in range(9):
#             if unsolved_sudoku[y][x] != solved_sudoku[y][x]:
#                 list_of_changes.append([solved_sudoku[y][x], x, y])
#     return list_of_changes
