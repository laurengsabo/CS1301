"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
"""

#########################################

"""
Function Name: clubPoints()
Parameters: N/A
Returns: None
"""

def clubPoints():
    clubnum = input("How many clubs have you joined?")
    clubnum = int(clubnum)
    friendnum = input("How many friends have you gotten to join clubs?")
    friendnum = int(friendnum)
    youjoin = (30*clubnum)
    friendjoin = ( 50 * friendnum )
    totalpoint = ( youjoin + friendjoin )
    print ("You have won a total of {} points!!".format(totalpoint))

#########################################

"""
Function Name: moveIn()
Parameters: N/A
Returns: None
"""
def moveIn():
    freshmennum = input("How many freshmen do you plan to assist?")
    freshmennum = int(freshmennum)
    
    sophomorenum = input("How many sophomores do you plan to assist?")
    sophomorenum = int(sophomorenum)
    
    juniornum = input("How many juniors do you plan to assist?")
    juniornum = int(juniornum)
    
    freshmentime = (35*freshmennum)
    sophomoretime = (20*sophomorenum)
    juniortime = (15*juniornum)

    totalstudents = (freshmennum + sophomorenum + juniornum)
    totalmin = (freshmentime + sophomoretime + juniortime)
    totalhours = (totalmin // 60)
    remmin = (totalmin % 60)
    print ("It will take {} hours and {} minutes to help {} students with move-in today.".format(totalhours, remmin, totalstudents))


#########################################

"""
Function Name: tireArea()
Parameters: N/A
Returns: None
"""
def tireArea():
    tireradius = input("What is the radius of the tire?")
    tireradius = float(tireradius)
    tirearea = (tireradius **2)
    tirearea = (tirearea * 3.14)
    tirearea = round(tirearea, 2)
    print ("The area of the tire is {}.".format(tirearea))


#########################################

"""
Function Name: dining()
Parameters: N/A
Returns: None
"""
def dining():
    pemeals = input("How many meals do you want to order from Panda Express?")
    pemeals = int(pemeals)
    
    rrmeals = input("How many meals do you want to order from Rising Roll?")
    rrmeals = int(rrmeals)
    
    chickmeals = input("How many meals do you want to order from Chick-fil-A?")
    chickmeals = int(chickmeals)

    mealscost = (6 * pemeals + 8 * rrmeals + 9 * chickmeals)

    tippercent = input("What percent would you like to tip?")
    tippercent = int(tippercent)
    tiptotal = (mealscost / 100 * tippercent)
    tiptotal = round(tiptotal, 2)
    mealscost = (tiptotal + mealscost)
    print ("You paid ${} and tipped ${}." .format(mealscost, tiptotal))


#########################################

"""
Function Name: weeklyBudget()
Parameters: N/A
Returns: None
"""
def weeklyBudget():
    budgetini = input("How much is your budget this week?")
    budgetini = int(budgetini)
    saveperc = input("What percentage do you want to save?")
    saveperc = int(saveperc)
    
    savebudget = (budgetini / 100 * saveperc)
    investbudget = (budgetini - 13.50 - 21.40 - savebudget)
    investbudget = round(investbudget, 2)
    print ("You have ${} left after savings and fees.".format(investbudget))
    
