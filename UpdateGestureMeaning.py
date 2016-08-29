#TAKE TEXT FROM USER

import cv2
import numpy as np
temporaryTextData=list('')
load=list('')

print 'ENTER TOTAL SHOWN GESTURES'
numberOfGestures=raw_input()

#Taking values for all the provided gestures
print 'ENTER TEXT ACCORDINGLY'
for i in range(int(numberOfGesturesl)):
    currentMeaning=raw_input()
    temporaryTextData.append((currentMeaning))
	
#Saving the data to the text file UserGestureMeaningDataFile.txt
np.savetxt('UserGestureMeaningDataFile.txt',temporaryTextData,delimiter=" ",fmt="%s")
load=np.loadtxt('UserGestureMeaningDataFile.txt',dtype=np.str,delimiter=" ")

#print all the given gesture meanings
print load


