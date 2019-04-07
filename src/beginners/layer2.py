import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))

from moves import execute_moves
from cube import Cube, find_edge, find_corner
from facelet import Move as Mv, Color as Cl, Corner as Cn, Edge as Ed
from layer1 import is_white_corners


"""
second layer algorithms: F2L ("first 2 layers")
"""
def is_f2l(cube_state, cubies):
    """
    Checks if the cube has reached the F2L state
    """
    return (is_white_corners(cube_state, cubies) and
        (cubies[Ed.FL] == tuple(sorted([Cl.F, Cl.L]))) and
        (cubies[Ed.FR] == tuple(sorted([Cl.F, Cl.R]))) and
        (cubies[Ed.BL] == tuple(sorted([Cl.B, Cl.L]))) and
        (cubies[Ed.BR] == tuple(sorted([Cl.B, Cl.R]))))

def move_FL(cube_obj, loc):
    """
    Returns the moves list to orient and position the FL edge
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Ed.UR:
        try:
            assert((cb[5] == Cl.F) or (cb[10] == Cl.F))
            if (cb[5] == Cl.F):
                assert(cb[10] == Cl.L)
                return ["U3", "F1", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[10] == Cl.D)
                assert(cb[5] == Cl.L)
                return ["L3", "U1", "L1", "U1", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UR])
    
    elif loc == Ed.UF:
        try:
            assert((cb[7] == Cl.F) or (cb[19] == Cl.F))
            if (cb[7] == Cl.F):
                assert(cb[19] == Cl.L)
                return ["U2", "F1", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[19] == Cl.F)
                assert(cb[7] == Cl.L)
                return ["U3", "L3", "U1", "L1", "U1", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UF])
    
    elif loc == Ed.UL:
        try:
            assert((cb[3] == Cl.F) or (cb[37] == Cl.F))
            if (cb[3] == Cl.F):
                assert(cb[37] == Cl.L)
                return ["U1", "F1", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[37] == Cl.D)
                assert(cb[3] == Cl.L)
                return ["U2", "L3", "U1", "L1", "U1", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UL])
    
    elif loc == Ed.UB:
        try:
            assert((cb[1] == Cl.F) or (cb[46] == Cl.F))
            if (cb[1] == Cl.F):
                assert(cb[46] == Cl.L)
                return ["F1", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[46] == Cl.F)
                assert(cb[1] == Cl.L)
                return ["U1", "L3", "U1", "L1", "U1", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.UB])

    elif loc == Ed.FR:
        try:
            assert((cb[23] == Cl.F) or (cb[12] == Cl.F))
            if (cb[23] == Cl.F):
                assert(cb[12] == Cl.R)
                return ["R1", "U3", "R3", "U3", "F3", "U1", "F2", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[12] == Cl.F)
                assert(cb[23] == Cl.R)
                return ["R1", "U3", "R3", "U3", "F3", "U1", "F1", "U1", "L3", "U1", "L1", "U1", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.FR])
    
    elif loc == Ed.FL:
        try:
            assert((cb[21] == Cl.F) or (cb[41] == Cl.F))
            if (cb[41] == Cl.F):
                assert(cb[21] == Cl.L)
                return ["L3", "U1", "L1", "U1", "F1", "U3", "F3", "U1", "L3", "U1", "L1", "U1", "F1", "U3", "F3"]
            else: # cb[41] == Cl.F)
                assert((cb[21] == Cl.F) and (cb[41] == Cl.L))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.FL])
    
    elif loc == Ed.BR:
        try:
            assert((cb[14] == Cl.F) or (cb[48] == Cl.F))
            if (cb[14] == Cl.F):
                assert(cb[48] == Cl.L)
                return ["B1", "U3", "B3", "U3", "R3", "U1", "R1", "U1", "F1", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[48] == Cl.F)
                assert(cb[14] == Cl.L)
                return ["B1", "U3", "B3", "U3", "R3", "U1", "R1", "U2", "L3", "U1", "L1", "U1", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.BR])
    
    else: #if loc == Ed.BL
        try:
            assert((cb[39] == Cl.F) or (cb[50] == Cl.F))
            if (cb[39] == Cl.F):
                assert(cb[50] == Cl.L)
                return ["B3", "U1", "B1", "U1", "L1", "U3", "L3", "U3", "F1", "U3", "F3", "U3", "L3", "U1", "L1"]
            else: # cb[50] == Cl.F)
                assert(cb[39] == Cl.L)
                return ["B3", "U1", "B3", "U3", "R1", "U1", "R1", "U2", "R1", "U3", "R1", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.BL])

    return []

def move_FR(cube_obj, loc):
    """
    Returns the moves list to orient and position the FL edge
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Ed.UR:
        try:
            assert((cb[5] == Cl.F) or (cb[10] == Cl.F))
            if (cb[5] == Cl.F):
                assert(cb[10] == Cl.R)
                return ["U3", "F3", "U1", "F1", "U1", "R1", "U3", "R3"]
            else: # cb[10] == Cl.D)
                assert(cb[5] == Cl.R)
                return ["U2", "R1", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UR])
    
    elif loc == Ed.UF:
        try:
            assert((cb[7] == Cl.F) or (cb[19] == Cl.F))
            if (cb[7] == Cl.F):
                assert(cb[19] == Cl.R)
                return ["U2", "F3", "U1", "F1", "U1", "R1", "U3", "R3"]
            else: # cb[19] == Cl.F)
                assert(cb[7] == Cl.R)
                return ["U1", "R1", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UF])
    
    elif loc == Ed.UL:
        try:
            assert((cb[3] == Cl.F) or (cb[37] == Cl.F))
            if (cb[3] == Cl.F):
                assert(cb[37] == Cl.R)
                return ["U1", "F3", "U1", "F1", "U1", "R1", "U3", "R3"]
            else: # cb[37] == Cl.D)
                assert(cb[3] == Cl.R)
                return ["R1", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UL])
    
    elif loc == Ed.UB:
        try:
            assert((cb[1] == Cl.F) or (cb[46] == Cl.F))
            if (cb[1] == Cl.F):
                assert(cb[46] == Cl.R)
                return ["F3", "U1", "F1", "U1", "R1", "U3", "R3"]
            else: # cb[46] == Cl.F)
                assert(cb[1] == Cl.R)
                return ["U3", "R1", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.UB])

    elif loc == Ed.FR:
        try:
            assert((cb[23] == Cl.F) or (cb[12] == Cl.F))
            if (cb[23] == Cl.F):
                assert((cb[23] == Cl.F) and (cb[12] == Cl.R))
                return []
            else: # cb[12] == Cl.F)
                assert(cb[23] == Cl.R)
                return ["R1", "U3", "R3", "U3", "F3", "U1", "F1", "U3", "R1", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.FR])
    
    elif loc == Ed.FL:
        try:
            assert((cb[21] == Cl.F) and (cb[41] == Cl.R))
            return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.FL])
    
    elif loc == Ed.BR:
        try:
            assert((cb[14] == Cl.F) or (cb[48] == Cl.F))
            if (cb[14] == Cl.F):
                assert(cb[48] == Cl.R)
                return ["B1", "U3", "B3", "U3", "R3", "U1", "R1", "U1", "F3", "U1", "F1", "U1", "R1", "U3", "R3"]
            else: # cb[48] == Cl.F)
                assert(cb[14] == Cl.R)
                return ["B1", "U3", "B3", "U3", "R3", "U1", "R2", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.BR])
    
    else: #if loc == Ed.BL
        try:
            assert((cb[39] == Cl.F) or (cb[50] == Cl.F))
            if (cb[39] == Cl.F):
                assert(cb[50] == Cl.R)
                return ["B3", "U1", "B1", "U1", "L1", "U3", "L3", "U3", "F3", "U1", "F1", "U1", "R1", "U3", "R3"]
            else: # cb[50] == Cl.F)
                assert(cb[39] == Cl.R)
                return ["B3", "U1", "B1", "U1", "L1", "U3", "L3", "U2", "R1", "U3", "R3", "U3", "F3", "U1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.F): (%s, %s)" 
                % cubies[Ed.BL])

    return []

