import cube
from facelet import Move as Mv

# cube_obj = cube.Cube()

"""
CUBE ROTATION MOVES
The eighteen types of cube rotation moves are the following (see facelet.py):
    90 degrees CW        90 degrees CCW        180 degrees
    U1: U                U2: U'                U3: U2
    R1: R                R2: R'                R3: R2
    F1: F                F2: F'                F3: F2
    D1: D                D2: D'                D3: D2
    L1: L                L2: L'                L3: L2
    B1: B                B2: B'                B3: B2
"""
def U1(cube_obj):
    """
    90 degree clockwise turn of the U face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[6]
    new_c[1] = c[3]
    new_c[2] = c[0]
    new_c[3] = c[7]
    new_c[4] = c[4] # U center piece
    new_c[5] = c[1]
    new_c[6] = c[8]
    new_c[7] = c[5]
    new_c[8] = c[2]
    new_c[9] = c[45]
    new_c[10] = c[46]
    new_c[11] = c[47]
    new_c[18] = c[9]
    new_c[19] = c[10]
    new_c[20] = c[11]
    new_c[36] = c[18]
    new_c[37] = c[19]
    new_c[38] = c[20]
    new_c[45] = c[36]
    new_c[46] = c[37]
    new_c[47] = c[38]

    return new_c

def U2(cube_obj):
    """
    90 degree counterclockwise turn of the U face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[2]
    new_c[1] = c[5]
    new_c[2] = c[8]
    new_c[3] = c[1]
    new_c[4] = c[4] # U center piece
    new_c[5] = c[7]
    new_c[6] = c[0]
    new_c[7] = c[3]
    new_c[8] = c[6]
    new_c[9] = c[18]
    new_c[10] = c[19]
    new_c[11] = c[20]
    new_c[18] = c[36]
    new_c[19] = c[37]
    new_c[20] = c[38]
    new_c[36] = c[45]
    new_c[37] = c[46]
    new_c[38] = c[47]
    new_c[45] = c[9]
    new_c[46] = c[10]
    new_c[47] = c[11]

    return new_c

def U3(cube_obj):
    """
    180 degree turn of the U face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[8]
    new_c[1] = c[7]
    new_c[2] = c[6]
    new_c[3] = c[5]
    new_c[4] = c[4] # U center piece
    new_c[5] = c[3]
    new_c[6] = c[2]
    new_c[7] = c[1]
    new_c[8] = c[0]
    new_c[9] = c[18]
    new_c[10] = c[19]
    new_c[11] = c[20]
    new_c[18] = c[36]
    new_c[19] = c[37]
    new_c[20] = c[38]
    new_c[36] = c[45]
    new_c[37] = c[46]
    new_c[38] = c[47]
    new_c[45] = c[9]
    new_c[46] = c[10]
    new_c[47] = c[11]

    return new_c

def R1(cube_obj):
    """
    90 degree clockwise turn of the R face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[2] = c[20]
    new_c[5] = c[23]
    new_c[8] = c[26]
    new_c[9] = c[15]
    new_c[10] = c[12]
    new_c[11] = c[9]
    new_c[12] = c[16]
    new_c[13] = c[13] # R center piece
    new_c[14] = c[10]
    new_c[15] = c[17]
    new_c[16] = c[14]
    new_c[17] = c[11]
    new_c[20] = c[29]
    new_c[23] = c[32]
    new_c[26] = c[35]
    new_c[29] = c[51]
    new_c[32] = c[48]
    new_c[35] = c[45]
    new_c[45] = c[8]
    new_c[48] = c[5]
    new_c[51] = c[2]

    return new_c

