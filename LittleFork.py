# Project: Better Little Fork
'''
Make a better sorting program,
1. grabs players in game (tip: perhaps make everything static, after code in variables)
2. sort list with variables attached
3. function to sort by value, and then alphabetically (3 list)
4. base priority system by 0. 1. and 2.

'''
#from collections import deque
import time, random
nameEntries = []
 
def userinput():
    #Gather 3 variables for this
    aInt = False
    numbers = 0
    while aInt != True:
        a = input("Please enter how many rounds to play: ")
        b = str.isdigit(a)
        if b is True:
            a = int(a)
        else:
            print("Please try again!\n\n")
        aInt = isinstance(a, int)
        if aInt == True:
            if a <= 0:
                print("You cannot have a value of 0 or less. Please try again. \n\n")
                print("Setting to 1 Round")
                a = 1
            else:
                if a > 1:
                    print(str(a) + " Rounds entered.")
                if a == 1:
                    print(str(a) + " Round entered.")
        if aInt == False:
            print("You entered an invalid value. Please try again.\n\n")
            aInt = False
    rounds = a
    aInt = False
    while aInt != True:
        a = input("Please enter how many players: ")
        b = str.isdigit(a)
        if b is True:
            a = int(a)
        else:
            print("Please try again!\n\n")
        aInt = isinstance(a, int)
        if aInt == True:
            if a <= 0:
                print("You cannot have a value of 0 or less. Please try again. \n\n")
                print("Setting to 1 Player")
                a = 1
            else:
                if a > 1:
                    print(str(a) + " Players entered.")
                if a == 1:
                    print(str(a) + " Player entered.")
        if aInt == False:
            print("You entered an invalid value. Please try again.\n\n")
            aInt = False
    numbers = a
    playersNum = numbers
    aInt = False
    while aInt != True:
        a = input("Please enter number of slots: ")
        b = str.isdigit(a)
        if b is True:
            a = int(a)
        else:
            print("Please try again!\n\n")
        aInt = isinstance(a, int)
        if aInt == True:
            if a <= 1:
                print("You cannot have a value of 1 or less. Please try again. \n\n")
                print("Setting to 2 slots")
                a = 2
            else:    
                print(str(a) + " Rounds entered.")
        if aInt == False:
            print("You entered an invalid value. Please try again.\n\n")
            aInt = False
    max = a
    maxPlayers = max
    return rounds, playersNum, maxPlayers

def sortNames(list):
    #Sorts list by priority, based on value (0, 1, 2)
    #2 would mean, 2 missed games
    toBeSorted = list
    numOfItems = len(toBeSorted)
    list1=[]
    list2=[]
    list3=[]
    if numOfItems > playersNum:
        numOfItems = playersNum
    for i in range(numOfItems):
        names = toBeSorted[i][0]
        num = toBeSorted[i][1]
        if num == 0:
            b = (names, num)
            list1.append(b)
            #print("added to list1")
        elif num == 1:
            b = (names, num)
            list2.append(b)
            #print("added to list2")
        else:
            b = (names, num)
            list3.append(b)
            #print("added to list3")
    listSorted=[]
    listSorted.extend(list3)
    listSorted.extend(list2)
    listSorted.extend(list1)        
    return listSorted

def makeTeams(playinglist):
    #split teams evenly, only split name list in half
    #code to take in maxPlayers variable
    a = len(playinglist)
    tempList = playinglist
    teamOne=[]
    teamTwo=[]
    teamOneCount=0
    teamTwoCount=0
    aCount=a/2
    for i in range(a):
        if teamOneCount >= aCount:
            c = tempList.pop()
            teamTwo.append(c)
        elif teamTwoCount >= aCount:
            c = tempList.pop()
            teamOne.append(c)
        else:
            b = random.randrange(1,100)
            if b >= 50:
                c = tempList.pop()
                teamOne.append(c)
                teamOneCount+=1
                #print("team 1: " + str(teamOneCount))
            else:
                c = tempList.pop()
                teamTwo.append(c)
                teamTwoCount+=1
                #print("team 2: " + str(teamTwoCount))
    tempList.extend(teamOne)
    tempList.extend(teamTwo)
    return teamOne, teamTwo, tempList

def playingList(nameEntries):
    a = maxPlayers
    tempList = nameEntries
    tempList.reverse()
    nowPlaying = []
    notPlaying = []
    for i in range(a):
        b = tempList.pop()
        nowPlaying.append(b)
    c = len(tempList)
    for i in range(c):
        b = tempList.pop()
        notPlaying.append(b)
    return nowPlaying, notPlaying

def enterPlayers():
    newPlayers = []
    a = playersNum
    for i in range(a):
        name = input("Please Enter a name: ")
        print("Player: "+name + " has been entered.")
        count = 0
        b = (name, count)
        newPlayers.append(b)
    return newPlayers

def limitValue(listN):
    a = len(listN)
    nameList = listN
    tempList = []
    for i in range(a):
        name = nameList[i][0]
        count = nameList[i][1]
        if count > 2:
            count = 2
        elif count < 0:
            count = 0
        b = (name, count)
        tempList.append(b)
    return tempList

