import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))

from moves import execute_moves
from facelet import Color as Cl

# https://www.speedcubereview.com/pll.html
# http://www.rubiksplace.com/speedcubing/PLL-algorithms/
# https://ruwix.com/the-rubiks-cube/advanced-cfop-fridrich/permutate-the-last-layer-pll/
# 57 different states
def pll_state(cb):
    """
    Finds and returns the cube object's pll state number; returns 0 if current
    state does not match any of the states
    """
    # edge perms
    u1_perm = ((cb[9] == cb[19]) and (cb[19] == cb[11]) and
                (cb[18] == cb[37]) and (cb[37] == cb[20]) and
                (cb[36] == cb[10]) and (cb[10] == cb[38]) and
                (cb[45] == cb[46]) and (cb[46] == cb[47]))
    u2_perm = ((cb[9] == cb[37]) and (cb[37] == cb[11]) and
                (cb[18] == cb[10]) and (cb[10] == cb[20]) and
                (cb[36] == cb[19]) and (cb[19] == cb[38]) and
                (cb[45] == cb[46]) and (cb[46] == cb[47]))
    z_perm = ((cb[9] == cb[46]) and (cb[46] == cb[11]) and
                (cb[18] == cb[37]) and (cb[37] == cb[20]) and
                (cb[36] == cb[19]) and (cb[19] == cb[38]) and
                (cb[45] == cb[10]) and (cb[10] == cb[47]))
    h_perm = ((cb[9] == cb[37]) and (cb[37] == cb[11]) and
                (cb[18] == cb[46]) and (cb[46] == cb[20]) and
                (cb[36] == cb[10]) and (cb[10] == cb[38]) and
                (cb[45] == cb[19]) and (cb[19] == cb[47]))

    if u1_perm:
        return 1
    if u2_perm:
        return 2
    if z_perm:
        return 3
    if h_perm:
        return 4

    # corner perms
    a1_perm = ((cb[45] == cb[10]) and (cb[10] == cb[47]) and
                (cb[18] == cb[19]) and (cb[19] == cb[11]) and
                (cb[9] == cb[37]) and (cb[37] == cb[38]) and
                (cb[36] == cb[46]) and (cb[46] == cb[20]))
    a2_perm = ((cb[9] == cb[10]) and (cb[10] == cb[38]) and
                (cb[36] == cb[19]) and (cb[19] == cb[20]) and
                (cb[45] == cb[37]) and (cb[37] == cb[47]) and
                (cb[11] == cb[46]) and (cb[46] == cb[18]))
    e_perm = ((cb[20] == cb[10]) and (cb[10] == cb[45]) and
                (cb[36] == cb[19]) and (cb[19] == cb[11]) and
                (cb[18] == cb[37]) and (cb[37] == cb[47]) and
                (cb[9] == cb[46]) and (cb[46] == cb[38]))

    if a1_perm:
        return 5
    if a2_perm:
        return 6
    if e_perm:
        return 7

    # corner & edge swap perms
    t_perm = ((cb[36] == cb[10]) and (cb[10] == cb[38]) and
                (cb[18] == cb[19]) and (cb[19] == cb[11]) and
                (cb[20] == cb[37]) and (cb[37] == cb[45]) and
                (cb[9] == cb[46]) and (cb[46] == cb[47]))
    f_perm = ((cb[45] == cb[10]) and (cb[10] == cb[20]) and
                (cb[18] == cb[46]) and (cb[46] == cb[11]) and
                (cb[36] == cb[37]) and (cb[37] == cb[38]) and
                (cb[9] == cb[19]) and (cb[19] == cb[47]))
    j1_perm = ((cb[9] == cb[10]) and (cb[10] == cb[11]) and
                (cb[18] == cb[19]) and (cb[19] == cb[47]) and
                (cb[36] == cb[37]) and (cb[37] == cb[20]) and
                (cb[45] == cb[46]) and (cb[46] == cb[38]))
    j2_perm = ((cb[18] == cb[10]) and (cb[10] == cb[11]) and
                (cb[45] == cb[19]) and (cb[19] == cb[20]) and
                (cb[36] == cb[37]) and (cb[37] == cb[38]) and
                (cb[9] == cb[46]) and (cb[46] == cb[47]))
    r1_perm = ((cb[9] == cb[10]) and (cb[10] == cb[47]) and
                (cb[18] == cb[37]) and (cb[37] == cb[20]) and
                (cb[45] == cb[19]) and (cb[19] == cb[38]) and
                (cb[36] == cb[46]) and (cb[46] == cb[11]))
    r2_perm = ((cb[9] == cb[19]) and (cb[19] == cb[47]) and
                (cb[18] == cb[10]) and (cb[10] == cb[20]) and
                (cb[45] == cb[37]) and (cb[37] == cb[38]) and
                (cb[11] == cb[46]) and (cb[46] == cb[36]))
    v_perm = ((cb[20] == cb[10]) and (cb[10] == cb[45]) and
                (cb[18] == cb[19]) and (cb[19] == cb[47]) and
                (cb[9] == cb[37]) and (cb[37] == cb[38]) and
                (cb[11] == cb[46]) and (cb[46] == cb[36]))
    y_perm = ((cb[36] == cb[10]) and (cb[10] == cb[11]) and
                (cb[18] == cb[19]) and (cb[19] == cb[47]) and
                (cb[20] == cb[37]) and (cb[37] == cb[45]) and
                (cb[9] == cb[46]) and (cb[46] == cb[38]))
    n1_perm = ((cb[36] == cb[10]) and (cb[10] == cb[11]) and
                (cb[45] == cb[19]) and (cb[19] == cb[20]) and
                (cb[9] == cb[37]) and (cb[37] == cb[38]) and
                (cb[18] == cb[46]) and (cb[46] == cb[47]))
    n2_perm = ((cb[9] == cb[10]) and (cb[10] == cb[38]) and
                (cb[18] == cb[19]) and (cb[19] == cb[47]) and
                (cb[36] == cb[37]) and (cb[37] == cb[11]) and
                (cb[45] == cb[46]) and (cb[46] == cb[20]))
    
    if t_perm:
        return 8
    if f_perm:
        return 9
    if j1_perm:
        return 10
    if j2_perm:
        return 11
    if r1_perm:
        return 12
    if r2_perm:
        return 13
    if v_perm:
        return 14
    if y_perm:
        return 15
    if n1_perm:
        return 16
    if n2_perm:
        return 17

    # corner & edge cycle perms
    g1_perm = ((cb[36] == cb[10]) and (cb[10] == cb[38]) and
                (cb[45] == cb[19]) and (cb[19] == cb[20]) and
                (cb[9] == cb[37]) and (cb[37] == cb[47]) and
                (cb[11] == cb[46]) and (cb[46] == cb[18]))
    g2_perm = ((cb[18] == cb[10]) and (cb[10] == cb[47]) and
                (cb[9] == cb[19]) and (cb[19] == cb[11]) and
                (cb[45] == cb[37]) and (cb[37] == cb[38]) and
                (cb[20] == cb[46]) and (cb[46] == cb[36]))
    g3_perm = ((cb[36] == cb[10]) and (cb[10] == cb[38]) and
                (cb[9] == cb[19]) and (cb[19] == cb[47]) and
                (cb[11] == cb[37]) and (cb[37] == cb[18]) and
                (cb[45] == cb[46]) and (cb[46] == cb[20]))
    g4_perm = ((cb[9] == cb[10]) and (cb[10] == cb[47]) and
                (cb[36] == cb[19]) and (cb[19] == cb[38]) and
                (cb[20] == cb[37]) and (cb[37] == cb[45]) and
                (cb[11] == cb[46]) and (cb[46] == cb[18]))

    if g1_perm:
        return 18
    if g2_perm:
        return 19
    if g3_perm:
        return 20
    if g4_perm:
        return 21

    return 0

