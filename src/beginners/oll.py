import sys, os
sys.path.insert(0, os.path.abspath('src/cube'))

from moves import execute_moves
from facelet import Color as Cl

# https://www.speedcubereview.com/oll.html
# http://www.rubiksplace.com/speedcubing/OLL-algorithms/
# https://ruwix.com/the-rubiks-cube/advanced-cfop-fridrich/orient-the-last-layer-oll/
# 57 different states
def oll_state(cb):
    """
    Finds and returns the cube object's OLL state number; returns 0 if current
    state does not match any of the states
    """
    # no edges solved
    oll1 = ((cb[4] == Cl.U) and (cb[9] == Cl.U) and (cb[10] == Cl.U) 
            and (cb[11] == Cl.U) and (cb[19] == Cl.U) and (cb[36] == Cl.U)
            and (cb[37] == Cl.U) and (cb[38] == Cl.U) and (cb[46] == Cl.U))
    oll2 = ((cb[4] == Cl.U) and (cb[9] == Cl.U) and (cb[10] == Cl.U) 
            and (cb[19] == Cl.U) and (cb[37] == Cl.U) and (cb[38] == Cl.U)
            and (cb[45] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll3 = ((cb[0] == Cl.U) and (cb[4] == Cl.U) and (cb[10] == Cl.U) 
            and (cb[11] == Cl.U) and (cb[19] == Cl.U) and (cb[20] == Cl.U)
            and (cb[37] == Cl.U) and (cb[38] == Cl.U) and (cb[46] == Cl.U))
    oll4 = ((cb[2] == Cl.U) and (cb[4] == Cl.U) and (cb[9] == Cl.U) 
            and (cb[10] == Cl.U) and (cb[18] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))
    oll5 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[10] == Cl.U) and (cb[18] == Cl.U) and (cb[19] == Cl.U)
            and (cb[20] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))
    oll6 = ((cb[4] == Cl.U) and (cb[6] == Cl.U) and (cb[8] == Cl.U) 
            and (cb[10] == Cl.U) and (cb[11] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))
    oll7 = ((cb[0] == Cl.U) and (cb[4] == Cl.U) and (cb[8] == Cl.U) 
            and (cb[10] == Cl.U) and (cb[19] == Cl.U) and (cb[37] == Cl.U)
            and (cb[38] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))
    oll8 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[8] == Cl.U) and (cb[10] == Cl.U)
            and (cb[19] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))

    if oll1:
        return 1
    if oll2:
        return 2
    if oll3:
        return 3
    if oll4:
        return 4
    if oll5:
        return 5
    if oll6:
        return 6
    if oll7:
        return 7
    if oll8:
        return 8
    
    # L-shapes: no corners solved
    oll9 = ((cb[1] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[10] == Cl.U) and (cb[19] == Cl.U) and (cb[20] == Cl.U)
            and (cb[36] == Cl.U) and (cb[38] == Cl.U) and (cb[45] == Cl.U))
    oll10 = ((cb[1] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[9] == Cl.U) and (cb[11] == Cl.U) and (cb[18] == Cl.U)
            and (cb[19] == Cl.U) and (cb[37] == Cl.U) and (cb[47] == Cl.U))
    oll11 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[10] == Cl.U) and (cb[18] == Cl.U) and (cb[20] == Cl.U)
            and (cb[45] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll12 = ((cb[4] == Cl.U) and (cb[5] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[18] == Cl.U) and (cb[20] == Cl.U) and (cb[37] == Cl.U)
            and (cb[45] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll13 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[9] == Cl.U) and (cb[10] == Cl.U) and (cb[11] == Cl.U)
            and (cb[18] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll14 = ((cb[4] == Cl.U) and (cb[5] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[20] == Cl.U) and (cb[36] == Cl.U) and (cb[37] == Cl.U)
            and (cb[38] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))

    if oll9:
        return 9
    if oll10:
        return 10
    if oll11:
        return 11
    if oll12:
        return 12
    if oll13:
        return 13
    if oll14:
        return 14

    # L-shapes: one corner solved
    oll15 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[10] == Cl.U) and (cb[11] == Cl.U)
            and (cb[19] == Cl.U) and (cb[20] == Cl.U) and (cb[38] == Cl.U))
    oll16 = ((cb[1] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[9] == Cl.U) and (cb[18] == Cl.U)
            and (cb[19] == Cl.U) and (cb[36] == Cl.U) and (cb[37] == Cl.U))
    oll17 = ((cb[2] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[7] == Cl.U) and (cb[20] == Cl.U) and (cb[37] == Cl.U)
            and (cb[38] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll18 = ((cb[0] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[7] == Cl.U) and (cb[9] == Cl.U) and (cb[10] == Cl.U)
            and (cb[18] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))
    oll19 = ((cb[4] == Cl.U) and (cb[5] == Cl.U) and (cb[6] == Cl.U) 
            and (cb[7] == Cl.U) and (cb[11] == Cl.U) and (cb[20] == Cl.U)
            and (cb[37] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll20 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[8] == Cl.U) and (cb[10] == Cl.U) and (cb[18] == Cl.U)
            and (cb[36] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))
    oll21 = ((cb[1] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[8] == Cl.U) and (cb[10] == Cl.U) and (cb[18] == Cl.U)
            and (cb[19] == Cl.U) and (cb[36] == Cl.U) and (cb[45] == Cl.U))

    oll22 = ((cb[1] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[11] == Cl.U) and (cb[19] == Cl.U)
            and (cb[20] == Cl.U) and (cb[37] == Cl.U) and (cb[47] == Cl.U))
    
    if oll15:
        return 15
    if oll16:
        return 16
    if oll17:
        return 17
    if oll18:
        return 18
    if oll19:
        return 19
    if oll20:
        return 20
    if oll21:
        return 21
    if oll22:
        return 22

    # L-shapes: two corners solved
    oll23 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[6] == Cl.U) and (cb[9] == Cl.U)
            and (cb[10] == Cl.U) and (cb[11] == Cl.U) and (cb[19] == Cl.U))
    oll24 = ((cb[1] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[8] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[37] == Cl.U) and (cb[38] == Cl.U))
    oll25 = ((cb[1] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[8] == Cl.U) and (cb[18] == Cl.U)
            and (cb[19] == Cl.U) and (cb[37] == Cl.U) and (cb[47] == Cl.U))
    oll26 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[6] == Cl.U) and (cb[10] == Cl.U)
            and (cb[19] == Cl.U) and (cb[20] == Cl.U) and (cb[45] == Cl.U))
    oll27 = ((cb[0] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[7] == Cl.U) and (cb[8] == Cl.U) and (cb[11] == Cl.U)
            and (cb[18] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))
    oll28 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[8] == Cl.U) and (cb[10] == Cl.U)
            and (cb[11] == Cl.U) and (cb[18] == Cl.U) and (cb[19] == Cl.U))
    oll29 = ((cb[0] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[7] == Cl.U) and (cb[8] == Cl.U) and (cb[10] == Cl.U)
            and (cb[11] == Cl.U) and (cb[18] == Cl.U) and (cb[46] == Cl.U))
    oll30 = ((cb[2] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[7] == Cl.U) and (cb[20] == Cl.U)
            and (cb[36] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))
    oll31 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[7] == Cl.U) and (cb[9] == Cl.U)
            and (cb[10] == Cl.U) and (cb[38] == Cl.U) and (cb[46] == Cl.U))
    oll32 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[7] == Cl.U) and (cb[9] == Cl.U)
            and (cb[37] == Cl.U) and (cb[38] == Cl.U) and (cb[46] == Cl.U))
    oll33 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[7] == Cl.U) and (cb[10] == Cl.U)
            and (cb[18] == Cl.U) and (cb[20] == Cl.U) and (cb[46] == Cl.U))
    oll34 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[7] == Cl.U) and (cb[18] == Cl.U)
            and (cb[20] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))

    if oll23:
        return 23
    if oll24:
        return 24
    if oll25:
        return 25
    if oll25:
        return 26
    if oll27:
        return 27
    if oll28:
        return 28
    if oll29:
        return 29
    if oll30:
        return 30
    if oll31:
        return 31
    if oll32:
        return 32
    if oll33:
        return 33
    if oll34:
        return 34

    # L-shapes: four corners solved
    oll35 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[6] == Cl.U) and (cb[7] == Cl.U)
            and (cb[8] == Cl.U) and (cb[37] == Cl.U) and (cb[46] == Cl.U))

    if oll35:
        return 35
    
    # Bar-shapes: no corners solved
    oll36 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[9] == Cl.U) and (cb[11] == Cl.U) and (cb[18] == Cl.U)
            and (cb[19] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll37 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[9] == Cl.U) and (cb[11] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[38] == Cl.U) and (cb[46] == Cl.U))
    oll38 = ((cb[1] == Cl.U) and (cb[4] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[9] == Cl.U) and (cb[10] == Cl.U) and (cb[11] == Cl.U)
            and (cb[18] == Cl.U) and (cb[37] == Cl.U) and (cb[47] == Cl.U))
    oll39 = ((cb[1] == Cl.U) and (cb[4] == Cl.U) and (cb[7] == Cl.U) 
            and (cb[9] == Cl.U) and (cb[10] == Cl.U) and (cb[11] == Cl.U)
            and (cb[36] == Cl.U) and (cb[37] == Cl.U) and (cb[38] == Cl.U))

    if oll36:
        return 36
    if oll37:
        return 37
    if oll38:
        return 38
    if oll39:
        return 39

    # Bar-shapes: one corner solved
    oll40 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[8] == Cl.U) and (cb[11] == Cl.U) and (cb[19] == Cl.U)
            and (cb[38] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll41 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[9] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))
    oll42 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[11] == Cl.U) and (cb[19] == Cl.U)
            and (cb[20] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll43 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[8] == Cl.U) and (cb[18] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))

    if oll40:
        return 40
    if oll41:
        return 41
    if oll42:
        return 42
    if oll43:
        return 43


    # Bar-shapes: two corners solved
    oll44 = ((cb[2] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[8] == Cl.U) and (cb[18] == Cl.U)
            and (cb[19] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))
    oll45 = ((cb[2] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[8] == Cl.U) and (cb[19] == Cl.U)
            and (cb[36] == Cl.U) and (cb[38] == Cl.U) and (cb[46] == Cl.U))
    oll46 = ((cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[8] == Cl.U) and (cb[11] == Cl.U)
            and (cb[19] == Cl.U) and (cb[36] == Cl.U) and (cb[46] == Cl.U))
    oll47 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[6] == Cl.U) and (cb[7] == Cl.U) and (cb[9] == Cl.U)
            and (cb[10] == Cl.U) and (cb[11] == Cl.U) and (cb[37] == Cl.U))
    oll48 = ((cb[0] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[8] == Cl.U) and (cb[19] == Cl.U)
            and (cb[38] == Cl.U) and (cb[45] == Cl.U) and (cb[46] == Cl.U))
    oll49 = ((cb[2] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[6] == Cl.U) and (cb[9] == Cl.U)
            and (cb[19] == Cl.U) and (cb[46] == Cl.U) and (cb[47] == Cl.U))

    if oll44:
        return 44
    if oll45:
        return 45
    if oll46:
        return 46
    if oll47:
        return 47
    if oll48:
        return 48
    if oll49:
        return 49

    # Bar-shapes: four corners solved
    oll50 = ((cb[0] == Cl.U) and (cb[2] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[5] == Cl.U) and (cb[6] == Cl.U)
            and (cb[8] == Cl.U) and (cb[19] == Cl.U) and (cb[46] == Cl.U))

    if oll50:
        return 50

    # Cross: four edges solved
    oll51 = ((cb[1] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[7] == Cl.U) and (cb[18] == Cl.U)
            and (cb[20] == Cl.U) and (cb[45] == Cl.U) and (cb[47] == Cl.U))
    oll52 = ((cb[1] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[7] == Cl.U) and (cb[20] == Cl.U)
            and (cb[36] == Cl.U) and (cb[38] == Cl.U) and (cb[45] == Cl.U))
    oll53 = ((cb[1] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[6] == Cl.U) and (cb[7] == Cl.U)
            and (cb[11] == Cl.U) and (cb[20] == Cl.U) and (cb[47] == Cl.U))
    oll54 = ((cb[1] == Cl.U) and (cb[3] == Cl.U) and (cb[4] == Cl.U) 
            and (cb[5] == Cl.U) and (cb[7] == Cl.U) and (cb[8] == Cl.U)
            and (cb[18] == Cl.U) and (cb[36] == Cl.U) and (cb[45] == Cl.U))
    oll55 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[5] == Cl.U) and (cb[7] == Cl.U)
            and (cb[8] == Cl.U) and (cb[11] == Cl.U) and (cb[18] == Cl.U))
    oll56 = ((cb[0] == Cl.U) and (cb[1] == Cl.U) and (cb[2] == Cl.U) 
            and (cb[3] == Cl.U) and (cb[4] == Cl.U) and (cb[5] == Cl.U)
            and (cb[7] == Cl.U) and (cb[18] == Cl.U) and (cb[20] == Cl.U))
    oll57 = ((cb[1] == Cl.U) and (cb[2] == Cl.U) and (cb[3] == Cl.U) 
            and (cb[4] == Cl.U) and (cb[5] == Cl.U) and (cb[7] == Cl.U)
            and (cb[8] == Cl.U) and (cb[18] == Cl.U) and (cb[47] == Cl.U))

    if oll51:
        return 51
    if oll52:
        return 52
    if oll53:
        return 53
    if oll54:
        return 54
    if oll55:
        return 55
    if oll56:
        return 56
    if oll57:
        return 57

    return 0

