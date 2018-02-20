import numpy as np
import sys
from sys import stdout
import time
from time import sleep
import os


# time paramters
tStart     = float(sys.argv[1]) 
tIncrement = float(sys.argv[2])

# player names
nameList   = []
for name in sys.argv[3:]: nameList.append(str(name))
nPlayers   = len(nameList)

# initialize time list
tList = np.zeros(nPlayers)
tList += tStart

outStringAll  = ""
nRound = 1
tTot0 = time.time()
# loop over rounds
while True:
# loop over players
    for nPlayer in range(len(nameList)):
        # clear terminal output
        os.system('clear')
        if nRound > 1 or nPlayer > 0:
            # print last turn time
            outString = nameList[nPlayer-1] + "'s turn took " + str(np.round(tTurn, 1)) + " seconds" 
            stdout.write("%s\n" % outString)
            # print net change in time remaing for last player
            outString = nameList[nPlayer-1] + "'s total time changed by " + str(np.round(tIncrement-tTurn, 1)) + " seconds" 
            stdout.write("%s\n" % outString)
            # print total time we've been playing
            outString = "We've been playing for " + str(int((time.time()-tTot0)/60.0)) + " minutes" 
            stdout.write("%s\n" % outString)
            outString = "_____________________________________________________" 
            stdout.write("%s\n\n" % outString)	
            stdout.flush()
        # print who's turn it is currently
        outString = "Round " + str(nRound) + ", " + nameList[nPlayer] + "'s turn"
        stdout.write("%s\n\n" % outString)	
        stdout.flush()
        # make table of time remaining, put a * next to the player whose turn it is
        for i in range(nPlayers):
            mins = int(np.floor_divide(tList[i], 60))
            secs = int(np.round(tList[i] - mins*60, 0))
            if i == nPlayer:
                stringPrefix = '*'
            else:
                stringPrefix = ' '	
            outString = stringPrefix + nameList[i].ljust(10) + "  " + str(mins) + "." + str(secs)
            stdout.write("%s \n" % outString)
            outString = "_____________________________________________________" 
        stdout.write("%s\n\n" % outString)	
        stdout.flush()
        t0 = time.time() # time at start of player's turn
        cmdIn = input("press enter to move on to the next player's turn \ntype 'end' then press enter to end the game\n")
        t1 = time.time() # time at end of player's turn
        # calculate turn time, subtract from total time
        tTurn = t1-t0
        tList[nPlayer] -= tTurn
        # end the game?
        if cmdIn == "end": break;
        # add increment to total time
        tList[nPlayer] += tIncrement
    if cmdIn == "end": break;
    nRound+=1

# end of the game output
os.system('clear')
outString = "THE GAME IS OVER!"  
stdout.write("%s\n" % outString)
outString = "full rounds played: " + str(nRound)
stdout.write("%s\n" % outString)
outString = "total game time: " + str(int((time.time()-tTot0)/60.0)) + " minutes" 
stdout.write("%s\n" % outString)
outString = "time per round: " + str(int((time.time()-tTot0)/nRound) + " seconds" 
stdout.write("%s\n" % outString)
for i in range(nPlayers):
    mins = int(np.floor_divide(tList[i], 60))
    secs = int(np.round(tList[i] - mins*60, 0))
    outString = nameList[i].ljust(10) + "  " + str(mins) + "." + str(secs)
    stdout.write("%s \n" % outString)
stdout.flush()
    



