def resetCount(listN):
    a = len(listN)
    nameList = listN
    tempList = []
    for i in range(a):
        name = nameList[i][0]
        count = 0
        b = (name, count)
        tempList.append(b)
    return (tempList)

def addCount(listN):
    a = len(listN)
    nameList = listN
    tempList = []
    for i in range(a):
        name = nameList[i][0]
        count = nameList[i][1]
        count += 1
        b = (name, count)
        tempList.append(b)
    return (tempList)

def combinelist(nowplay, notplay):
    tempList = []
    tempList.extend(nowplay)
    tempList.extend(notplay)
    return tempList

def stats():
    print("==========STATS:============")
    if rounds == 1:
        print("Number of Rounds to play: \t" + str(rounds) + " Round")
    else:
        print("Number of Rounds to play: \t" + str(rounds) + " Rounds")
    print("Number of Players: \t\t" + str(playersNum) + " Players")
    print("Number of slots open: \t\t" + str(maxPlayers) + " Slots")
    print("number of listed players:\t\t" + str(len(nameEntries)))

def startRounds(nameEntries):
    a = rounds
    roundnum = 1
    for i in range(a):
        input("\n\t\tPress any key to continue...")
        #print("==\tStarting Round " + str(roundnum)+"\t==\n")
        roundnum += 1
        nameEntries = sortNames(nameEntries)
        nameEntries = limitValue(nameEntries)
        nowPlaying, notPlaying = playingList(nameEntries)
        print("\n\n"+"="*10+ "Now Playing:"+"="*10)
        prettyDisplay_list(nowPlaying)
        print("="*10+ "Now in waiting:"+"="*10)
        prettyDisplay_list(notPlaying)
        nowPlaying = resetCount(nowPlaying)
        notPlaying = addCount(notPlaying)
        teamOne,teamTwo,nowPlaying = makeTeams(nowPlaying)
        #print("="*10 + "Team One:" + "="*10)
        #prettyDisplay(teamOne)
        #print("="*10 + "Team Two:" + "="*10)
        #prettyDisplay(teamTwo)
        teamsDisplay(teamOne, teamTwo)
        nameEntries = combinelist(nowPlaying, notPlaying)
        #print(nameEntries)

def teamsDisplay(teamOne, teamTwo):
    a1 = teamOne
    a2 = teamTwo
    playersNum = max(len(a1), len(a2))
    a11=len(a1)
    a22=len(a2)
    print("")
    print("{:=^25}".format("Team One") + "#" + "{:=^25}".format("Team Two"))
    for i in range(playersNum):
        a = teamOne[i][0]
        b = teamTwo[i][0]
        print("||"+"{:^23}".format(a+" ") + "|" + "{:^23}".format(" "+b)+"||")
    print("{:=^25}".format("") + "#" + "{:=^25}".format(""))

def prettyDisplay(listN):
    tempList = listN
    nameDisplay = []
    a = len(tempList)
    #print("", end="")
    for i in range(a):
        name = tempList[i][0]
        print(" "+'{:^15}'.format(name), end="\n")
    print("" ,end="\n")

def prettyDisplay_list(listN):
    tempList = listN
    nameDisplay = []
    a = len(tempList)
    b = 1
    print("", end="")
    for i in range(a):
        name = tempList[i][0]
        
        c = b%2
        b +=1
        if c == 1:
            print(" "+'{:^15}'.format(name), end="")
        if c == 0:
            print(" "+'{:^15}'.format(name), end="\n")
    print("")

#TODO: Collect number of variables to use from USER
# 1. Rounds, number of players, MaxNumber of players
# 2. randomize a list, and name entry

rounds, playersNum, maxPlayers = userinput()
nameEntries = enterPlayers() # Line to manually enter names

#nameEntries = (['Aaron', 2],['Daniela', 2],['dsgrh', 0],['Brannnn', 0], ['Looolla', 0], ['Brian', 0], ['Brian2', 0], ['Brian3', 0], ['AaronNA', 0],['Daniela2', 0],['Mdohwe', 0],['Foella', 0], ['SmomMo', 0], ['Bully', 0], ['Cowy', 0], ['Brfsn3', 0])
#print(nameEntries)
#nameEntries = sortNames(nameEntries)
#print(nameEntries)
#stats()

#some error checking, make sure, values are between (0-2)
#nameEntries = limitValue(nameEntries)

#nowPlaying,notPlaying = playingList()
#print("Now Playing:\n" + str(nowPlaying))
#print("Waiting:\n" + str(notPlaying))

#resets value to 0, for each of the playing
#adds 1 to value, for each round missed
#nowPlaying = resetCount(nowPlaying)
#notPlaying = addCount(notPlaying)
#print(nowPlaying)
#print(notPlaying)

#teamOne,teamTwo,nowPlaying = makeTeams(nowPlaying)
#print("Team 1:\n" + str(teamOne))
#print("Team 2:\n" + str(teamTwo))

#combine lists again
#nameEntries = combinelist(nowPlaying, notPlaying)

startRounds(nameEntries)