def R2(cube_obj):
    """
    90 degree counterclockwise turn of the R face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[2] = c[51]
    new_c[5] = c[48]
    new_c[8] = c[45]
    new_c[9] = c[11]
    new_c[10] = c[14]
    new_c[11] = c[17]
    new_c[12] = c[10]
    new_c[13] = c[13] # R center piece
    new_c[14] = c[16]
    new_c[15] = c[9]
    new_c[16] = c[12]
    new_c[17] = c[15]
    new_c[20] = c[2]
    new_c[23] = c[5]
    new_c[26] = c[8]
    new_c[29] = c[20]
    new_c[32] = c[23]
    new_c[35] = c[26]
    new_c[45] = c[35]
    new_c[48] = c[32]
    new_c[51] = c[29]

    return new_c

def R3(cube_obj):
    """
    180 degree turn of the R face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[2] = c[29]
    new_c[5] = c[32]
    new_c[8] = c[35]
    new_c[9] = c[17]
    new_c[10] = c[16]
    new_c[11] = c[15]
    new_c[12] = c[14]
    new_c[13] = c[13] # R center piece
    new_c[14] = c[12]
    new_c[15] = c[11]
    new_c[16] = c[10]
    new_c[17] = c[9]
    new_c[20] = c[51]
    new_c[23] = c[48]
    new_c[26] = c[45]
    new_c[29] = c[2]
    new_c[32] = c[5]
    new_c[35] = c[8]
    new_c[45] = c[26]
    new_c[48] = c[23]
    new_c[51] = c[20]

    return new_c

def F1(cube_obj):
    """
    90 degree clockwise turn of the F face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[6] = c[44]
    new_c[7] = c[41]
    new_c[8] = c[38]
    new_c[9] = c[6]
    new_c[12] = c[7]
    new_c[15] = c[8]
    new_c[18] = c[24]
    new_c[19] = c[21]
    new_c[20] = c[18]
    new_c[21] = c[25]
    new_c[22] = c[22] # F center piece
    new_c[23] = c[19]
    new_c[24] = c[26]
    new_c[25] = c[23]
    new_c[26] = c[20]
    new_c[27] = c[15]
    new_c[28] = c[12]
    new_c[29] = c[9]
    new_c[38] = c[27]
    new_c[41] = c[28]
    new_c[44] = c[29]

    return new_c

def F2(cube_obj):
    """
    90 degree counterclockwise turn of the F face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[6] = c[9]
    new_c[7] = c[12]
    new_c[8] = c[15]
    new_c[9] = c[29]
    new_c[12] = c[28]
    new_c[15] = c[27]
    new_c[18] = c[20]
    new_c[19] = c[23]
    new_c[20] = c[26]
    new_c[21] = c[19]
    new_c[22] = c[22]  # F center piece
    new_c[23] = c[25]
    new_c[24] = c[18]
    new_c[25] = c[21]
    new_c[26] = c[24]
    new_c[27] = c[38]
    new_c[28] = c[41]
    new_c[29] = c[44]
    new_c[38] = c[8]
    new_c[41] = c[7]
    new_c[44] = c[6]

    return new_c

def F3(cube_obj):
    """
    180 degree turn of the F face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[6] = c[29]
    new_c[7] = c[28]
    new_c[8] = c[27]
    new_c[9] = c[44]
    new_c[12] = c[41]
    new_c[15] = c[38]
    new_c[18] = c[26]
    new_c[19] = c[25]
    new_c[20] = c[25]
    new_c[21] = c[23]
    new_c[22] = c[22]  # F center piece
    new_c[23] = c[21]
    new_c[24] = c[20]
    new_c[25] = c[19]
    new_c[26] = c[18]
    new_c[27] = c[8]
    new_c[28] = c[7]
    new_c[29] = c[6]
    new_c[38] = c[15]
    new_c[41] = c[12]
    new_c[44] = c[9]

    return new_c

def D1(cube_obj):
    """
    90 degree clockwise turn of the D face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[15] = c[24]
    new_c[16] = c[25]
    new_c[17] = c[26]
    new_c[24] = c[42]
    new_c[25] = c[43]
    new_c[26] = c[44]
    new_c[27] = c[33]
    new_c[28] = c[30]
    new_c[29] = c[27]
    new_c[30] = c[34]
    new_c[31] = c[31] # D center piece
    new_c[32] = c[28]
    new_c[33] = c[35]
    new_c[34] = c[32]
    new_c[35] = c[29]
    new_c[42] = c[51]
    new_c[43] = c[52]
    new_c[44] = c[53]
    new_c[51] = c[15]
    new_c[52] = c[16]
    new_c[53] = c[17]

    return new_c

