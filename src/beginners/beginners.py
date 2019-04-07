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
    Calls solving algorithms for each layer
    """
    cube = Cube(config, test)
    print("initial cube state: \n")
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
beginners("FUUBUUDRBLBBBRLBLBFDDBFRUURFFDFDDFDUDDRLLLRRLLRLFBURFU")
# test_layer2("RLBRUUFLULFURRBRRRLBBBFFFFFDDDDDDDDDFUUFLULLLRUURBLBBB")
# test_layer2("RLBRULFLULFURRBRRRLBBBFFFFFDDDDDDDDDFUUFLULLLRUURBUBBB")

# test = True
# config1 = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube = Cube(config1, test)
# soln2 = "U1 F2 U3 F3 R3 D3 L1 F3 D3 R1 D2 B2 U3 B2 L2 D1 B2 L2 B2 U1"
# execute_moves(cube, soln2.split())
# print("scrambled cube:")
# print(cube)
# layer1(cube)
# layer2(cube)