def pll_moves(cube_obj, state):
    """
    Returns the moves list to permute the top layer into the fully-solved state
    """
    # edge perms
    if (state == 1):
        return ["R1", "U3", "R1", "U1", "R1", "U1", "R1", "U3", "R3", "U3", "R2"]
    elif (state == 2):
        return ["R2", "U1", "R1", "U1", "R3", "U3", "R3", "U3", "R3", "U1", "R3"]
    elif (state == 3):
        return ["U3", "R3", "U3", "R2", "U1", "R1", "U1", "R3", "U3", "R1", "U1", "R1", "U3", "R1", "U3", "R3"]
    elif (state == 4):
        return ["R2", "U2", "R1", "U2", "R2", "U2", "R2", "U2", "R1", "U2", "R2"]

    # corner perms
    elif (state == 5):
        return ["R3", "F1", "R3", "B2", "R1", "F3", "R3", "B2", "R2"]
    elif (state == 6):
        return ["L1", "F3", "L1", "B2", "L3", "F1", "L1", "B2", "L2"]
    elif (state == 7):
        return ["R1", "B3", "R3", "F1", "R1", "B1", "R3", "F3", "R1", "B1", "R3", "F1", "R1", "B3", "R3", "F3"]

    # corner & edge swap perms
    elif (state == 8):
        return ["R1", "U1", "R3", "U3", "R3", "F1", "R2", "U3", "R3", "U3", "R1", "U1", "R3", "F3"]
    elif (state == 9):
        return ["R3", "U3", "F3", "R1", "U1", "R3", "U3", "R3", "F1", "R2", "U3", "R3", "U3", "R1", "U1", "R3", "U1", "R1"]
    elif (state == 10):
        return ["L3", "U3", "L1", "F1", "L3", "U3", "L1", "U1", "L1", "F3", "L2", "U1", "L1", "U1"]
    elif (state == 11):
        return ["R1", "U1", "R3", "F3", "R1", "U1", "R3", "U3", "R3", "F1", "R2", "U3", "R3", "U3"]
    elif (state == 12):
        return ["L1", "U2", "L3", "U2", "L1", "F3", "L3", "U3", "L1", "U1", "L1", "F1", "L2", "U1"]
    elif (state == 13):
        return ["R3", "U2", "R1", "U2", "R3", "F1", "R1", "U1", "R3", "U3", "R3", "F3", "R2", "U3"]
    elif (state == 14):
        return ["R3", "U1", "R3", "U3", "B3", "R3", "B2", "U3", "B3", "U1", "B3", "R1", "B1", "R1"]
    elif (state == 15):
        return ["F1", "R1", "U3", "R3", "U3", "R1", "U1", "R3", "F3", "R1", "U1", "R3", "U3", "R3", "F1", "R1", "F3"]
    elif (state == 16):
        return ["L1", "U3", "R1", "U2", "L3", "U1", "R3", "L1", "U3", "R1", "U2", "L3", "U1", "R3"]
    elif (state == 17):
        return ["R3", "U1", "L3", "U2", "R1", "U3", "L1", "R3", "U1", "L3", "U2", "R1", "U3", "L1"]

    # corner & edge cycle perms
    elif (state == 18):
        return ["R2", "D1", "B3", "U1", "B3", "U3", "B1", "D3", "R2", "F3", "U1", "F1"]
    elif (state == 19):
        return ["L3", "U3", "L1", "F2", "D1", "R3", "U1", "R1", "U3", "R1", "D3", "F2"]
    elif (state == 20):
        return ["R2", "D3", "F1", "U3", "F1", "U1", "F3", "D1", "R2", "B1", "U3", "B3"]
    elif (state == 21):
        return ["R1", "U1", "R3", "F2", "D3", "L1", "U3", "L3", "U1", "L3", "D1", "F2"]

    # should never reach this
    return []









