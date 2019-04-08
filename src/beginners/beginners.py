import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))
from cube import Cube
from layer1 import layer1
from layer2 import layer2
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
    into a solution string, to the Arduino
    """
    cube = Cube(config, test)
    print("initial cube state:")
    print(cube)
    print("\n\n")

    layer1(cube)
    soln1 = cube.soln
    len1 = cube.total
    print("# of layer 1 moves: %s" % len1)
    print("layer 1 soln: %s\n\n" % soln1)

    layer2(cube)
    soln2 = cube.soln[len(soln1):]
    len2 = cube.total - len1
    print("# of layer 2 moves (so far): %s" % len2)
    print("layer 2 soln (so far): %s\n\n" % soln2)

    print("# of moves so far: %s" % cube.total)
    print("full solution so far: %s\n\n" % cube.soln)

# def test_layer2(config):
#     cube = Cube(config)
#     print("initial cube state: \n")
#     print(cube)
#     print("\n\n")

#     layer2(cube)

# tests
# beginners("FUUBUUDRBLBBBRLBLBFDDBFRUURFFDFDDFDUDDRLLLRRLLRLFBURFU")
# beginners("RLBRUUFLULFURRBRRRLBBBFFFFFDDDDDDDDDFUUFLULLLRUURBLBBB")
# beginners("RLBRULFLULFURRBRRRLBBBFFFFFDDDDDDDDDFUUFLULLLRUURBUBBB")

# test = True
# config = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube = Cube(config, test)
# scramble1 = "U1 F2 U3 F3 R3 D3 L1 F3 D3 R1 D2 B2 U3 B2 L2 D1 B2 L2 B2 U1"
# execute_moves(cube, scramble1.split())
# print("scrambled cube:")
# print(cube)
# layer1(cube)
# print(cube)
# layer2(cube)
# print(cube)

# test = True
# config = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube2 = Cube(config, test)
# scramble2 = "R1 U1 R2 U2 D1 R2 L1 F1 R1 D3 L2 U1 L2 B1 D3 L3 R3 U3 B3 R3 D3 R2 D3 B1 F3"
# execute_moves(cube2, scramble2.split())
# print("scrambled cube:")
# print(cube2)
# layer1(cube2)
# print(cube2)
# layer2(cube2)
# print(cube2)

# test = True
# config = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube3 = Cube(config, test)
# scramble3 = "R3 F3 U1 D2 L2 B1 F2 D1 U2 R3 F2 U2 D1 F1 B3 L2 D3 U1 L1 D1 R2 U1 L3 U1 D3"
# execute_moves(cube3, scramble3.split())
# print("scrambled cube:")
# print(cube3)
# layer1(cube3)
# print(cube3)
# layer2(cube3)
# print(cube3)

# @NOTE: this test breaks on placing Corner.DRB, need to debug white corners
#        and debug white cross
test = True
config = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
cube4 = Cube(config, test)
scramble4 = "U3 B3 L3 F3 R2 L3 U3 D2 B1 L3 U2 F2 D2 L3 D3 U2 L1 B1 L3 D3 U3 L3 D1 L3 R3"
execute_moves(cube4, scramble4.split())
print("scrambled cube:")
print(cube4)
layer1(cube4)
print(cube4)
layer2(cube4)
print(cube4)
