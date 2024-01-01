"""
Georgia Institute of Technology - CS1301
HW03 - Loops and Iteration
"""

#########################################

"""
Function Name: userReplace()
Parameters: startingString (str), username (str)
Returns: replacedString (string)
"""
def userReplace(startingString, username):
    for char in startingString:
        if char == "$":
            replacedString = startingString.replace("$", username)
            return replacedString

#########################################


""""
Function Name: specialChar()
Parameters: characterString (str)
Returns: sumOfIndices (int)
"""
def specialChar(characterString):
    sumOfIndices = int(0)
    for char in characterString:
        if char == "!":
            sumOfIndices += 1
        if char == "@":
            sumOfIndices += 2
        if char == "#":
            sumOfIndices += 3
        if char == "$":
            sumOfIndices += 4
        if char == "%":
            sumOfIndices += 5
        if char == "^":
            sumOfIndices += 6
        if char == "&":
            sumOfIndices += 7
        if char == "*":
            sumOfIndices += 8
        else:
            continue

    return sumOfIndices

#########################################

"""
Function Name: footballGame()
Parameters: score1 (str), score2 (str), team1 (str), team2 (str)
Returns: winningTeam (string)
"""
def footballGame(score1, score2, team1, team2):
    score1f = 0
    score2f = 0
    winningTeam = ""

    for char in score1:
        if char != "_":
           score1f += int(char)
        else:
            continue
    for char in score2:
        if char != "_":
           score2f += int(char)
        else:
            continue

    if score1f > score2f:
        winningTeam = team1
    elif score2f > score1f:
        winningTeam = team2
    else:
        winningTeam = "It's a tie!"
    return(winningTeam)

#########################################

"""
Function Name: buyTheDip()
Parameters: currentPrice (float), finalPrice (float), growth (float)
Returns: days (int)
"""

def buyTheDip(currentPrice, finalPrice, growth):
    days = 0
    growth *= 0.01
    
    while currentPrice > finalPrice:
        midstep = currentPrice * growth
        currentPrice += midstep
        days = days + 1

    return days

#########################################

"""
Function Name: questionMaker()
Parameters: questions (str), subQuestions (str)
Returns: combinedQuestions (str)
"""
def questionMaker(questions, subQuestions):
    combinedQuestions = ""
    
    for num in questions:
        for char in subQuestions:
            combinedQuestions += num + char
    return combinedQuestions
