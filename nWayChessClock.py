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
		os.system('clear')
		# announce last turn time
		if nRound > 1 or nPlayer > 0:
		    outString = nameList[nPlayer-1] + "'s turn took " + str(np.round(tTurn, 1)) + " seconds" 
		    stdout.write("%s\n" % outString)	
			outString = nameList[nPlayer-1] + "'s total time changed by " + str(np.round(tIncrement-tTurn, 1)) + " seconds" 
			stdout.write("%s\n" % outString)
			outString = "We've been playing for " + str(int((time.time()-tTot0)/60.0)) + " minutes" 
			stdout.write("%s\n" % outString)
			outString = "_____________________________________________________" 
			stdout.write("%s\n\n" % outString)	
			stdout.flush()
		# announce who's turn it is currently
		outString = "Round " + str(nRound) + ", " + nameList[nPlayer] + "'s turn"
		stdout.write("%s\n\n" % outString)	
		stdout.flush()
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
		t0 = time.time()
		cmdIn = input("press enter to move on to the next player's turn...")
		t1 = time.time()
		tTurn = t1-t0
		tList[nPlayer] -= tTurn
		tList[nPlayer] += tIncrement		
	nRound+=1




















