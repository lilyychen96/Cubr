# modules imported
import cv2
import numpy as np
import math

################### GLOBAL VARIABLES ###################
SQUARELEN = 133
# Hue & Saturation list
# Blue, Green, Yellow, White, Red, Orange
HSLIST = [[105, 177], [80,177], [30, 177], [125, 60], [165, 177], [12, 177]]
COLOR = ['b', 'g', 'y', 'w', 'r', 'o']
MIRROR = True
# stores mapped cube
CUBE = [["N" for i in range(9)] for j in range(6)]
########################################################

# distance formula between 2 points
def distance(x1, y1, x2, y2):
	return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

# finds the color in a given region of the image
def findColor(img, leftX, bottomY):
	hAvg = 0
	sAvg = 0
	colorDist = []
	for row in range(bottomY, bottomY + SQUARELEN):
		for col in range(leftX, leftX + SQUARELEN):
			# hue 
			hAvg += img[row][col][0]
			# saturation
			sAvg += img[row][col][1]
	hAvg /= (SQUARELEN ** 2)
	sAvg /= (SQUARELEN ** 2)

	# DEBUG HSV values in a grid
	# print(hAvg)
	# print(sAvg)

	colorDist.append(distance(hAvg, sAvg, HSLIST[0][0], HSLIST[0][1]))
	colorDist.append(distance(hAvg, sAvg, HSLIST[1][0], HSLIST[1][1]))
	colorDist.append(distance(hAvg, sAvg, HSLIST[2][0], HSLIST[2][1]))	
	colorDist.append(distance(hAvg, sAvg, HSLIST[3][0], HSLIST[3][1]))
	colorDist.append(distance(hAvg, sAvg, HSLIST[4][0], HSLIST[4][1]))
	colorDist.append(distance(hAvg, sAvg, HSLIST[5][0], HSLIST[5][1]))

	minDist = 10000
	minIndex = 0
	counter = 0
	for dist in colorDist:
		if dist < minDist:
			minDist = dist
			minIndex = counter
		counter += 1

	return COLOR[minIndex]

# map the colors present on the cube face
def mapCubeFace(hsv):
	topLeft = findColor(hsv, 450, 150)
	topMid = findColor(hsv, 583, 150)
	topRight = findColor(hsv, 716, 150)
	midLeft = findColor(hsv, 450, 283)
	center = findColor(hsv, 583, 283)
	midRight = findColor(hsv, 716, 283)
	lowerLeft = findColor(hsv, 450, 416)
	lowerMid = findColor(hsv, 583, 416)
	lowerRight = findColor(hsv, 716, 416)

	# fill the mapped cube depending on center color
	index = COLOR.index(center)
	CUBE[index][0] = topLeft
	CUBE[index][1] = topMid
	CUBE[index][2] = topRight
	CUBE[index][3] = midLeft
	CUBE[index][4] = center
	CUBE[index][5] = midRight
	CUBE[index][6] = lowerLeft
	CUBE[index][7] = lowerMid
	CUBE[index][8] = lowerRight
	print(CUBE[index])

def mapToStr():
	output = " " * 4 + CUBE[3][0] +  CUBE[3][1] + CUBE[3][2] + " " * 7 + "\n" \
	+ " " * 4 + CUBE[3][3] +  CUBE[3][4] + CUBE[3][5] + " " * 7 + "\n" \
	+ " " * 4 + CUBE[3][6] +  CUBE[3][7] + CUBE[3][8] + " " * 7 + "\n" \
	+ CUBE[1][0] +  CUBE[1][1] + CUBE[1][2] + " " + CUBE[4][0] +  CUBE[4][1] + CUBE[4][2] + " " + CUBE[0][0] +  CUBE[0][1] + CUBE[0][2] + " " + CUBE[5][0] +  CUBE[5][1] + CUBE[5][2] + "\n" \
	+ CUBE[1][3] +  CUBE[1][4] + CUBE[1][5] + " " + CUBE[4][3] +  CUBE[4][4] + CUBE[4][5] + " " + CUBE[0][3] +  CUBE[0][4] + CUBE[0][5] + " " + CUBE[5][3] +  CUBE[5][4] + CUBE[5][5] + "\n" \
	+ CUBE[1][6] +  CUBE[1][7] + CUBE[1][8] + " " + CUBE[4][6] +  CUBE[4][7] + CUBE[4][8] + " " + CUBE[0][6] +  CUBE[0][7] + CUBE[0][8] + " " + CUBE[5][6] +  CUBE[5][7] + CUBE[5][8] + "\n" \
	+ " " * 4 + CUBE[2][0] +  CUBE[2][1] + CUBE[2][2] + " " * 7 + "\n" \
	+ " " * 4 + CUBE[2][3] +  CUBE[2][4] + CUBE[2][5] + " " * 7 + "\n" \
	+ " " * 4 + CUBE[2][6] +  CUBE[2][7] + CUBE[2][8] + " " * 7
	print(output)
				
