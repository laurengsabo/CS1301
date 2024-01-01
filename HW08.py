"""
Georgia Institute of Technology - CS1301
HW08 -  API
"""

#########################################

"""
Function Name: averagePopulation()
Parameters: regionalBloc(str)
Returns: average population(float)
"""
def averagePopulation(reg):
    import requests
    baseurl = "https://restcountries.com/v2/regionalbloc/"
    fullurl = baseurl + reg
    print(fullurl)
    r = requests.get(fullurl)
    data_dict = r.json()
    total = 0
    poptotal = 0
    avg = 0
    for dicta in data_dict:
        print(dicta["name"])
        poptotal += dicta["population"]
        total += 1
    avg = (poptotal/total)
    avg = round(avg,2)
    return avg

#########################################

"""
Function Name: commonCountries()
Parameters: langTup1(tuple), langTup2(tuple)
Returns: list of countries(list)
"""
def commonCountries(langTup1, langTup2):
    import requests
    groundurl = "https://restcountries.com/v2/lang/"
    url1 = groundurl + langTup1[0]
    url2 = groundurl + langTup2[0]
    a = requests.get(url1)
    dicta = a.json()
    b = requests.get(url2)
    dictb = b.json()
    alist = []
    blist = []
    finallist = []
    for dictaa in dicta:
        alist.append(dictaa["name"])
    for dictbb in dictb:
        blist.append(dictbb["name"])
    for itema in alist:
        for itemb in blist:
            if itema == itemb:
                finallist.append(itema)
    finallist.sort()
    return finallist
    
#########################################

"""
Function Name: uniqueRegions()
Parameters: countryList(list)
Returns: True or False(bool) or Error Message(str)
"""
def uniqueRegions(countryList):
    import requests
    groundurl = ("https://restcountries.com/v2/alpha/")
    regionlist = []
    invalidoutput = "Invalid country code!"
    
    try:
        for country in countryList:
            newurl = groundurl + country
            r = requests.get(newurl)
            dictr = r.json()
            regionlist.append(dictr["region"])

        for region in range(len(regionlist)):
            for otherregion in regionlist[region+1:]:
                if regionlist[region] != otherregion:
                    return True
                if regionlist[region] == otherregion:
                    return False
    except:
        return invalidoutput

#########################################

"""
Function Name: organizeCapitals()
Parameters: capitalList(list)
Returns: Dictionary mapping regions to a list of countries(dict)
"""
def organizeCapitals(capitallist):
    import requests
    groundurl = ("https://restcountries.com/v2/capital/")
    finaldict ={}
    newfinaldict = {}

    for capital0 in capitallist:
        if capital0.lower() == "invalid":
            capitallist.remove(capital0)

    finaldict["Africa"] = []
    finaldict["Americas"] = []
    finaldict["Europe"] = []
    finaldict["Asia"] = []
    finaldict["Oceania"] = []
    
    for capital1 in capitallist:
        newurl = groundurl + capital1.lower()
        r = requests.get(newurl)
        dictr = r.json()
        for dict0 in dictr:
                finaldict[dict0["region"]].append(dict0["name"])

    for dict1 in finaldict.keys():
        if finaldict[dict1] != []:
            newfinaldict[dict1] = finaldict[dict1]

    return newfinaldict

#########################################

"""
Function Name: visitableCountries()
Parameters: countryCodeList(list)
Returns: list of country names(list)
"""
def visitableCountries(countrylist):
    import requests
    groundurl = ("https://restcountries.com/v2/alpha/")
    nextc = ""
    finallist = []

    for countrynum0 in range(len(countrylist)):
        newurl = groundurl + countrylist[countrynum0]
        r = requests.get(newurl)
        dictr = r.json()
        if countrynum0 == 0:
            finallist.append(dictr["name"])
        try:
            nextc = countrylist[countrynum0+1]
        except:
            continue
            
        for country1 in dictr["borders"]:
            if country1 == nextc:
                newnewurl = groundurl + str(country1)
                nn = requests.get(newnewurl)
                dictnn = nn.json()
                finallist.append(dictnn["name"])
            else:
                continue

            
    return finallist





