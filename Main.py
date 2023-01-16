import random


def sum_list(inputList):
    i = 0
    sum = 0
    while i < len(inputList):
        sum += inputList[i]
        i += 1
    return sum


def amount_of_x_in_list(x, inputList):
    i = 0
    count = 0
    while i < len(inputList):
        if inputList[i] == x:
            count += 1
        i += 1
    return count


def operator_converter(num, reverse=False):
    operatorString = " "

    if not reverse:
        if num == 1:
            operatorString = " + "
        elif num == 2:
            operatorString = " - "
        elif num == 3:
            operatorString = " * "
        elif num == 4:
            operatorString = " / "
    else:
        if num == " + ":
            operatorString = 1
        elif num == " - ":
            operatorString = 2
        elif num == " * ":
            operatorString = 3
        elif num == " / ":
            operatorString = 4
        elif num == "+":
            operatorString = 1
        elif num == "-":
            operatorString = 2
        elif num == "*":
            operatorString = 3
        elif num == "/":
            operatorString = 4
        elif num == " +":
            operatorString = 1
        elif num == " -":
            operatorString = 2
        elif num == " *":
            operatorString = 3
        elif num == " /":
            operatorString = 4
        elif num == "+ ":
            operatorString = 1
        elif num == "- ":
            operatorString = 2
        elif num == "* ":
            operatorString = 3
        elif num == "/ ":
            operatorString = 4

    return operatorString


def difficulty_of_equation(inputList):
    # Translating the input list into individual variables.
    # Dice 1, 2, 3, Exponent 1, 2, 3 Operator 1, 2 Total
    d1 = inputList[0]
    d2 = inputList[1]
    d3 = inputList[2]
    p1 = inputList[3]
    p2 = inputList[4]
    p3 = inputList[5]
    o1 = inputList[6]
    o2 = inputList[7]
    total = inputList[8]

    # List of base numbers, base numbers are just the dice numbers to exponents
    basesList = []

    # List of maximum exponents for each dice roll, starting at 0
    # Limiting the max individual base to 10,000. Changed for 6^7/3^7 and such
    maxExponents = maxExponents = [1, 1, 13, 10, 6, 6, 10, 6, 6, 6, 10, 3, 10, 3, 3, 3, 3, 3, 10, 3, 3]

    # Making the dice into a list for a loop later
    diceList = [d1, d2, d3]

    # List of distances between base numbers and the total.
    # This will later be sorted to come up with the shortest distance.
    listOfDistances = []

    # This variable is not currently included in the difficulty calculation
    # It is now.  Smallest number in an the multiplication of two numbers
    smallestMultiplier = 0

    # Making pycharm happy because it gets defined in a if statement
    largestNum = 0

    tenFlag = False

    i = 0
    j = 0

    # Generate bases list
    while i < 3:
        while j < maxExponents[diceList[i]]:
            basesList.append(pow(diceList[i], j))
            j += 1
        i += 1
        j = 0

    i = 0
    j = 0

    # Generate distances list
    while i < len(basesList):
        listOfDistances.append(abs(basesList[i] - total))
        i += 1

    i = 0

    if o1 == 3:
        if d1 == 10 or d2 == 10:
            tenFlag = True
        if pow(d1, p1) >= pow(d2, p2):
            smallestMultiplier = pow(d2, p2)
        else:
            smallestMultiplier = pow(d1, p1)
    if o2 == 3:
        if d2 == 10 or d3 == 10:
            tenFlag = True
        if pow(d2, p2) >= pow(d3, p3):
            smallestMultiplier = pow(d3, p3)
        else:
            smallestMultiplier = pow(d2, p2)

    if smallestMultiplier <= 1:
        smallestMultiplier = 0

    # difficultyVariables has [Result of equation, Shortest distance between a base number and the result,
    # amount of ^0s, amount of ^1s, Largest number in equation, Distance between largest number in equation and the
    # result]

    # Defining difficulty variables
    shortestDistance = min(listOfDistances)
    zeroes = amount_of_x_in_list(0, [p1, p2, p3])
    ones = amount_of_x_in_list(0, [p1, p2, p3])

    if o1 != 3 and o2 != 3:
        largestNum = max(pow(d1, p1), pow(d2, p2), pow(d3, p3))
    elif o1 == 3:
        largestNum = max(pow(d3, p3), pow(d1, p1) * pow(d2, p2))
    elif o2 == 3:
        largestNum = max(pow(d1, p1), pow(d3, p3) * pow(d2, p2))

    largestNumDistance = abs(largestNum - total)

    # Calculating difficulty
    difficulty = pow(total, 0.5) + shortestDistance / 12 + (-1 * zeroes) / 0.45 + (-1 * ones) / 0.7 + \
                 pow(largestNum, 0.5) / 16 + largestNumDistance / 7 + pow(smallestMultiplier, 0.75) / 2

    if tenFlag:
        difficulty = (difficulty - 5) / 1.75

    # Smoothing
    if difficulty < 3:
        difficulty = difficulty

    if difficulty > 90:
        difficulty = 99 + difficulty / 5000

    if difficulty > 100:
        difficulty = 100

    return round(difficulty * 100) / 100


