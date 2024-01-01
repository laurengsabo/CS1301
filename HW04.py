"""
Georgia Institute of Technology - CS1301
HW04 - Strings, indexing and lists
"""

#########################################

"""
Function Name: fixTickets()
Parameters: ticketNumber (str)
Returns: fixedTicket (str)
"""
def fixTickets(ticketNumber):
    fixedTicket = ""
    for num in range(len(ticketNumber)):
        if ticketNumber[num] in "0123456789":
            fixedTicket += ticketNumber[num]
            continue
        if ticketNumber[num].isupper():
            fixedTicket += ticketNumber[num].lower()
        if ticketNumber[num].islower():
            fixedTicket += ticketNumber[num].upper()
    return fixedTicket

#########################################

"""
Function Name: secret()
Parameters: message (str)
Returns: secret message (str)
"""
def secret(message):
    secretmessage = ""
    medmessage = ""
    medmessage = message.split(" ")
    for num in range(len(medmessage)):
        medmessage[num] = medmessage[num][::-1]
        if num < (len(medmessage) - 1): 
            secretmessage += medmessage[num] + " "
        elif num == (len(medmessage) - 1):
            secretmessage += medmessage[num]
        
    return secretmessage 

#########################################

"""
Function Name: countTickets()
Parameters: aList (list)
Returns: total (int) or error message (str)
"""
def countTickets(aList):
    total = 0
    errormessage = ""

    for num in range(len(aList)):
        if isinstance(aList[num], int):
            if int(aList[num]) <= 3:
                total += aList[num]
            else:
                errormessage = "Sorry {}, but you can only get a maximum of three tickets per person.".format(aList[num-1])
                return errormessage
        elif isinstance(aList[num], str):
                continue

    return total


#########################################

"""
Function Name: fieldTripRoster()
Parameters: friendList (list)
Returns: nameList (list)
"""
def fieldTripRoster(friendList):
    nameList = []
    for thing in range(len(friendList)):
        for thing2 in range(len(friendList[thing])):
            if isinstance(friendList[thing][thing2], str):
                nameList.append(friendList[thing][thing2])
        else:
            continue
    nameList.sort()

    for seq  in range(len(nameList)):
        while seq <= (len(nameList)-2):
            if nameList[seq] == nameList[seq+1]:
                nameList.remove(nameList[seq+1])
            else:
                break
    return nameList

#########################################

"""
Function Name: isSublist()
Parameters: myList (list), otherList (list)
Returns: True or False (bool)
"""
def isSublist(myList, otherList):
    startMy = 0
    finishMy = int(len(myList))
    startO = 0
    finishO = int(len(otherList))
    final = True

    if myList == otherList:
        final = True
    if myList or otherList == []:
        final = True

    for char in range(startO, finishO, 1):
        if otherList[char] in myList:
            continue
        else:
            final = False
    
    if otherList[0] in myList:
        startMy = int(myList.index(otherList[0]))

        
    for num in range(startO, finishO, 1):
        if (num+1) <= len(otherList):
            break
        if num != finishO-1:
            if myList.index(otherList[num]) < myList.index(otherList[num+1]):
                continue
            elif myList.index(otherList[num]) > myList.index(otherList[num+1]):
                final = False
        elif num == finishO:
            final = True
    return final


print(isSublist(['Arvin', 'Arushi', 'Naomi', 'Michael', 'Nikhila', 'Assata'], ['Arushi', 'Naomi', 'Assata', 'Nikhila']))



        



