import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))
from cube import Cube
from layer1 import layer1
from layer2 import layer2
from layer3 import layer3
from moves import execute_moves

# input: Cube object
# layer1.py
# layer2.py
# layer3.py
# output: moves list

def beginners(config, test=False):
    """
    Calls solving algorithms for each layer from a given cube state from the
    cube state detection module; outputs the resulting moves list, converted
    into a string, to the Arduino.

    NOTE: depending on top-level module, output may be maintained as a list.
    """
    cube = Cube(config, test)
    # print("initial cube state:")
    # print(cube)
    # print("\n\n")

    layer1(cube)
    # soln1 = cube.soln
    # len1 = cube.total
    # print("# of layer 1 moves: %s" % len1)
    # print("layer 1 soln: %s\n\n" % soln1)

    layer2(cube)
    # soln2 = cube.soln[len(soln1):]
    # len2 = cube.total - len1
    # print("# of layer 2 moves: %s" % len2)
    # print("layer 2 soln: %s\n\n" % soln2)

    layer3(cube)
    # soln3 = cube.soln[len(soln1)+len(soln2):]
    # len3 = cube.total - len1 - len2
    # print("# of layer 3 moves: %s" % len3)
    # print("layer 3 soln: %s\n\n" % soln3)

    print("cube solved? %s\n" % cube.solved)
    print("# of moves: %s\n" % cube.total)
    print("solution:\n%s\n\n\n" % cube.soln)

    return cube.soln

import random
def random_scramble():
    config = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
    cube = Cube(config, True)
    moves = [
        "U1", "U2", "U3", "R1", "R2", "R3", "F1", "F2", "F3",
        "D1", "D2", "D3", "L1", "L2", "L3", "B1", "B2", "B3"
    ]

    scramble = ""
    for i in range(random.randint(20,25)):
        scramble += moves[random.randint(0,17)] + " "

    print("scramble: %s" % scramble)
    execute_moves(cube, scramble.split())
    return cube


# # tests
# beginners("FUUBUUDRBLBBBRLBLBFDDBFRUURFFDFDDFDUDDRLLLRRLLRLFBURFU")
# beginners("RLBRUUFLULFURRBRRRLBBBFFFFFDDDDDDDDDFUUFLULLLRUURBLBBB")

config = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube = Cube(config, True)
# scramble1 = "U1 F2 U3 F3 R3 D3 L1 F3 D3 R1 D2 B2 U3 B2 L2 D1 B2 L2 B2 U1"
# execute_moves(cube, scramble1.split())
# beginners(cube.config)

# cube2 = Cube(config, True)
# scramble2 = "R1 U1 R2 U2 D1 R2 L1 F1 R1 D3 L2 U1 L2 B1 D3 L3 R3 U3 B3 R3 D3 R2 D3 B1 F3"
# execute_moves(cube2, scramble2.split())
# beginners(cube2.config)

# cube3 = Cube(config, True)
# scramble3 = "R3 F3 U1 D2 L2 B1 F2 D1 U2 R3 F2 U2 D1 F1 B3 L2 D3 U1 L1 D1 R2 U1 L3 U1 D3"
# execute_moves(cube3, scramble3.split())
# beginners(cube3.config)

# cube4 = Cube(config, True)
# scramble4 = "U3 B3 L3 F3 R2 L3 U3 D2 B1 L3 U2 F2 D2 L3 D3 U2 L1 B1 L3 D3 U3 L3 D1 L3 R3"
# execute_moves(cube4, scramble4.split())
# beginners(cube4.config)

# cube5 = Cube("FLURUBDFBDRLURUBRBLLRDFFBUULLRDDUDDLUDFFLLRFDFBRBBRUBF")
# beginners(cube5.config)

# cube6 = Cube(config, True)
# execute_moves(cube6, "L3 R2 L3 U1 D3 U2 R2 R3 F3 B2 L3 F3 L3 B3 U2 R1 B1 F2 U3 F1 D1 R2 F3 B2 D3".split())
# beginners(cube6.config)

# cube7 = Cube(config, True)
# execute_moves(cube7, "R1 F1 B1 L2 L2 R2 R3 F3 F1 L3 F2 F2 D1 B3 D3 U1 L1 U3 F2 B1 F1 U3".split())
# beginners(cube7.config)

# uncomment to test
# breaks at 2nd layer
# cube8 = Cube(config, True)
# execute_moves(cube8, "B2 L2 R2 L2 R3 U3 F1 B2 U2 L2 U2 U2 L1 D3 B3 R1 R3 R3 R3 D1".split())
# beginners(cube8.config)

cube = random_scramble()
print(cube)
beginners(cube.config)

