"""
Georgia Institute of Technology - CS1301
HW07 -  File I/O & CSV
"""

#########################################

"""
Function Name: sortByArtist()
Parameters: filename (str), artist (str)
Returns: list of songs (list)
"""
def sortByArtist(filename, artist):
    infile = open(filename, "r")
    data = infile.readlines()
    infile.close()
    newstr = []
    addon = []
    final = []
    
    for line in data:
        if line == "\n":
            continue
        if "\n" in line:
            addon = line[:len(line)-1]
            newstr.append(addon)
            addon = []
        else:
            newstr.append(line)
            
    for thing in range(len(newstr)):
        if newstr[thing] == artist:
            final.append(newstr[thing-2])
            
    return final

#########################################

"""
Function Name: genreFilter()
Parameters: filename (str)
Returns: mapping of songs to lists of genres of that song (dict)
"""


def genreFilter(filename):
    myfile = open(filename, "r")
    data = myfile.readlines()
    new2str = []
    addonstr = []
    new1 = ""
    new2 = ""
    new3 = ""
    addon = []
    final = {}
    newword = ""
    finalnew = []
    
    for num0 in range(len(data)):
        if data[num0] == "\n":
            new1 = data[num0+1]
            addonstr.append(new1)
            new2 = data[num0+2]
            addonstr.append(new2)
            new3 = data[num0+3]
            addonstr.append(new3)
            new2str.append(addonstr)
            addonstr = []

    for num1 in range(len(new2str)):
        for num2 in range(len(new2str[num1])):
            if "\n" in new2str[num1][num2]:
                newword = new2str[num1][num2][:len(new2str[num1][num2])-1]
                new2str[num1][num2] = newword
                newword = ""
                
    for num3 in range(len(new2str)):
        for num4 in range(len(new2str[num3])):
            if num4 == 1:
                final[new2str[num3][num4]] = []

    for num5 in range(len(new2str)):
        for num6 in range(len(new2str[num5])):
            if num6 == 1:
                final[new2str[num5][num6]].append(new2str[num5][num6-1])


    return final
    myfile.close()

#########################################

"""
Function Name: sortByGenre()
Parameters: filename (str), genre (str), output filename (str)
Returns: None (NoneType)
"""
def sortByGenre(ogfilename, genre, newfilename):
    myfile = open(ogfilename, "r")
    data = myfile.readlines()
    new2str = []
    addonstr = []
    new1 = ""
    new2 = ""
    new3 = ""
    addon = []
    final = {}
    newword = ""
    addonnew = ""
    
    for num0 in range(len(data)):
        if data[num0] == "\n":
            new1 = data[num0+1]
            addonstr.append(new1)
            new2 = data[num0+2]
            addonstr.append(new2)
            new3 = data[num0+3]
            addonstr.append(new3)
            new2str.append(addonstr)
            addonstr = []

    for num1 in range(len(new2str)):
        for num2 in range(len(new2str[num1])):
            if "\n" in new2str[num1][num2]:
                newword = new2str[num1][num2][:len(new2str[num1][num2])-1]
                new2str[num1][num2] = newword
                newword = ""
                
    for num3 in range(len(new2str)):
        for num4 in range(len(new2str[num3])):
            if new2str[num3][num4] == genre:
                final[new2str[num3][num4]] = []

    for num5 in range(len(new2str)):
        for num6 in range(len(new2str[num5])):
            if new2str[num5][num6] == genre:
                addonnew = (new2str[num5][num6-1] + " - " + new2str[num5][num6+1])
                final[new2str[num5][num6]].append(addonnew)

    for num7 in final.values():
        num7.sort()

    outfile = open(newfilename, "w")
    outfile.write(genre +"\n\n")

    try:
        for num8 in range(len(final[genre])):
            if num8 != (len(final[genre])-1):
                outfile.write(str(num8 +1) + ". " + final[genre][num8] +"\n")
            else:
                outfile.write(str(num8 +1) + ". " + final[genre][num8])
    except:
        outfile.close()

    outfile.close()
    myfile.close()


#########################################

"""
Function Name: biggestSuccess()
Parameters: filename (str), artists (list)
Returns: artist and percentage (tuple)
"""
def biggestSuccess(filename, artists):
    csvfile = open(filename, "r")
    headers = csvfile.readline()
    data = csvfile.readlines()
    csvfile.close()
    pieces = []

    compare = {}
    rationum = 0
    ratioden = 0
    zone = ""
    ayo = []
    store = 0
    final = ()

    for line0 in data:
        pieces.append(line0.split(","))

    for line1 in range(len(pieces)):
        if "\n" in pieces[line1][3]:
            zone = pieces[line1][3][:len(pieces[line1][3])-1]
            pieces[line1][3] = zone
            zone = ""

    for line2 in range(len(pieces)):
        for artistnum in range(len(artists)):
            if pieces[line2][0] == artists[artistnum]:
                rationum = int(pieces[line2][3])
                ratioden = int(pieces[line2][1])
                try:
                    ratio = rationum/ ratioden
                    compare[artists[artistnum]] = []
                    compare[artists[artistnum]] = round((ratio*100),2)
                    float(compare[artists[artistnum]])
                except:
                    break

    ayo = sorted(compare.values())
    store = ayo[len(ayo)-1]

    for artist, ratio in compare.items():
        if ratio == store:
            final = (artist, ratio)

    if final[1] == 0.0:
        final = ()

    return final

#########################################

"""
Function Name: grammyAwards()
Parameters: filename (str), artists (list)
Returns: category of artists by celebrity status (dict)
"""
def grammyAwards(filename, artists):
    csvfile = open(filename, "r")
    headers = csvfile.readline()
    data = csvfile.readlines()
    csvfile.close()
    pieces = []

    compare = {}
    rationum = 0
    ratioden = 0
    ratio = 0
    zone = ""
    ayo = []
    store = 0
    final = ()

    listdict = {}

    for line0 in data:
        pieces.append(line0.split(","))

    for line1 in range(len(pieces)):
        if "\n" in pieces[line1][3]:
            zone = pieces[line1][3][:len(pieces[line1][3])-1]
            pieces[line1][3] = zone

    for line2 in range(len(pieces)):
        for artistnum in range(len(artists)):
            if pieces[line2][0] == artists[artistnum]:
                rationum = int(pieces[line2][3])
                ratioden = int(pieces[line2][1])
                try:
                    ratio = rationum/ ratioden
                    compare[artists[artistnum]] = []
                    compare[artists[artistnum]] = round((ratio*100),2)
                except:
                    break
    
    listdict["C-List"] = []
    listdict["B-List"] = []
    listdict["A-List"] = []
    
    for key in compare.keys():
        if compare[key] > 70:
            listdict["A-List"].append(key)
        if compare[key] > 30 and compare[key] <= 70:
            listdict["B-List"].append(key)
        if compare[key] <= 30:
            listdict["C-List"].append(key)
    return listdict