def generate_random_board(highestNum=999):
    boardNums = []

    while len(boardNums) < 36:
        nextNum = random.randint(1, highestNum)
        if amount_of_x_in_list(nextNum, boardNums) == 0:
            boardNums.append(nextNum)

    boardNums.sort()
    return boardNums


def generate_pattern_board(multiple=[6], startingNumber=6):
    boardList = []
    i = 0

    if len(multiple) == 1:
        while i < 36:
            boardList.append(startingNumber + i * multiple[0])
            i += 1
        i = 0
    elif len(multiple) == 2:
        while i < 18:
            boardList.append(startingNumber + i * multiple[0] + i * multiple[1])
            boardList.append(startingNumber + + i * multiple[0] + i * multiple[1] + multiple[0])
            i += 1
        i = 0
    return boardList


def generate_random_dice(minDice=1, maxDice=10, lastMaxDice=20):
    dice = [random.randint(minDice, maxDice), random.randint(minDice, maxDice), random.randint(minDice, lastMaxDice)]
    while amount_of_x_in_list(dice[0], dice) > 2:
        dice = [random.randint(minDice, maxDice), random.randint(minDice, maxDice),
                random.randint(minDice, lastMaxDice)]
    return dice


def calculate_equation(n1, n2, n3, o1, o2):
    if o1 == 1:
        if o2 == 1:
            return n1 + n2 + n3
        if o2 == 2:
            return n1 + n2 - n3
        if o2 == 3:
            return n1 + n2 * n3
        if o2 == 4:
            return n1 + n2 / n3
    if o1 == 2:
        if o2 == 1:
            return n1 - n2 + n3
        if o2 == 2:
            return n1 - n2 - n3
        if o2 == 3:
            return n1 - n2 * n3
        if o2 == 4:
            return n1 - n2 / n3
    if o1 == 3:
        if o2 == 1:
            return n1 * n2 + n3
        if o2 == 2:
            return n1 * n2 - n3
        if o2 == 3:
            return n1 * n2 * n3
        if o2 == 4:
            return n1 * n2 / n3
    if o1 == 4:
        if o2 == 1:
            return n1 / n2 + n3
        if o2 == 2:
            return n1 / n2 - n3
        if o2 == 3:
            return n1 / n2 * n3
        if o2 == 4:
            return n1 / n2 / n3


def cycle(x, y, z, i):
    if i == 0:
        return [x, y, z]
    elif i == 1:
        return [x, z, y]
    elif i == 2:
        return [y, x, z]
    elif i == 3:
        return [y, z, x]
    elif i == 4:
        return [z, y, x]
    elif i == 5:
        return [z, x, y]


def de_power(x):
    if x == 4 or x == 8 or x == 16:
        return 2
    elif x == 9:
        return 3
    else:
        return x


