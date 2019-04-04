import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))
from cube import Cube
from layer1 import layer1

# input: Cube object
# layer1.py
# layer2.py
# layer3.py
# output: moves list

def beginners(config):
    cube = Cube(config)
    layer1(cube)
    print("layer 1 soln: %s" % cube.soln)
    print("# of moves so far: %s" % cube.total)


# unit test
beginners("FUUBUUDRBLBBBRLBLBFDDBFRUURFFDFDDFDUDDRLLLRRLLRLFBURFU")