def D2(cube_obj):
    """
    90 degree counterclockwise turn of the D face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[15] = c[51]
    new_c[16] = c[52]
    new_c[17] = c[53]
    new_c[24] = c[15]
    new_c[25] = c[16]
    new_c[26] = c[17]
    new_c[27] = c[29]
    new_c[28] = c[32]
    new_c[29] = c[35]
    new_c[30] = c[28]
    new_c[31] = c[31] # D center piece
    new_c[32] = c[34]
    new_c[33] = c[27]
    new_c[34] = c[30]
    new_c[35] = c[33]
    new_c[42] = c[24]
    new_c[43] = c[25]
    new_c[44] = c[26]
    new_c[51] = c[42]
    new_c[52] = c[43]
    new_c[53] = c[44]

    return new_c

def D3(cube_obj):
    """
    180 degree turn of the D face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[15] = c[42]
    new_c[16] = c[43]
    new_c[17] = c[44]
    new_c[24] = c[51]
    new_c[25] = c[52]
    new_c[26] = c[53]
    new_c[27] = c[35]
    new_c[28] = c[34]
    new_c[29] = c[33]
    new_c[30] = c[32]
    new_c[31] = c[31] # D center piece
    new_c[32] = c[30]
    new_c[33] = c[29]
    new_c[34] = c[28]
    new_c[35] = c[27]
    new_c[42] = c[15]
    new_c[43] = c[16]
    new_c[44] = c[17]
    new_c[51] = c[24]
    new_c[52] = c[25]
    new_c[53] = c[26]

    return new_c

def L1(cube_obj):
    """
    90 degree clockwise turn of the L face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[53]
    new_c[3] = c[50]
    new_c[6] = c[47]
    new_c[18] = c[0]
    new_c[21] = c[3]
    new_c[24] = c[6]
    new_c[27] = c[18]
    new_c[30] = c[21]
    new_c[33] = c[24]
    new_c[36] = c[42]
    new_c[37] = c[39]
    new_c[38] = c[36]
    new_c[39] = c[43]
    new_c[40] = c[40] # L center piece
    new_c[41] = c[37]
    new_c[42] = c[44]
    new_c[43] = c[41]
    new_c[44] = c[38]
    new_c[47] = c[33]
    new_c[50] = c[30]
    new_c[53] = c[27]

    return new_c

def L2(cube_obj):
    """
    90 degree counterclockwise turn of the L face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[18]
    new_c[3] = c[21]
    new_c[6] = c[24]
    new_c[18] = c[27]
    new_c[21] = c[30]
    new_c[24] = c[33]
    new_c[27] = c[53]
    new_c[30] = c[50]
    new_c[33] = c[47]
    new_c[36] = c[38]
    new_c[37] = c[41]
    new_c[38] = c[44]
    new_c[39] = c[37]
    new_c[40] = c[40] # L center piece
    new_c[41] = c[43]
    new_c[42] = c[36]
    new_c[43] = c[39]
    new_c[44] = c[42]
    new_c[47] = c[6]
    new_c[50] = c[3]
    new_c[53] = c[0]

    return new_c

def L3(cube_obj):
    """
    180 degree turn of the L face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[27]
    new_c[3] = c[30]
    new_c[6] = c[33]
    new_c[18] = c[53]
    new_c[21] = c[50]
    new_c[24] = c[47]
    new_c[27] = c[0]
    new_c[30] = c[3]
    new_c[33] = c[6]
    new_c[36] = c[44]
    new_c[37] = c[43]
    new_c[38] = c[42]
    new_c[39] = c[41]
    new_c[40] = c[40] # L center piece
    new_c[41] = c[39]
    new_c[42] = c[38]
    new_c[43] = c[37]
    new_c[44] = c[36]
    new_c[47] = c[24]
    new_c[50] = c[21]
    new_c[53] = c[18]

    return new_c

def B1(cube_obj):
    """
    90 degree clockwise turn of the B face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[11]
    new_c[1] = c[14]
    new_c[2] = c[17]
    new_c[11] = c[35]
    new_c[14] = c[34]
    new_c[17] = c[33]
    new_c[33] = c[36]
    new_c[34] = c[39]
    new_c[35] = c[42]
    new_c[36] = c[2]
    new_c[39] = c[1]
    new_c[42] = c[0]
    new_c[45] = c[51]
    new_c[46] = c[48]
    new_c[47] = c[45]
    new_c[48] = c[52]
    new_c[49] = c[49] # B center piece
    new_c[50] = c[46]
    new_c[51] = c[53]
    new_c[52] = c[50]
    new_c[53] = c[47]

    return new_c

