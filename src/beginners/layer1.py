import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))

from moves import execute_moves
from cube import Cube, find_edge, find_corner
from facelet import Color as Cl, Corner as Cn, Edge as Ed


"""
white cross: part 1 of first layer algorithms
"""
def is_white_cross(cube_state):
    """
    Checks if the cube has reached the "white cross" state
    """
    return ((cube_state[31] == Cl.D) and
        (cube_state[28] == Cl.D) and (cube_state[25] == Cl.F) and
        (cube_state[30] == Cl.D) and (cube_state[43] == Cl.L) and
        (cube_state[34] == Cl.D) and (cube_state[52] == Cl.B) and
        (cube_state[32] == Cl.D) and (cube_state[16] == Cl.R))

def move_DF(cube_obj, loc):
    """
    Returns the moves list to orient and position the DF edge
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Ed.UR:
        try:
            assert((cb[5] == Cl.D) or (cb[10] == Cl.D))
            if (cb[5] == Cl.D):
                return ["R2", "D3"]
            else: # cb[10] == Cl.D)
                return ["R3", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UR])
    
    elif loc == Ed.UF:
        try:
            assert((cb[7] == Cl.D) or (cb[19] == Cl.D))
            if (cb[7] == Cl.D):
                return ["F2"]
            else: # cb[19] == Cl.D)
                return ["U1", "L1", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UF])
    
    elif loc == Ed.UL:
        try:
            assert((cb[3] == Cl.D) or (cb[37] == Cl.D))
            if (cb[3] == Cl.D):
                return ["L2", "D1"]
            else: # cb[37] == Cl.D)
                return ["L1", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UL])
    
    elif loc == Ed.UB:
        try:
            assert((cb[1] == Cl.D) or (cb[46] == Cl.D))
            if (cb[1] == Cl.D):
                return ["B2", "D2"]
            else: # cb[46] == Cl.D)
                return ["U3", "L1", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UB])
    
    elif loc == Ed.DR:
        try:
            assert((cb[32] == Cl.D) or (cb[16] == Cl.D))
            if (cb[32] == Cl.D):
                return ["D3"]
            else: # cb[16] == Cl.D)
                return ["R1", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DR])
    
    elif loc == Ed.DF:
        try:
            assert((cb[28] == Cl.D) or (cb[25] == Cl.D))
            if ((cb[28] == Cl.F) and (cb[25] == Cl.D)):
                return ["F2", "U3", "R3", "F1"]
            else:
                assert((cb[28] == Cl.D) and (cb[25] == Cl.F))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DF])
    
    elif loc == Ed.DL:
        try:
            assert((cb[30] == Cl.D) or (cb[43] == Cl.D))
            if (cb[30] == Cl.D):
                return ["D1"]
            else: # cb[43] == Cl.D)
                return ["L3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DL])
    
    elif loc == Ed.DB:
        try:
            assert((cb[34] == Cl.D) or (cb[52] == Cl.D))
            if (cb[34] == Cl.D):
                return ["D2"]
            else: # cb[52] == Cl.D)
                return ["B1", "R1", "D3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DB])
    
    elif loc == Ed.FR:
        try:
            assert((cb[23] == Cl.D) or (cb[12] == Cl.D))
            if (cb[23] == Cl.D):
                return ["R3", "D3"]
            else: # cb[12] == Cl.D)
                return ["F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FR])
    
    elif loc == Ed.FL:
        try:
            assert((cb[21] == Cl.D) or (cb[41] == Cl.D))
            if (cb[21] == Cl.D):
                return ["L1", "D1"]
            else: # cb[41] == Cl.D)
                return ["F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FL])
    
    elif loc == Ed.BR:
        try:
            assert((cb[14] == Cl.D) or (cb[48] == Cl.D))
            if (cb[14] == Cl.D):
                return ["B3", "D2"]
            else: # cb[48] == Cl.D)
                return ["R1", "D3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BR])
    
    else: #if loc == Ed.BL
        try:
            assert((cb[39] == Cl.D) or (cb[50] == Cl.D))
            if (cb[39] == Cl.D):
                return ["B1", "D2"]
            else: # cb[50] == Cl.D)
                return ["L3", "D1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BL])

    return []

def move_DL(cube_obj, loc):
    """
    Returns the moves list to orient and position the DL edge
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Ed.UR:
        try:
            assert((cb[5] == Cl.D) or (cb[10] == Cl.D))
            if (cb[5] == Cl.D):
                return ["U2", "L2"]
            else: # cb[10] == Cl.D)
                return ["U3", "B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UR])
    
    elif loc == Ed.UF:
        try:
            assert((cb[7] == Cl.D) or (cb[19] == Cl.D))
            if (cb[7] == Cl.D):
                return ["U1", "L2"]
            else: # cb[19] == Cl.D)
                return ["U2", "B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UF])
    
    elif loc == Ed.UL:
        try:
            assert((cb[3] == Cl.D) or (cb[37] == Cl.D))
            if (cb[3] == Cl.D):
                return ["L2"]
            else: # cb[37] == Cl.D)
                return ["U1", "B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UL])
    
    elif loc == Ed.UB:
        try:
            assert((cb[1] == Cl.D) or (cb[46] == Cl.D))
            if (cb[1] == Cl.D):
                return ["U3", "L2"]
            else: # cb[46] == Cl.D)
                return ["B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UB])
    
    elif loc == Ed.DR:
        try:
            assert((cb[32] == Cl.D) or (cb[16] == Cl.D))
            if (cb[32] == Cl.D):
                return ["R3", "B2", "L3"]
            else: # cb[16] == Cl.D)
                return ["R2", "U3", "B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DR])
    
    elif loc == Ed.DF:
        try:
            # should not reach here
            assert((cb[25] == Cl.F) and (cb[28] == Cl.D))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.B])), cubies[Ed.DF]))
    
    elif loc == Ed.DL:
        try:
            assert((cb[30] == Cl.D) or (cb[43] == Cl.D))
            if ((cb[30] == Cl.L) and (cb[43] == Cl.D)):
                return ["L1", "B3", "U3", "L2"]
            else:
                assert((cb[30] == Cl.D) and (cb[43] == Cl.L))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DL])
    
    elif loc == Ed.DB:
        try:
            assert((cb[34] == Cl.D) or (cb[52] == Cl.D))
            if (cb[34] == Cl.D):
                return ["B2", "U3", "L2"]
            else: # cb[52] == Cl.D)
                return ["B3", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DB])
    
    elif loc == Ed.FR:
        try:
            assert((cb[23] == Cl.D) or (cb[12] == Cl.D))
            if (cb[23] == Cl.D):
                return ["R1", "U2", "L2"]
            else: # cb[12] == Cl.D)
                return ["R1", "U3", "B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FR])
    
    elif loc == Ed.FL:
        try:
            assert((cb[21] == Cl.D) or (cb[41] == Cl.D))
            if (cb[21] == Cl.D):
                return ["L1"]
            else: # cb[41] == Cl.D)
                return ["L3", "U1", "B1", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FL])
    
    elif loc == Ed.BR:
        try:
            assert((cb[14] == Cl.D) or (cb[48] == Cl.D))
            if (cb[14] == Cl.D):
                return ["B1", "U3", "L2"]
            else: # cb[48] == Cl.D)
                return ["B2", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BR])
    
    else: #if loc == Ed.BL
        try:
            assert((cb[39] == Cl.D) or (cb[50] == Cl.D))
            if (cb[39] == Cl.D):
                return ["B3", "U3", "L2"]
            else: # cb[50] == Cl.D)
                return ["L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BL])

    return []

def move_DB(cube_obj, loc):
    """
    Returns the moves list to orient and position the DB edge
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Ed.UR:
        try:
            assert((cb[5] == Cl.D) or (cb[10] == Cl.D))
            if (cb[5] == Cl.D):
                return ["U3", "B2"]
            else: # cb[10] == Cl.D)
                return ["R1", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UR])
    
    elif loc == Ed.UF:
        try:
            assert((cb[7] == Cl.D) or (cb[19] == Cl.D))
            if (cb[7] == Cl.D):
                return ["U2", "B2"]
            else: # cb[19] == Cl.D)
                return ["U3", "R1", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UF])
    
    elif loc == Ed.UL:
        try:
            assert((cb[3] == Cl.D) or (cb[37] == Cl.D))
            if (cb[3] == Cl.D):
                return ["U1", "B2"]
            else: # cb[37] == Cl.D)
                return ["U2", "R1", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UL])
    
    elif loc == Ed.UB:
        try:
            assert((cb[1] == Cl.D) or (cb[46] == Cl.D))
            if (cb[1] == Cl.D):
                return ["B2"]
            else: # cb[46] == Cl.D)
                return ["U1", "R1", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UB])
    
    elif loc == Ed.DR:
        try:
            assert((cb[32] == Cl.D) or (cb[16] == Cl.D))
            if (cb[32] == Cl.D):
                return ["R2", "U3", "B2"]
            else: # cb[16] == Cl.D)
                return ["R3", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DR])
    
    elif loc == Ed.DF:
        try:
            # should not reach here
            assert((cb[25] == Cl.F) and (cb[28] == Cl.D))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.B])), cubies[Ed.DF]))
    
    elif loc == Ed.DL:
        try:
            # should not reach here
            assert((cb[30] == Cl.D) and (cb[43] == Cl.L))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.L])), cubies[Ed.DL]))
    
    elif loc == Ed.DB:
        try:
            assert((cb[34] == Cl.D) or (cb[52] == Cl.D))
            if ((cb[34] == Cl.B) and (cb[52] == Cl.D)):
                return ["B2", "U1", "R1", "B3"]
            else:
                assert((cb[34] == Cl.D) and (cb[52] == Cl.B))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DL])
    
    elif loc == Ed.FR:
        try:
            assert((cb[23] == Cl.D) or (cb[12] == Cl.D))
            if (cb[23] == Cl.D):
                return ["R1", "U3", "B2"]
            else: # cb[12] == Cl.D)
                return ["R2", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FR])
    
    elif loc == Ed.FL:
        try:
            assert((cb[21] == Cl.D) or (cb[41] == Cl.D))
            if (cb[21] == Cl.D):
                return ["D1", "L1", "D3"]
            else: # cb[41] == Cl.D)
                return ["D2", "F3", "D2"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FL])
    
    elif loc == Ed.BR:
        try:
            assert((cb[14] == Cl.D) or (cb[48] == Cl.D))
            if (cb[14] == Cl.D):
                return ["B3"]
            else: # cb[48] == Cl.D)
                return ["B1", "U1", "R1", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BR])
    
    else: #if loc == Ed.BL
        try:
            assert((cb[39] == Cl.D) or (cb[50] == Cl.D))
            if (cb[39] == Cl.D):
                return ["B1"]
            else: # cb[50] == Cl.D)
                return ["B3", "U1", "R1", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BL])

    return []

def move_DR(cube_obj, loc):
    """
    Returns the moves list to orient and position the DR edge
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Ed.UR:
        try:
            assert((cb[5] == Cl.D) or (cb[10] == Cl.D))
            if (cb[5] == Cl.D):
                return ["R2"]
            else: # cb[10] == Cl.D)
                return ["R1", "D1", "B3", "D3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UR])
    
    elif loc == Ed.UF:
        try:
            assert((cb[7] == Cl.D) or (cb[19] == Cl.D))
            if (cb[7] == Cl.D):
                return ["U3", "R2"]
            else: # cb[19] == Cl.D)
                return ["U2", "B3", "R1", "B1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UF])
    
    elif loc == Ed.UL:
        try:
            assert((cb[3] == Cl.D) or (cb[37] == Cl.D))
            if (cb[3] == Cl.D):
                return ["U2", "R2"]
            else: # cb[37] == Cl.D)
                return ["U1", "B3", "R1", "B1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UL])
    
    elif loc == Ed.UB:
        try:
            assert((cb[1] == Cl.D) or (cb[46] == Cl.D))
            if (cb[1] == Cl.D):
                return ["U1", "R2"]
            else: # cb[46] == Cl.D)
                return ["B3", "R1", "B1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.UB])
    
    elif loc == Ed.DR:
        try:
            assert((cb[32] == Cl.D) or (cb[16] == Cl.D))
            if ((cb[32] == Cl.R) and (cb[16] == Cl.D)):
                return ["R3", "D1", "B3", "D3"]
            else:
                assert((cb[32] == Cl.D) and (cb[16] == Cl.R))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.DR])
    
    elif loc == Ed.DF:
        try:
            # should not reach here
            assert((cb[25] == Cl.F) and (cb[28] == Cl.D))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.B])), cubies[Ed.DF]))
    
    elif loc == Ed.DL:
        try:
            # should not reach here
            assert((cb[30] == Cl.D) and (cb[43] == Cl.L))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.L])), cubies[Ed.DL]))
    
    elif loc == Ed.DB:
        try:
            # should not reach here
            assert((cb[34] == Cl.D) and (cb[52] == Cl.B))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.B])), cubies[Ed.DB]))
    
    elif loc == Ed.FR:
        try:
            assert((cb[23] == Cl.D) or (cb[12] == Cl.D))
            if (cb[23] == Cl.D):
                return ["R3"]
            else: # cb[12] == Cl.D)
                return ["D3", "F1", "D1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FR])
    
    elif loc == Ed.FL:
        try:
            assert((cb[21] == Cl.D) or (cb[41] == Cl.D))
            if (cb[21] == Cl.D):
                return ["D2", "L1", "D2"]
            else: # cb[41] == Cl.D)
                return ["D3", "F3", "D1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.FL])
    
    elif loc == Ed.BR:
        try:
            assert((cb[14] == Cl.D) or (cb[48] == Cl.D))
            if (cb[14] == Cl.D):
                return ["D1", "B3", "D3"]
            else: # cb[48] == Cl.D)
                return ["R1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BR])
    
    else: #if loc == Ed.BL
        try:
            assert((cb[39] == Cl.D) or (cb[50] == Cl.D))
            if (cb[39] == Cl.D):
                return ["D1", "B1", "D3"]
            else: # cb[50] == Cl.D)
                return ["D2", "L3", "D2"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s)" 
                % cubies[Ed.BL])
    return []

def white_cross(cube_obj):
    """
    Outputs the moves list for solving the down face edge cubies according to
    the initial cube state
    """
    # search for cubies and move into place
    # edge DF
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_cross(cube_state):
        print("white cross completed")
        print(cube_obj)
        return

    # print("DF")
    # print(cube_obj)
    if not ((cube_state[28] == Cl.D) and (cube_state[25] == Cl.F)):
        loc = find_edge(cubies, tuple(sorted([Cl.D, Cl.F])))
        # print(loc)
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.D, Cl.F])))
        else:
            move_list = move_DF(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # edge DL
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_cross(cube_state):
        print("white cross completed")
        print(cube_obj)
        return

    # print("DL")
    # print(cube_obj)
    if not ((cube_state[30] == Cl.D) and (cube_state[43] == Cl.L)):
        loc = find_edge(cubies, tuple(sorted([Cl.D, Cl.L])))
        # print(loc)
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.D, Cl.L])))
        else:
            move_list = move_DL(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # edge DB
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_cross(cube_state):
        print("white cross completed")
        print(cube_obj)
        return

    # print("DB")
    # print(cube_obj)
    if not ((cube_state[34] == Cl.D) and (cube_state[52] == Cl.B)):
        loc = find_edge(cubies, tuple(sorted([Cl.D, Cl.B])))
        # print(loc)
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.D, Cl.B])))
        else:
            move_list = move_DB(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # edge DR
    cube_state = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_cross(cube_state):
        print("white cross completed")
        print(cube_obj)
        return

    # print("DR")
    # print(cube_obj)
    if not ((cube_state[32] == Cl.D) and (cube_state[16] == Cl.R)):
        loc = find_edge(cubies, tuple(sorted([Cl.D, Cl.R])))
        # print(loc)
        if loc is None:
            print("can't find edge (%s, %s)" % tuple(sorted([Cl.U, Cl.R])))
        else:
            move_list = move_DR(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    try:
        assert(is_white_cross(cube_obj.cb))
        print("white cross completed")
        print(cube_obj)
    except AssertionError:
        print("did not successfully reach white cross state\n")

"""
white corners: part 2 of first layer algorithms
"""
def is_white_corners(cstate):
    """
    Checks if the cube has reached the "white corners" state
    """
    return (is_white_cross(cstate) and
        (cstate[29] == Cl.D) and (cstate[26] == Cl.F) and (cstate[15] == Cl.R) and
        (cstate[27] == Cl.D) and (cstate[44] == Cl.L) and (cstate[24] == Cl.F) and
        (cstate[33] == Cl.D) and (cstate[53] == Cl.B) and (cstate[42] == Cl.L) and
        (cstate[35] == Cl.D) and (cstate[17] == Cl.R) and (cstate[51] == Cl.B))

def move_DFR(cube_obj, loc):
    """
    Returns the moves list to orient and position the DFR corner
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Cn.URF:
        try:
            assert((cb[8] == Cl.D) or (cb[9] == Cl.D) or (cb[20] == Cl.D))
            if (cb[8] == Cl.D):
                return ["R1", "U2", "R3", "U2", "F3", "U1", "F1"]
            elif (cb[9] == Cl.D):
                return ["R1", "U1", "R3"]
            else: # cb[20] == Cl.D)
                return ["F3", "U3", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.URF])
    
    elif loc == Cn.UFL:
        try:
            assert((cb[6] == Cl.D) or (cb[18] == Cl.D) or (cb[38] == Cl.D))
            if (cb[6] == Cl.D):
                return ["R1", "U2", "R3", "U1", "R1", "U3", "R3"]
            elif (cb[18] == Cl.D):
                return ["U3", "R1", "U1", "R3"]
            else: # cb[38] == Cl.D)
                return ["R1", "U3", "R3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UFL])
    
    elif loc == Cn.ULB:
        try:
            assert((cb[0] == Cl.D) or (cb[36] == Cl.D) or (cb[47] == Cl.D))
            if (cb[0] == Cl.D):
                return ["R1", "U1", "R3", "U1", "R1", "U3", "R3"]
            elif (cb[36] == Cl.D):
                return ["F3", "U2", "F1"]
            else: # cb[47] == Cl.D)
                return ["R1", "U2", "R3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.ULB])
    
    elif loc == Cn.UBR:
        try:
            assert((cb[2] == Cl.D) or (cb[45] == Cl.D) or (cb[11] == Cl.D))
            if (cb[2] == Cl.D):
                return ["U3", "R1", "U1", "R3", "U1", "R1", "U3", "R3"]
            elif (cb[45] == Cl.D):
                return ["F3", "U1", "F1"]
            else: # cb[11] == Cl.D)
                return ["U2", "R1", "U3", "R3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UBR])
    
    elif loc == Cn.DFR:
        try:
            assert((cb[29] == Cl.D) or (cb[26] == Cl.D) or (cb[15] == Cl.D))
            if (cb[26] == Cl.D):
                return ["R1", "U3", "R3", "U1", "R1", "U3", "R3"]
            elif (cb[15] == Cl.D):
                return ["R1", "U1", "R3", "U2", "F3", "U1", "F1"]
            else: # cb[29] == Cl.D)
                assert((cb[29] == Cl.D) and (cb[26] == Cl.F) and (cb[15] == Cl.R))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DFR])

    elif loc == Cn.DLF:
        try:
            assert((cb[27] == Cl.D) or (cb[44] == Cl.D) or (cb[24] == Cl.D))
            if (cb[27] == Cl.D):
                return ["F1", "U1", "F3", "R1", "U2", "R3"]
            elif (cb[44] == Cl.D):
                return ["L3", "R1", "U3", "L1", "R3"]
            else: # cb[24] == Cl.D)
                return ["L3", "R1", "U2", "R3", "U1", "R1", "U3", "R3", "L1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DLF])

    elif loc == Cn.DBL:
        try:
            assert((cb[33] == Cl.D) or (cb[53] == Cl.D) or (cb[42] == Cl.D))
            if (cb[33] == Cl.D):
                return ["B3", "F3", "U2", "B1", "F1"]
            elif (cb[53] == Cl.D):
                return ["L1", "R1", "U1", "R3", "U1", "R1", "U3", "R3", "L3"]
            else: # cb[42] == Cl.D)
                return ["B3", "R1", "U1", "R3", "B1", "U1", "R1", "U3", "R3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DBL])

    else: #if loc == Cn.DRB
        try:
            assert((cb[35] == Cl.D) or (cb[17] == Cl.D) or (cb[51] == Cl.D))
            if (cb[35] == Cl.D):
                return ["B1", "U2", "B3", "R1", "U3", "R3"]
            elif (cb[17] == Cl.D):
                return ["R3", "U2", "R2", "U3", "R3"]
            else: # cb[51] == Cl.D)
                return ["F3", "B1", "U1", "B3", "F1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DRB])

    return []

def move_DLF(cube_obj, loc):
    """
    Returns the moves list to orient and position the DFR corner
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Cn.URF:
        try:
            assert((cb[8] == Cl.D) or (cb[9] == Cl.D) or (cb[20] == Cl.D))
            if (cb[8] == Cl.D):
                return ["L3", "U2", "L1", "U3", "L3", "U1", "L1"]
            elif (cb[9] == Cl.D):
                return ["L3", "U1", "L1"]
            else: # cb[20] == Cl.D)
                return ["U2", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.URF])
    
    elif loc == Cn.UFL:
        try:
            assert((cb[6] == Cl.D) or (cb[18] == Cl.D) or (cb[38] == Cl.D))
            if (cb[6] == Cl.D):
                return ["U1", "F1", "U2", "F3", "U1", "F1", "U3", "F3"]
            elif (cb[18] == Cl.D):
                return ["U3", "L3", "U1", "L1"]
            else: # cb[38] == Cl.D)
                return ["L3", "U3", "L1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UFL])
    
    elif loc == Cn.ULB:
        try:
            assert((cb[0] == Cl.D) or (cb[36] == Cl.D) or (cb[47] == Cl.D))
            if (cb[0] == Cl.D):
                return ["U1", "L3", "U3", "L1", "U3", "L3", "U1", "L1"]
            elif (cb[36] == Cl.D):
                return ["U2", "L3", "U1", "L1"]
            else: # cb[47] == Cl.D)
                return ["F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.ULB])
    
    elif loc == Cn.UBR:
        try:
            assert((cb[2] == Cl.D) or (cb[45] == Cl.D) or (cb[11] == Cl.D))
            if (cb[2] == Cl.D):
                return ["L3", "U3", "L1", "U3", "L3", "U1", "L1"]
            elif (cb[45] == Cl.D):
                return ["L3", "U2", "L1"]
            else: # cb[11] == Cl.D)
                return ["U3", "F1", "U3", "F3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UBR])
    
    elif loc == Cn.DFR:
        try:
            assert((cb[29] == Cl.D) and (cb[26] == Cl.F) and (cb[15] == Cl.R))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.F, Cl.R])), cubies[Cn.DFR]))

    elif loc == Cn.DLF:
        try:
            assert((cb[27] == Cl.D) or (cb[44] == Cl.D) or (cb[24] == Cl.D))
            if (cb[44] == Cl.D):
                return ["L3", "U2", "L1", "U3", "F1", "U3", "F3"]
            elif (cb[24] == Cl.D):
                return ["F1", "U1", "F3", "U3", "F1", "U1", "F3", "U3"]
            else: # cb[27] == Cl.D)
                assert((cb[27] == Cl.D) and (cb[44] == Cl.L) and (cb[24] == Cl.F))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DLF])

    elif loc == Cn.DBL:
        try:
            assert((cb[33] == Cl.D) or (cb[53] == Cl.D) or (cb[42] == Cl.D))
            if (cb[33] == Cl.D):
                return ["B3", "U2", "B1", "L3", "U1", "L1"]
            elif (cb[53] == Cl.D):
                return ["B3", "U2", "B1", "U2", "F1", "U3", "F3"]
            else: # cb[42] == Cl.D)
                return ["B3", "U1", "B1", "U2", "L3", "U1", "L1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DBL])

    else: #if loc == Cn.DRB
        try:
            assert((cb[35] == Cl.D) or (cb[17] == Cl.D) or (cb[51] == Cl.D))
            if (cb[35] == Cl.D):
                return ["B1", "U1", "B3", "U2", "F1", "U3", "F3"]
            elif (cb[17] == Cl.D):
                return ["B1", "U3", "B3", "F1", "U2", "F3"]
            else: # cb[51] == Cl.D)
                return ["B1", "U1", "L3", "U1", "B3", "L1"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DRB])

    return []