def layer2(cube_obj):
    """
    Outputs the moves list for solving the cubies in the middle layer after
    solving for the white cross and white corners
    """
    # search for cubies and move into place
    # edge FL
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_f2l(cube_state, cubies):
        return

    if not (cubies[Ed.FL] == tuple(sorted([Cl.F, Cl.L]))):
        loc = find_edge(cubies, tuple(sorted([Cl.F, Cl.L])))
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.F, Cl.L])))
        else:
            move_list = move_FL(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # edge FR
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_f2l(cube_state, cubies):
        return

    if not (cubies[Ed.FR] == tuple(sorted([Cl.F, Cl.R]))):
        loc = find_edge(cubies, tuple(sorted([Cl.F, Cl.R])))
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.F, Cl.R])))
        else:
            move_list = move_FR(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # edge BL
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_f2l(cube_state, cubies):
        return

    if not (cubies[Ed.BL] == tuple(sorted([Cl.B, Cl.L]))):
        loc = find_edge(cubies, tuple(sorted([Cl.B, Cl.L])))
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.B, Cl.L])))
        else:
            pass
            # @NOTE: implement move_BL
            # move_list = move_BL(cube_obj, loc)
            # execute_moves(cube_obj, move_list)

    # edge BR
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_f2l(cube_state, cubies):
        return

    if not (cubies[Ed.BR] == tuple(sorted([Cl.B, Cl.R]))):
        loc = find_edge(cubies, tuple(sorted([Cl.B, Cl.R])))
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.B, Cl.R])))
        else:
            pass
            # @NOTE: implement move_BR
            # move_list = move_BR(cube_obj, loc)
            # execute_moves(cube_obj, move_list)

    try:
        assert(is_f2l(cube_obj.cb, cube_obj.cubies))
    except AssertionError:
        print("did not successfully complete F2L\n")