def easiest_solution(inputList):
    dice1 = de_power(inputList[0])
    dice2 = de_power(inputList[1])
    dice3 = de_power(inputList[2])
    total = inputList[3]
    p1 = 0
    p2 = 0
    p3 = 0
    o1 = 1
    o2 = 1

    i = 0

    # List of maximum exponents for each dice roll, starting at 0
    # Limiting the max individual base to 10,000.  Changed this so I can do things like 6^7/3^7
    maxExponents = [1, 1, 13, 10, 6, 6, 10, 6, 6, 6, 10, 3, 10, 3, 3, 3, 3, 3, 10, 3, 3]

    # List of solutions.  Formatted normally (including the total)
    solutionsList = []

    # Current lowest difficulty achieved by an equation
    smallestDifficulty = pow(10, 10)

    # Current least difficult equation
    easiestEquation = []

    run = True

    while i < 6:

        d1 = cycle(dice1, dice2, dice3, i)[0]
        d2 = cycle(dice1, dice2, dice3, i)[1]
        d3 = cycle(dice1, dice2, dice3, i)[2]

        while run:

            if calculate_equation(pow(d1, p1), pow(d2, p2), pow(d3, p3), o1, o2) == total:
                solutionsList.append([d1, d2, d3, p1, p2, p3, o1, o2, total])
                if difficulty_of_equation([d1, d2, d3, p1, p2, p3, o1, o2, total]) < smallestDifficulty:
                    smallestDifficulty = difficulty_of_equation([d1, d2, d3, p1, p2, p3, o1, o2, total])
                    easiestEquation = [d1, d2, d3, p1, p2, p3, o1, o2, total]
            if p1 < maxExponents[d1]:
                p1 += 1
            elif p2 < maxExponents[d2]:
                p2 += 1
                p1 = 0
            elif p3 < maxExponents[d3]:
                p3 += 1
                p2 = 0
                p1 = 0
            elif o1 < 4:
                o1 += 1
                p3 = 0
                p2 = 0
                p1 = 0
            elif o2 < 4:
                o2 += 1
                o1 = 0
                p3 = 0
                p2 = 0
                p1 = 0
            else:
                run = False
        run = True
        i += 1
        o2 = 0
        o1 = 0
        p3 = 0
        p2 = 0
        p1 = 0

    return easiestEquation


def validate_user_input(firstString, errorString="Error, please enter an integer: "):
    validatedInput = 0
    tryLoop = True

    try:
        validatedInput = int(input(firstString))
    except ValueError:
        while tryLoop:
            tryLoop = False
            try:
                validatedInput = int(input(errorString))
            except ValueError:
                tryLoop = True
    return validatedInput


def validate_between_ranges(minVal, maxVal, userInput):
    while userInput < minVal or userInput > maxVal:
        userInput = validate_user_input("Error, value out of range.  Please re enter value: ")
    return userInput


def print_board(numList):
    i = 0
    while i < 6:
        print(str(numList[6 * i + 0]) + " " + str(numList[6 * i + 1]) + " " + str(numList[6 * i + 2]) + " " +
              str(numList[6 * i + 3]) + " " + str(numList[6 * i + 4]) + " " + str(numList[6 * i + 5]))
        i += 1

    i = 0


def convert_list_of_strings(inputList):
    # Converts a list of string to a list of integers
    outputList = []
    for a in inputList:
        outputList.append(int(a))
    return outputList


def check_with_multiple_strings(main, string1, string2="", string3="", string4="", string5=""):
    if string2 == "":
        string2 = string1
    if string3 == "":
        string3 = string1
    if string4 == "":
        string4 = string1
    if string5 == "":
        string5 = string1
    return main == string1 or main == string2 or main == string3 or main == string4 or main == string5


diceList = [[2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 2, 6], [2, 2, 7], [2, 2, 10], [2, 3, 3], [2, 3, 5], [2, 3, 6],
            [2, 3, 7], [2, 3, 10], [2, 3, 11], [2, 3, 12], [2, 3, 13], [2, 3, 14], [2, 3, 15], [2, 3, 17],
            [2, 3, 18], [2, 3, 19], [2, 3, 20], [2, 5, 5], [2, 5, 6], [2, 5, 10], [2, 6, 6], [2, 6, 7], [2, 6, 12],
            [3, 3, 5], [3, 3, 6], [3, 3, 12], [3, 5, 5], [3, 5, 6], [3, 5, 7], [3, 5, 15], [3, 6, 6],
            [3, 6, 7], [3, 6, 10], [3, 6, 12], [3, 6, 18]]

listOfCommands = "Command 1: End\n" \
                 "Command 2: List commands\n" \
                 "Command 3: Generate random board\n" \
                 "Command 4: Generate pattern board\n" \
                 "Command 5: Generate random dice\n" \
                 "Command 6: Solve equation\n" \
                 "Command 7: Find difficulty\n" \
                 "Command 8: Find board difficulty"
