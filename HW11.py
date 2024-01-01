"""
Georgia Institute of Technology - CS1301
HW11
"""

#########################################

"""
Function Name: potluck()
Parameters: food list (list)
Returns: food types (dict)
"""
def potluck(foods):
    final = {}
    for tup in foods:
        final[(tup[1])] = []

    for tup in foods:
        final[(tup[1])].append(tup[0])

    return final

#########################################

"""
Function Name: insertEmoji()
Parameters: message (str), emojis (dict)
Returns: final message (str)
"""
def insertEmoji(saying, emojis):
    for key, value in emojis.items():
        if key in saying:
            saying = saying.replace("*"+key,value)
            
    return saying

#########################################

"""
Function Name: buyTickets()
Parameters: ticket prices (dict)
Returns: best website and time to buy (str)
"""
def buyTickets(tickets):
    finlist = []
    for key in tickets:
        print(key)
        if len(tickets[key]) > 0:
            for thing in tickets[key]:
                time = thing[0]
                amount = thing[1]
                fintup = (amount, time, key)
                finlist.append(tuple(fintup))
    finlist.sort()
    winner = finlist[0]
    return "Buy tickets from {} at {}pm.".format(winner[2], winner[1])

#########################################

"""
Function Name: dinnerLocation()
Parameters: preferred locations (dict), location (str)
Returns: whether majority of people favor that certain time (bool)
"""
def dinnerLocation(availability, place):
    places = {}
    numfriends = float(len(availability))

    for key, value in availability.items():
        for thing in value:
            places[thing] = 0

    for key, value in availability.items():
        for thing in value:
            places[thing] += 1

    if place not in places.keys():
        return False

    if places[place] > (0.5*numfriends):
        return True
    elif places[place] <= (0.5*numfriends):
        return False

#########################################

"""
Function Name: sumNestedList()
Parameters: nested list (list)
Returns: sum of all integers (int)
"""
def sumNestedList(alist):
    if type(alist) != list:
        return alist
    elif len(alist) == 0:
        return 0
    else:
        return sumNestedList(alist[0]) + sumNestedList(alist[1:])