def move_DBL(cube_obj, loc):
    """
    Returns the moves list to orient and position the DFR corner
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Cn.URF:
        try:
            assert((cb[8] == Cl.D) or (cb[9] == Cl.D) or (cb[20] == Cl.D))
            if (cb[8] == Cl.D):
                return ["B3", "U3", "B1", "U3", "B3", "U1", "B1"]
            elif (cb[9] == Cl.D):
                return ["U1", "B3", "U1", "B1"]
            else: # cb[20] == Cl.D)
                return ["U3", "L1", "U3", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.URF])
    
    elif loc == Cn.UFL:
        try:
            assert((cb[6] == Cl.D) or (cb[18] == Cl.D) or (cb[38] == Cl.D))
            if (cb[6] == Cl.D):
                return ["B3", "U2", "B1", "U3", "B3", "U1", "B1"]
            elif (cb[18] == Cl.D):
                return ["B3", "U1", "B1"]
            else: # cb[38] == Cl.D)
                return ["U2", "L1", "U3", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UFL])
    
    elif loc == Cn.ULB:
        try:
            assert((cb[0] == Cl.D) or (cb[36] == Cl.D) or (cb[47] == Cl.D))
            if (cb[0] == Cl.D):
                return ["B3", "U1", "B1", "L1", "U2", "L3"]
            elif (cb[36] == Cl.D):
                return ["U3", "B3", "U1", "B1"]
            else: # cb[47] == Cl.D)
                return ["U1", "L1", "U3", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.ULB])
    
    elif loc == Cn.UBR:
        try:
            assert((cb[2] == Cl.D) or (cb[45] == Cl.D) or (cb[11] == Cl.D))
            if (cb[2] == Cl.D):
                return ["R3", "B2", "R1", "B2", "R1"]
            elif (cb[45] == Cl.D):
                return ["U3", "L1", "U1", "L3"]
            else: # cb[11] == Cl.D)
                return ["L1", "U3", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UBR])
    
    elif loc == Cn.DFR:
        try:
            assert((cb[29] == Cl.D) and (cb[26] == Cl.F) and (cb[15] == Cl.R))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.F, Cl.R])), cubies[Cn.DFR]))

    elif loc == Cn.DLF:
        try:
            assert((cb[27] == Cl.D) and (cb[44] == Cl.L) and (cb[24] == Cl.F))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.L, Cl.F])), cubies[Cn.DLF]))

    elif loc == Cn.DBL:
        try:
            assert((cb[33] == Cl.D) or (cb[53] == Cl.D) or (cb[42] == Cl.D))
            if (cb[53] == Cl.D):
                return ["B3", "U1", "B1", "U3", "B3", "U2", "B1", "U3", "B3", "U1", "B1"]
            elif (cb[42] == Cl.D):
                return ["B3", "U1", "B1", "U3", "B3", "U1", "B1"]
            else: # cb[33] == Cl.D)
                assert((cb[33] == Cl.D) and (cb[53] == Cl.B) and (cb[42] == Cl.L))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DBL])

    else: #if loc == Cn.DRB
        try:
            assert((cb[35] == Cl.D) or (cb[17] == Cl.D) or (cb[51] == Cl.D))
            if (cb[35] == Cl.D):
                return ["B1", "U3", "B3", "U2", "B3", "U1", "B1"]
            elif (cb[17] == Cl.D):
                return ["B1", "U3", "B3", "L1", "U3", "L3"]
            else: # cb[51] == Cl.D)
                return ["B1", "U3", "B3", "L1", "U2", "L3", "U1", "L1", "U3", "L3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DRB])

    return []

def move_DRB(cube_obj, loc):
    """
    Returns the moves list to orient and position the DFR corner
    """
    cb = cube_obj.get_cb()
    cubies = cube_obj.cubies
    if loc == Cn.URF:
        try:
            assert((cb[8] == Cl.D) or (cb[9] == Cl.D) or (cb[20] == Cl.D))
            if (cb[8] == Cl.D):
                return ["B1", "U2", "B3", "U1", "B1", "U3", "B3"]
            elif (cb[9] == Cl.D):
                return ["U2", "R3", "U1", "R1"]
            else: # cb[20] == Cl.D)
                return ["B1", "U3", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.URF])
    
    elif loc == Cn.UFL:
        try:
            assert((cb[6] == Cl.D) or (cb[18] == Cl.D) or (cb[38] == Cl.D))
            if (cb[6] == Cl.D):
                return ["B1", "U1", "B3", "U1", "B1", "U3", "B3"]
            elif (cb[18] == Cl.D):
                return ["U1", "R3", "U1", "R1"]
            else: # cb[38] == Cl.D)
                return ["B1", "U2", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UFL])
    
    elif loc == Cn.ULB:
        try:
            assert((cb[0] == Cl.D) or (cb[36] == Cl.D) or (cb[47] == Cl.D))
            if (cb[0] == Cl.D):
                return ["R3", "U2", "R1", "U3", "R3", "U1", "R1"]
            elif (cb[36] == Cl.D):
                return ["R3", "U1", "R1"]
            else: # cb[47] == Cl.D)
                return ["U2", "B1", "U3", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.ULB])
    
    elif loc == Cn.UBR:
        try:
            assert((cb[2] == Cl.D) or (cb[45] == Cl.D) or (cb[11] == Cl.D))
            if (cb[2] == Cl.D):
                return ["U1", "B1", "U2", "B3", "U1", "B1", "U3", "B3"]
            elif (cb[45] == Cl.D):
                return ["U3", "R3", "U1", "R1"]
            else: # cb[11] == Cl.D)
                return ["U1", "B1", "U3", "B3"]

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.UBR])
    
    elif loc == Cn.DFR:
        try:
            assert((cb[29] == Cl.D) and (cb[26] == Cl.F) and (cb[15] == Cl.R))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.F, Cl.R])), cubies[Cn.DFR]))

    elif loc == Cn.DLF:
        try:
            assert((cb[27] == Cl.D) and (cb[44] == Cl.L) and (cb[24] == Cl.F))
            return []

        except AssertionError:
            print("should be (%s); is (%s)"
                % (tuple(sorted([Cl.D, Cl.L, Cl.F])), cubies[Cn.DLF]))

    elif loc == Cn.DBL:
        try:
            assert((cb[33] == Cl.D) and (cb[53] == Cl.B) and (cb[42] == Cl.L))
            return []

        except AssertionError:
            print("should be (%s); is (%s)" 
                % (tuple(sorted([Cl.D, Cl.B, Cl.L])), cubies[Cn.DBL]))

    else: #if loc == Cn.DRB
        try:
            assert((cb[35] == Cl.D) or (cb[17] == Cl.D) or (cb[51] == Cl.D))
            if (cb[17] == Cl.D):
                return ["B1", "U3", "B3", "U1", "B1", "U3", "B3"]
            elif (cb[51] == Cl.D):
                return ["B1", "U1", "B3", "U2", "R3", "U1", "R1"]
            else: # cb[51] == Cl.D)
                assert((cb[35] == Cl.D) and (cb[17] == Cl.R) and (cb[51] == Cl.B))
                return []

        except AssertionError:
            print("invalid colors (at least one should be Cl.D): (%s, %s, %s)" 
                % cubies[Cn.DRB])

    return []

def white_corners(cube_obj):
    """
    Outputs the moves list for solving the down face corner cubies after
    solving for the white cross
    """
    # search for cubies and move into place
    # corner DFR
    cstate = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_corners(cstate):
        print("white corners completed")
        print(cube_obj)
        return

    # print("DFR")
    # print(cube_obj)
    if not ((cstate[29] == Cl.D) and (cstate[26] == Cl.F) and (cstate[15] == Cl.R)):
        loc = find_corner(cubies, tuple(sorted([Cl.D, Cl.F, Cl.R])))
        # print(loc)
        if loc is None:
            print("can't find corner (%s, %s, %s)" 
                % tuple(sorted([Cl.D, Cl.F, Cl.R])))
        else:
            move_list = move_DFR(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # corner DLF
    cstate = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_corners(cstate):
        print("white corners completed")
        print(cube_obj)
        return

    # print("DLF")
    # print(cube_obj)
    if not ((cstate[27] == Cl.D) and (cstate[44] == Cl.L) and (cstate[24] == Cl.F)):
        loc = find_corner(cubies, tuple(sorted([Cl.D, Cl.L, Cl.F])))
        # print(loc)
        if loc is None:
            print("can't find corner (%s, %s, %s)" 
                % tuple(sorted([Cl.D, Cl.L, Cl.F])))
        else:
            move_list = move_DLF(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # corner DBL
    cstate = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_corners(cstate):
        print("white corners completed")
        print(cube_obj)
        return

    # print("DBL")
    # print(cube_obj)
    if not ((cstate[33] == Cl.D) and (cstate[53] == Cl.B) and (cstate[42] == Cl.L)):
        loc = find_corner(cubies, tuple(sorted([Cl.D, Cl.B, Cl.L])))
        # print(loc)
        if loc is None:
            print("can't find corner (%s, %s, %s)" 
                % tuple(sorted([Cl.D, Cl.B, Cl.L])))
        else:
            move_list = move_DBL(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    # corner DRB
    cstate = cube_obj.cb
    cubies = cube_obj.cubies

    if is_white_corners(cstate):
        print("white corners completed")
        print(cube_obj)
        return

    # print("DRB")
    # print(cube_obj)
    if not ((cstate[35] == Cl.D) and (cstate[17] == Cl.R) and (cstate[51] == Cl.B)):
        loc = find_corner(cubies, tuple(sorted([Cl.D, Cl.R, Cl.B])))
        # print(loc)
        if loc is None:
            print("can't find corner (%s, %s, %s)" 
                % tuple(sorted([Cl.D, Cl.R, Cl.B])))
        else:
            move_list = move_DRB(cube_obj, loc)
            execute_moves(cube_obj, move_list)

    try:
        assert(is_white_corners(cube_obj.cb))
        print("white corners completed")
        print(cube_obj)
    except AssertionError:
        print("did not successfully reach white corners state\n")

def layer1(cube_obj):
    """
    Calls the solving algorithms for the first layer: white cross and white
    corners
    """
    white_cross(cube_obj)
    white_corners(cube_obj)
    