def main():
	cam = cv2.VideoCapture(0)
	while True:
	    retVal, img = cam.read()
	    if MIRROR: 
	        img = cv2.flip(img, 1)

	    # convert to hsv color space
	    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	    cv2.namedWindow('Cube State',cv2.WINDOW_NORMAL)
	    cv2.resizeWindow('Cube State', 1000,1000)

	    # blue color detection
	    blueLower = [98,100,20]
	    blueUpper = [112,255,255]
	    blueLower = np.array(blueLower, dtype = "uint8")
	    blueUpper = np.array(blueUpper, dtype = "uint8")

	    # green color detection
	    greenLower = [60,100,100]
	    greenUpper = [100,255,255]
	    greenLower = np.array(greenLower, dtype = "uint8")
	    greenUpper = np.array(greenUpper, dtype = "uint8")

	    # yellow color detection
	    yellowLower = [20, 100, 100]
	    yellowUpper = [40, 255, 255]
	    yellowLower = np.array(yellowLower, dtype = "uint8")
	    yellowUpper = np.array(yellowUpper, dtype = "uint8")

	    # white color detection
	    whiteLower = [90, 10, 130]
	    whiteUpper = [160, 110, 255]
	    whiteLower = np.array(whiteLower, dtype = "uint8")
	    whiteUpper = np.array(whiteUpper, dtype = "uint8")

	    # red color detection
	    redLower = [150, 100, 100]
	    redUpper = [180, 255, 255]
	    redLower = np.array(redLower, dtype = "uint8")
	    redUpper = np.array(redUpper, dtype = "uint8")

	    # orange color detection
	    orangeLower = [10, 100, 100]
	    orangeUpper = [15, 255, 255]
	    orangeLower = np.array(orangeLower, dtype = "uint8")
	    orangeUpper = np.array(orangeUpper, dtype = "uint8")

	    # black and white
	    maskBlue = cv2.inRange(hsv, blueLower, blueUpper)
	    maskGreen = cv2.inRange(hsv, greenLower, greenUpper)
	    maskYellow = cv2.inRange(hsv, yellowLower, yellowUpper)
	    maskWhite = cv2.inRange(hsv, whiteLower, whiteUpper)
	    maskRed = cv2.inRange(hsv, redLower, redUpper)
	    maskOrange = cv2.inRange(hsv, orangeLower, orangeUpper)

	    # bitwise & with img and mask
	    mask = cv2.bitwise_or(maskBlue,maskGreen)
	    mask = cv2.bitwise_or(mask,maskYellow)
	    mask = cv2.bitwise_or(mask,maskWhite)
	    mask = cv2.bitwise_or(mask,maskRed)
	    mask = cv2.bitwise_or(mask,maskOrange)
	    res = cv2.bitwise_and(img,img, mask = mask)
	    
	    # draw in area where cube will be scanned
	    cv2.rectangle(res,(450,150),(850,550),(0,255,0),3)
	    cv2.line(res,(588,150),(588,550),(0,255,0),3)
	    cv2.line(res,(716,150),(716,550),(0,255,0),3)
	    cv2.line(res,(450,283),(850,283),(0,255,0),3)
	    cv2.line(res,(450,416),(850,416),(0,255,0),3)

	    # display the frame
	    cv2.imshow('Cube State', res)

	    key = cv2.waitKey(1)
	    # esc to quit
	    if  key == 27: 
	        break

	    # write logic for enter key
	    if key == 32:
	    	mapCubeFace(hsv)
	    	mapToStr()

	cv2.destroyAllWindows()

if __name__ == '__main__':
    main()