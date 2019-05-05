# input: cube state configuration string
# call a solving method (e.g. beginners.py)
# get moves list from this
# convert to solution string
# output: solution string
import sys, os
import cubeState
import argparse
import serial
import time
parser = argparse.ArgumentParser()
parser.add_argument("--solver", help="Select either twophase or beginners solver")
args = parser.parse_args()

if args.solver == "beginners":
	sys.path.insert(0, os.path.abspath('beginners'))
	print(sys.path)
	import beginners as sv

else:
	
	sys.path.insert(0, os.path.abspath('twoPhase'))
	import twoPhase.solver as sv

def mapToArduino(sol):
	solList = sol.split()
	remappedList = ['<']
	for elem in solList:
		if elem == "F1":
			remappedList.append('Q')
		elif elem == "F2":
			remappedList.append('W')		
		elif elem == "F3":
			remappedList.append('E')
		elif elem == "R1":
			remappedList.append('R')		
		elif elem == "R2":
			remappedList.append('T')
		elif elem == "R3":
			remappedList.append('Y')		
		elif elem == "B1":
			remappedList.append('U')
		elif elem == "B2":
			remappedList.append('I')
		elif elem == "B3":
			remappedList.append('O')
		elif elem == "L1":
			remappedList.append('P')
		elif elem == "L2":
			remappedList.append('A')
		elif elem == "L3":
			remappedList.append('S')
		elif elem == "U1":
			remappedList.append('D')
		elif elem == "U2":
			remappedList.append('F')
		elif elem == "U3":
			remappedList.append('G')
		elif elem == "D1":
			remappedList.append('H')
		elif elem == "D2":
			remappedList.append('J')
		elif elem == "D3":
			remappedList.append('K')
		else:
			continue
	remappedList.append('>')
	return "".join(remappedList)

def reverse_scramble(sol):
	remappedList = ['<']
	for elem in sol:
		if elem == "E":
			remappedList.append('Q')
		elif elem == "W":
			remappedList.append('W')		
		elif elem == "Q":
			remappedList.append('E')
		elif elem == "Y":
			remappedList.append('R')		
		elif elem == "T":
			remappedList.append('T')
		elif elem == "R":
			remappedList.append('Y')		
		elif elem == "O":
			remappedList.append('U')
		elif elem == "I":
			remappedList.append('I')
		elif elem == "U":
			remappedList.append('O')
		elif elem == "S":
			remappedList.append('P')
		elif elem == "A":
			remappedList.append('A')
		elif elem == "P":
			remappedList.append('S')
		elif elem == "G":
			remappedList.append('D')
		elif elem == "F":
			remappedList.append('F')
		elif elem == "D":
			remappedList.append('G')
		elif elem == "K":
			remappedList.append('H')
		elif elem == "J":
			remappedList.append('J')
		elif elem == "H":
			remappedList.append('K')
		else:
			continue
	remappedList.append('>')
	remappedList.reverse()
	remappedList[0] = '<'
	remappedList[-1] = '>'
	return "".join(remappedList)

# DEBG
# output = "FLURUBDFBDRLURUBRBLLRDFFBUULLRDDUDDLUDFFLLRFDFBRBBRUBF"

# call cubeState detection
output = cubeState.main()

if args.solver == "beginners":
	a = sv.beginners(output)
else:
	# solve with a maximum of 20 moves and a timeout of 2 seconds for example
	a = sv.solve(output, 20, 2)

sol = mapToArduino(a)
# scramble
scram = reverse_scramble(sol)
print(a)
print(scram)
print(sol)

# communicate to Arduino using pyserial
ser = serial.Serial('/dev/tty.usbmodem14101',9600)
time.sleep(5)
c = ser.write(scram.encode())
time.sleep(30)
b = ser.write(sol.encode())
ser.close()