# "Complex Command 1: Find dice difficulties"

print("Welcome to the all in one N2K program.  Type in any of the following words to execute a command. ")
print(listOfCommands)

run = True

tryLoop = True

while run:

    currentCommand = input("\nEnter a command: ")

    if check_with_multiple_strings(currentCommand.upper(), "LIST COMMANDS", "2", "COMMAND 2", "C2"):
        print(listOfCommands)
    elif check_with_multiple_strings(currentCommand.upper(), "GENERATE RANDOM BOARD", "3", "COMMAND 3", "C3"):
        userHighestNum = validate_user_input(firstString="Enter the range of the board "
                                                         "(Ex. 600 makes a board from 1-600): ")
        userHighestNum = validate_between_ranges(36, 10000, userHighestNum)

        print(generate_random_board(highestNum=userHighestNum))
    elif check_with_multiple_strings(currentCommand.upper(), "GENERATE PATTERN BOARD", "4", "COMMAND 4", "C4"):
        userMultiple = validate_user_input(firstString="Enter the multiple between numbers for the board: ")

        userMultiple = validate_between_ranges(1, 500, userMultiple)

        print(generate_pattern_board(multiple=[userMultiple]))
    elif check_with_multiple_strings(currentCommand.upper(), "GENERATE RANDOM DICE", "5", "COMMAND 5", "C5"):
        userMaxDice = validate_user_input(firstString="Enter the maximum number for the first two die: ")

        userMaxDice = validate_between_ranges(2, 20, userMaxDice)

        userLastMaxDice = validate_user_input(firstString="Enter the maximum number for the last die: ")

        userLastMaxDice = validate_between_ranges(2, 20, userLastMaxDice)

        print(generate_random_dice(maxDice=userMaxDice, lastMaxDice=userLastMaxDice))
    elif check_with_multiple_strings(currentCommand.upper(), "SOLVE EQUATION", "6", "COMMAND 6", "C6"):
        userFirstDie = validate_user_input(firstString="Enter the first dice roll in the equation: ")

        userFirstDie = validate_between_ranges(2, 20, userFirstDie)

        userSecondDie = validate_user_input(firstString="Enter the second dice roll in the equation: ")

        userSecondDie = validate_between_ranges(2, 20, userSecondDie)

        userThirdDie = validate_user_input(firstString="Enter the third dice roll in the equation: ")

        userThirdDie = validate_between_ranges(2, 20, userThirdDie)

        userBoardNum = validate_user_input(firstString="Enter the board number for the equation: ")

        userBoardNum = validate_between_ranges(-1000000, 1000000, userBoardNum)

        solutionValues = easiest_solution([userFirstDie, userSecondDie, userThirdDie, userBoardNum])

        try:
            print(str(solutionValues[0]) + "^" + str(solutionValues[3]) + operator_converter(solutionValues[6]) +
                  str(solutionValues[1]) + "^" + str(solutionValues[4]) + operator_converter(solutionValues[7]) +
                  str(solutionValues[2]) + "^" + str(solutionValues[5]) + " = " +
                  str(solutionValues[8]))
        except IndexError:
            print("No possible solution")
    elif check_with_multiple_strings(currentCommand.upper(), "FIND DIFFICULTY", "7", "COMMAND 7", "C7"):
        userEquation = input("Enter equation to find difficulty (Format: '2^5 + 2^2 + 2^2 = 40'): ")
        userList = userEquation.split(" ")

        userOperatorOne = operator_converter(userList[1], reverse=True)
        userOperatorTwo = operator_converter(userList[3], reverse=True)

        userFirstBase = userList[0].split("^")
        userSecondBase = userList[2].split("^")
        userThirdBase = userList[4].split("^")

        userFirstDie = userFirstBase[0]
        userSecondDie = userSecondBase[0]
        userThirdDie = userThirdBase[0]

        userFirstPower = userFirstBase[1]
        userSecondPower = userSecondBase[1]
        userThirdPower = userThirdBase[1]

        total = userList[6]

        finalList = [int(userFirstDie), int(userSecondDie), int(userThirdDie), int(userFirstPower),
                     int(userSecondPower), int(userThirdPower), int(userOperatorOne), int(userOperatorTwo), int(total)]

        print("Difficulty: " + str(difficulty_of_equation(finalList)))
    elif check_with_multiple_strings(currentCommand.upper(), "FIND BOARD DIFFICULTY", "8", "COMMAND 8", "C8"):
        count = 0

        diceAndDifficulties = []

        boardNums = convert_list_of_strings(
            ((input("Enter board: ").replace("[", "")).replace("]", "")).split(","))

        extraInfo = ""

        i = 0

        while extraInfo.upper() != "Y" and extraInfo.upper() != "N":
            extraInfo = input("Would you like extra information to be outputted? (y or n): ")

        if extraInfo.upper() == "Y":
            extraInfo = True
        else:
            extraInfo = False

        difficulty0_10 = []
        difficulty10_20 = []
        difficulty20_30 = []
        difficulty30_40 = []
        difficulty40_50 = []
        difficulty50_65 = []
        difficulty65_80 = []
        difficulty80_100 = []

        while count < len(diceList):

            dice = diceList[count]

            # Difficulty for each number on the board
            difficultyOfBoardNums = []

            # Number of impossible to get board numbers
            impossibleNums = 0

            # A difficulty list that doesn't include any impossible ones
            possibleDifficulties = []

            # Initializing the traditional i and j :D
            # making i 1 for the loading % loop
            i = 1
            j = 0

            # Setting up the loading %
            while i < 10:
                if count == round(i * len(diceList) / 10):
                    print("Loading, " + str(i) + "0% Completed")
                i += 1

            i = 0

            # Printing the board
            if extraInfo:
                print_board(boardNums)

            # Calculating the difficulty of the boardNums
            while i < len(boardNums):
                currentEasiestSolution = easiest_solution([dice[0], dice[1], dice[2], boardNums[i]])

                if len(currentEasiestSolution) > 0:
                    difficultyOfBoardNums.append(difficulty_of_equation(currentEasiestSolution))
                    possibleDifficulties.append(difficulty_of_equation(currentEasiestSolution))
                else:
                    difficultyOfBoardNums.append(-1)
                    impossibleNums += 1

                i += 1
            i = 0

            if extraInfo:
                print_board(difficultyOfBoardNums)

            if extraInfo:
                print(dice)
                print(str(round(impossibleNums * 10000 / 36) / 100) + "%")
                print(str(round(sum_list(possibleDifficulties) / len(possibleDifficulties) * 100) / 100))

            boardDifficulty = (sum_list(possibleDifficulties) / len(possibleDifficulties) * (36 - impossibleNums)
                               + 100 * impossibleNums) / 36

            diceAndDifficulties.append(
                [dice, round(sum_list(possibleDifficulties) / len(possibleDifficulties) * 100) / 100,
                 impossibleNums])

            boardDifficulty = round(boardDifficulty * 100) / 100

            if boardDifficulty < 10:
                difficulty0_10.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 20:
                difficulty10_20.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 30:
                difficulty20_30.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 40:
                difficulty30_40.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 50:
                difficulty40_50.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 65:
                difficulty50_65.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 80:
                difficulty65_80.append(str(dice) + "(" + str(boardDifficulty) + ")")
            elif boardDifficulty < 100:
                difficulty80_100.append(str(dice) + "(" + str(boardDifficulty) + ")")

            count += 1

        print("Board difficulty summary\n")
        print("Dice that give difficulty from 0-10: " + str(difficulty0_10))
        print("Dice that give difficulty from 10-20: " + str(difficulty10_20))
        print("Dice that give difficulty from 20-30: " + str(difficulty20_30))
        print("Dice that give difficulty from 30-40: " + str(difficulty30_40))
        print("Dice that give difficulty from 40-50: " + str(difficulty40_50))
        print("Dice that give difficulty from 50-65: " + str(difficulty50_65))
        print("Dice that give difficulty from 65-80: " + str(difficulty65_80))
        print("Dice that give difficulty from 80-100: " + str(difficulty80_100))
    elif check_with_multiple_strings(currentCommand.upper(), "END", "1", "COMMAND 1", "C1"):
        run = False
    else:
        print("Error, command not in list of commands")
