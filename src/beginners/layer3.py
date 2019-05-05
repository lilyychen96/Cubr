import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))

from moves import execute_moves
from cube import Cube
from facelet import Color as Cl
from layer2 import is_f2l
from oll import oll_state, oll_moves
from pll import pll_state, pll_moves


"""
third layer algorithms: OLL ("Orient Last Layer") and PLL ("Permute Last Layer")
"""
def is_oll(cube_state):
    """
    Checks if the cube has reached the OLL state
    """
    return (is_f2l(cube_state) and (cube_state[0] == Cl.U) and
            (cube_state[1] == Cl.U) and (cube_state[2] == Cl.U) and
            (cube_state[3] == Cl.U) and (cube_state[4] == Cl.U) and
            (cube_state[5] == Cl.U) and (cube_state[6] == Cl.U) and
            (cube_state[7] == Cl.U) and (cube_state[8] == Cl.U))

def solve_oll(cube_obj):
    """
    Outputs the moves list for orienting the cubies in the top layer after
    solving the first two layers
    """
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_oll(cube_state):
        return

    # rotate top layer until matching state is found
    u_turns = 0
    state = oll_state(cube_state)
    temp = Cube(cube_obj.config)
    while ((state == 0) and (u_turns < 4)):
        # make temp cube object, execute U1
        execute_moves(temp, "U1")
        state = oll_state(temp.cb)
        print("OLL state: %s" % state)
        print(temp)
        u_turns += 1

    if (u_turns == 1):
        execute_moves(cube_obj, "U1")
    elif (u_turns == 2):
        execute_moves(cube_obj, "U2")
    elif (u_turns == 3):
        execute_moves(cube_obj, "U3")
    else:
        try:
            assert((u_turns < 4) and (state != 0))
        except AssertionError:
            print("cannot find matching top layer state...")

    moves_list = oll_moves(cube_obj, state)
    execute_moves(cube_obj, moves_list)

    try:
        assert(is_oll(cube_obj.cb))
        print("OLL completed", end="...")
        # print(cube_obj)
    except AssertionError:
        print("did not successfully complete OLL\n")

def is_pll(cube_state):
    """
    Checks if the cube has reached the PLL state (a.k.a. is fully solved)
    """
    return (is_oll(cube_state) and (cube_state[9] == cube_state[10]) and
            (cube_state[10] == cube_state[11]) and
            (cube_state[18] == cube_state[19]) and
            (cube_state[19] == cube_state[20]) and
            (cube_state[36] == cube_state[37]) and
            (cube_state[37] == cube_state[38]) and
            (cube_state[45] == cube_state[46]) and
            (cube_state[46] == cube_state[47]))

def solve_pll(cube_obj):
    """
    Outputs the moves list for permuting the cubies in the top layer after
    orienting the top layer cubies
    """
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_pll(cube_state):
        return

    # rotate top layer until matching state is found
    u_turns = 0
    state = pll_state(cube_state)
    temp = Cube(cube_obj.config)
    while ((state == 0) and (u_turns < 4)):
        # make temp cube object, execute U1
        execute_moves(temp, "U1")
        state = pll_state(temp.cb)
        # print("PLL state: %s" % state)
        # print(temp)
        u_turns += 1

    if (u_turns == 1):
        execute_moves(cube_obj, "U1")
    elif (u_turns == 2):
        execute_moves(cube_obj, "U2")
    elif (u_turns == 3):
        execute_moves(cube_obj, "U3")
    else:
        try:
            assert((u_turns < 4) and (state != 0))
        except AssertionError:
            print("cannot find matching top layer state...\n")

    moves_list = pll_moves(cube_obj, state)
    execute_moves(cube_obj, moves_list)

    try:
        assert(is_pll(cube_obj.cb))
        print("PLL completed", end="...")
        # print(cube_obj)
    except AssertionError:
        print("did not successfully complete PLL\n")

def layer3(cube_obj):
    """
    Calls the solving algorithms for the third/top layer: OLL and PLL
    """
    print("solving OLL")
    print(cube_obj)
    solve_oll(cube_obj)
    exit()
    # print(cube_obj)
    solve_pll(cube_obj)

    # spins top layer until everything lines up
    if (not cube_obj.solved):
        u_turns = 0
        found = False
        temp = Cube(cube_obj.config)
        while ((not found) and (u_turns < 4)):
            # make temp cube object, execute U1
            execute_moves(temp, "U1")
            if (temp.solved):
                found = True
            u_turns += 1

        if (u_turns == 1):
            execute_moves(cube_obj, "U1")
        elif (u_turns == 2):
            execute_moves(cube_obj, "U2")
        elif (u_turns == 3):
            execute_moves(cube_obj, "U3")
        else:
            try:
                assert(u_turns < 4)
            except AssertionError:
                print("cannot solve cube at PLL layer...\n")
                print(cube_obj)

    try:
        assert(cube_obj.solved)
        print("cube is fully solved!!!\n")
        print(cube_obj)
    except AssertionError:
        print("did not successfully solve cube at last layer...\n")
        print(cube_obj)