def B2(cube_obj):
    """
    90 degree counterclockwise turn of the B face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[35]
    new_c[1] = c[34]
    new_c[2] = c[33]
    new_c[11] = c[42]
    new_c[14] = c[39]
    new_c[17] = c[36]
    new_c[33] = c[2]
    new_c[34] = c[1]
    new_c[35] = c[0]
    new_c[36] = c[17]
    new_c[39] = c[14]
    new_c[42] = c[11]
    new_c[45] = c[53]
    new_c[46] = c[52]
    new_c[47] = c[51]
    new_c[48] = c[50]
    new_c[49] = c[49] # B center piece
    new_c[50] = c[48]
    new_c[51] = c[47]
    new_c[52] = c[46]
    new_c[53] = c[45]

    return new_c

def B3(cube_obj):
    """
    180 degree turn of the B face
    """
    c = cube_obj.c
    new_c = c.copy()

    new_c[0] = c[42]
    new_c[1] = c[39]
    new_c[2] = c[36]
    new_c[11] = c[0]
    new_c[14] = c[1]
    new_c[17] = c[2]
    new_c[33] = c[17]
    new_c[34] = c[14]
    new_c[35] = c[11]
    new_c[36] = c[33]
    new_c[39] = c[34]
    new_c[42] = c[35]
    new_c[45] = c[47]
    new_c[46] = c[50]
    new_c[47] = c[53]
    new_c[48] = c[46]
    new_c[49] = c[49] # B center piece
    new_c[50] = c[52]
    new_c[51] = c[45]
    new_c[52] = c[48]
    new_c[53] = c[51]

    return new_c

def check_current_cube(c):
    """
    Check if
    """
    try:
        assert(type(c) == list)
    except AssertionError:
        print("current cube config must be of type list, is type %s\n"
              % type(c))

    con_len = len(c)
    try:
        assert(con_len == 54)
    except AssertionError:
        print("invalid configuration; must have length of 54\n"
              + "currently is length " + str(con_len) + "\n")

    count = [0] * 6  # number of faces
    for i in range(con_len):
        if c[i] == Cl.U:
            count[Cl.U] += 1

        elif c[i] == Cl.R:
            count[Cl.R] += 1

        elif c[i] == Cl.F:
            count[Cl.F] += 1

        elif c[i] == Cl.D:
            count[Cl.D] += 1

        elif c[i] == Cl.L:
            count[Cl.L] += 1

        elif c[i] == Cl.B:
            count[Cl.B] += 1

    if all(elem == 9 for elem in count):  # 9 facelets per face
        return True
    return False

def execute_move(c, move):
    """
    Executes the specified move on the cube.
    NOTE: Python does NOT have switch-case functionality; official docs suggest
    using if-elif-...-else but this feels inelegant.
    """
    moves = {
        U1: "U",
        U2: "U\'",
        U3: "U2",
        R1: "R",
        R2: "R\'",
        R3: "R2",
        F1: "F",
        F2: "F\'",
        F3: "F2",
        D1: "D",
        D2: "D\'",
        D3: "D2",
        L1: "L",
        L2: "L\'",
        L3: "L2",
        B1: "B",
        B2: "B\'",
        B3: "B2"
    }

    if move in moves:
        move_str = moves.get(move, "Invalid move specification.\n")
        new_c = move(cube_obj)

        try:
            assert(check_current_cube(new_c))
            cube_obj.update_state(new_c)
            cube_obj.add_move(move_str)
        except AssertionError:
            print("Move failed!!! %s\n" % move_str)

    else:
        print("invalid move")
