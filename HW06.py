"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries and Try/Except
"""

#########################################

"""
Function Name: possibleMovies()
Parameters: movies(dict), time (str)
Returns: list of movie names (list)
"""
def possibleMovies(movies, time):
    moviesfinal = []
    for key in movies.keys():
        if time in movies[key]:
            moviesfinal.append(key)
    moviesfinal.sort()
    return moviesfinal

#########################################

"""
Function Name: gameSelector()
Parameters: gameList (list), filterType (str)
Returns: dictionary of games mapped to a boolean value (dict)
"""

def gameSelector(gameList, filterType):
    final = {}
    if filterType == "even":
        for nume in range(len(gameList)):
            if len(gameList[nume])%2 == 0:
                final[gameList[nume]] = True
            else:
                final[gameList[nume]] = False
    if filterType == "odd":
        for numo in range(len(gameList)):
            if len(gameList[numo])%2 == 1:
                final[gameList[numo]] = True
            else:
                final[gameList[numo]] = False
    return final
    
#########################################

"""
Function Name: foodDecoder()
Parameters: secretList1 (list), secretList2 (list)
Returns: list of combined strings and the number of errors (list)
"""
def foodDecoder(list1, list2):
    errors = 0
    final = []
    newlist1 = []
    newlist2 = []
    addon = ""
    for item1 in range(len(list1)):
        if type(list1[item1]) == str and type(list2[item1]) == str:
            newlist1.append(list1[item1])
            newlist2.append(list2[item1])
        else:
            errors += 1
            continue

    for item3 in range(len(newlist1)):
        addon = newlist1[item3]+newlist2[item3]
        final.append(addon)
        addon = ""
    final.append(errors)
    return final

#########################################

"""
Function Name: cheapestLocations()
Parameters: activities (dict)
Returns: dictionary mapping each activity to a location (dict)
"""
def cheapestLocations(activities):
    numlist = []
    lowestnum = 0.0
    cheapest = ""
    final = {}
    for key1 in activities.keys():
        for key2 in activities[key1].keys():
            numlist.append(activities[key1][key2])
        numlist.sort()
        lowest = numlist[0]
        numlist = []
        for key3 in activities[key1].keys():
            if lowest == activities[key1][key3]:
                cheapest = key3
                final[key1] = cheapest
    return final

#########################################

"""
Function Name: sportSuggestions()
Parameters: friends mapped to their suggested sports (dict)
Returns: dictionary mapping each sport to the list of friends who selected these sports (dict).
"""
def sportSuggestions(friends):
    final = {}
    addon = ""
    for key0 in friends.keys():
        friends[key0].sort()
    print(friends)
    for key1 in friends.keys():
        for sub1 in range(len(friends[key1])):
            if friends[key1][sub1] not in final:
                addon = friends[key1][sub1]
                final[addon] = [key1]
                addon = ""
            elif friends[key1][sub1] in final:
                addon = friends[key1][sub1]
                final[addon].append(key1)
    for key2 in final.keys():
        final[key2].sort()
    return final