def oll_moves(cube_obj, state):
    """
    Returns the moves list to orient the top layer
    """
    print("oll state: %s" % state)
    # no edges solved
    if (state == 1):
        return ["R1", "U2", "R2", "F1", "R1", "F3", "U2", "R3", "F1", "R1", "F3"]
    elif (state == 2):
        return ["R3", "F3", "R1", "U2", "L3", "U2", "L1", "U2", "R3", "F1", "R1"]
    elif (state == 3):
        return ["F1", "U1", "R1", "U3", "R3", "F3", "U1", "F1", "R1", "U1", "R3", "U3", "F3"]
    elif (state == 4):
        return ["F3", "U3", "L3", "U1", "L1", "F1", "U1", "F1", "R1", "U1", "R3", "U3", "F3"]
    elif (state == 5):
        return ["F1", "R3", "F3", "R1", "U1", "R1", "U3", "R3", "U1", "F1", "R1", "U1", "R3", "U3", "F3"]
    elif (state == 6):
        return ["F1", "R3", "F3", "R1", "U1", "R1", "U3", "R3", "U3", "F1", "R1", "U1", "R3", "U3", "F3"]
    elif (state == 7):
        return ["R1", "U1", "R3", "U1", "R3", "F1", "R1", "F3", "U2", "R3", "F1" ,"R1", "F3"]
    elif (state == 8):
        return ["L1", "R3", "F2", "L3", "R1", "U2", "L1", "R3", "F1", "L3", "R1", "U2", "L1", "R3", "F2", "L3", "R1"]
    
    # L-shapes: no corners solved
    elif (state == 9):
        return ["F1", "R1", "U1", "R3", "U3", "R1", "U1", "R3", "U3", "F3"]
    elif (state == 10):
        return ["F3", "L3", "U3", "L1", "U1", "L3", "U3", "L1", "U1", "F1"]
    elif (state == 11):
        return ["L3", "B3", "L1", "R3", "U3", "R1", "U1", "R3", "U3", "R1", "U1", "L3", "B1", "L1"]
    elif (state == 12):
        return ["R1", "B1", "R3", "L1", "U1", "L3", "U3", "L1", "U1", "L3", "U3", "R1", "B3", "R3"]
    elif (state == 13):
        return ["R1", "B3", "R2", "F1", "R2", "B1", "R2", "F3", "R1"]
    elif (state == 14):
        return ["L3", "B1", "L2", "F3", "L2", "B3", "L2", "F1", "L3"]
    
    # L-shapes: one corner solved
    elif (state == 15):
        return ["R3", "F2", "L1", "F1", "L3", "F1", "R1"]
    elif (state == 16):
        return ["L1", "F2", "R3", "F3", "R1", "F3", "L3"]
    elif (state == 17):
        return ["R1", "B1", "L3", "B1", "L1", "B2", "R3"]
    elif (state == 18):
        return ["L3", "B3", "L1", "U3", "R3", "U1", "R1", "L3", "B1", "L1"]
    elif (state == 19):
        return ["L3", "R2", "B1", "R3", "B1", "R1", "B2", "R3", "B1", "L1", "R3"]
    elif (state == 20):
        return ["L2", "R1", "B3", "L1", "B3", "L3", "B2", "L1", "B3", "L1", "R3"]
    elif (state == 21):
        return ["R1", "U1", "R3", "U3", "R3", "F1", "R2", "U1", "R3", "U3", "F3"]
    elif (state == 22):
        return ["L3", "U3", "L1", "U1", "L1", "F3", "L2", "U3", "L1", "U1", "F1"]

    # L-shapes: two corners solved
    elif (state == 23):
        return ["F1", "U1", "R1", "U3", "R3", "F3"]
    elif (state == 24):
        return ["F3", "U3", "L3", "U1", "L1", "F1"]
    elif (state == 25):
        return ["R3", "U3", "F1", "U1", "R1", "U3", "R3", "F3", "R1"]
    elif (state == 26):
        return ["L1", "U1", "F3", "U3", "L3", "U1", "L1", "F1", "L3"]
    elif (state == 27):
        return ["R1", "U2", "R2", "F1", "R1", "F3", "R1", "U2", "R3"]
    elif (state == 28):
        return ["F1", "R3", "F3", "R1", "U1", "R1", "U3", "R3"]
    elif (state == 29):
        return ["R3", "U3", "R1", "U3", "R3", "U1", "R1", "U1", "R1", "B3", "R3", "B1"]
    elif (state == 30):
        return ["L1", "U1", "L3", "U1", "L1", "U3", "L3", "U3", "L3", "B1", "L1", "B3"]
    elif (state == 31):
        return ["L3", "R1", "B1", "R1", "B1", "R3", "B3", "R3", "U1", "R1", "U3", "L1", "R3"]
    elif (state == 32):
        return ["R2", "U1", "R3", "B3", "R1", "U3", "R2", "U1", "R1", "B1", "R3"]
    elif (state == 33):
        return ["L3", "U1", "L1", "U2", "L3", "U3", "B3", "U1", "B1", "U1", "L1"]
    elif (state == 34):
        return ["L3", "R1", "B3", "U3", "L3", "B3", "L1", "B1", "U1", "L1", "R3"]

    # L-shapes: four corners solved
    elif (state == 35):
        return ["L1", "R3", "F1", "L3", "R1", "U2", "L1", "R3", "F1", "L3", "R1"]

    # Bar-shapes: no corners solved
    elif (state == 36):
        return ["F1", "U1", "R1", "U3", "R3", "U1", "R1", "U3", "R3", "F3"]
    elif (state == 37):
        return ["L3", "B3", "L1", "U3", "R3", "U1", "R1", "U3", "R3", "U1", "R1", "L3", "B1", "L1"]
    elif (state == 38):
        return ["R1", "U1", "R3", "U1", "R1", "U3", "B1", "U3", "B3", "R3"]
    elif (state == 39):
        return ["R1", "U2", "R2", "U3", "R1", "U3", "R3", "U2", "F1", "R1", "F3"]

    # Bar-shapes: one corner solved
    elif (state == 40):
        return ["L3", "B3", "L1", "R3", "U3", "R1", "U1", "L3", "B1", "L1"]
    elif (state == 41):
        return ["R1", "B1", "R3", "L1", "U1", "L3", "U3", "R1", "B3", "R3"]
    elif (state == 42):
        return ["L1", "F3", "L3", "U3", "L1", "F1", "L3", "F3", "U1", "F3"]
    elif (state == 43):
        return ["R3", "F1", "R1", "U1", "R3", "F3", "R1", "F1", "U3", "F3"]

    # Bar-shapes: two corners solved
    elif (state == 44):
        return ["R1", "U1", "R3", "U3", "R3", "F1", "R1", "F3"]
    elif (state == 45):
        return ["F1", "R1", "U1", "R3", "U3", "F3"]
    elif (state == 46):
        return ["R1", "U1", "R3", "U3", "B3", "R3", "F1", "R1", "F3", "B1"]
    elif (state == 47):
        return ["R3", "U3", "R3", "F1", "R1", "F3", "U1", "R1"]
    elif (state == 48):
        return ["R3", "F1", "R1", "U1", "R3", "U3", "F3", "U1", "R1"]
    elif (state == 49):
        return ["L1", "F3", "L3", "U3", "L1", "U1", "F1", "U3", "L3"]

    # Bar-shapes: four corners solved
    elif (state == 50):
        return ["R1", "U1", "R3", "U3", "L1", "R3", "F1", "R1", "F3", "L3"]

    # Cross: four edges solved
    elif (state == 51):
        return ["R1", "U2", "R3", "U3", "R1", "U1", "R3", "U3", "R1", "U3", "R3"]
    elif (state == 52):
        return ["R1", "U2", "R2", "U3", "R2", "U3", "R2", "U2", "R1"]
    elif (state == 53):
        return ["R1", "U1", "R3", "U1", "R1", "U2", "R3"]
    elif (state == 54):
        return ["L3", "U3", "L1", "U3", "L3", "U2", "L1"]
    elif (state == 55):
        return ["R3", "F1", "R1", "B3", "R3", "F3", "R1", "B1"]
    elif (state == 56):
        return ["R2", "D1", "R3", "U2", "R1", "D3", "R3", "U2", "R3"]
    elif (state == 57):
        return ["L3", "B3", "R1", "B1", "L1", "B3", "R3", "B1"]
    
    # should never reach this
    return []
