from cube import Cube
from facelet import Move as Mv, Color as Cl, Corner as Cn, Edge as Ed

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
def U1(cb):
    """
    90 degree clockwise turn of the U face
    """
    new_c = cb.copy()

    new_c[0] = cb[6]
    new_c[1] = cb[3]
    new_c[2] = cb[0]
    new_c[3] = cb[7]
    new_c[4] = cb[4] # U center piece
    new_c[5] = cb[1]
    new_c[6] = cb[8]
    new_c[7] = cb[5]
    new_c[8] = cb[2]
    new_c[9] = cb[45]
    new_c[10] = cb[46]
    new_c[11] = cb[47]
    new_c[18] = cb[9]
    new_c[19] = cb[10]
    new_c[20] = cb[11]
    new_c[36] = cb[18]
    new_c[37] = cb[19]
    new_c[38] = cb[20]
    new_c[45] = cb[36]
    new_c[46] = cb[37]
    new_c[47] = cb[38]

    return new_c

def U2(cb):
    """
    90 degree counterclockwise turn of the U face
    """
    new_c = cb.copy()

    new_c[0] = cb[2]
    new_c[1] = cb[5]
    new_c[2] = cb[8]
    new_c[3] = cb[1]
    new_c[4] = cb[4] # U center piece
    new_c[5] = cb[7]
    new_c[6] = cb[0]
    new_c[7] = cb[3]
    new_c[8] = cb[6]
    new_c[9] = cb[18]
    new_c[10] = cb[19]
    new_c[11] = cb[20]
    new_c[18] = cb[36]
    new_c[19] = cb[37]
    new_c[20] = cb[38]
    new_c[36] = cb[45]
    new_c[37] = cb[46]
    new_c[38] = cb[47]
    new_c[45] = cb[9]
    new_c[46] = cb[10]
    new_c[47] = cb[11]

    return new_c

def U3(cb):
    """
    180 degree turn of the U face
    """
    new_c = cb.copy()

    new_c[0] = cb[8]
    new_c[1] = cb[7]
    new_c[2] = cb[6]
    new_c[3] = cb[5]
    new_c[4] = cb[4] # U center piece
    new_c[5] = cb[3]
    new_c[6] = cb[2]
    new_c[7] = cb[1]
    new_c[8] = cb[0]
    new_c[9] = cb[36]
    new_c[10] = cb[37]
    new_c[11] = cb[38]
    new_c[18] = cb[45]
    new_c[19] = cb[46]
    new_c[20] = cb[47]
    new_c[36] = cb[9]
    new_c[37] = cb[10]
    new_c[38] = cb[11]
    new_c[45] = cb[18]
    new_c[46] = cb[19]
    new_c[47] = cb[20]

    return new_c

def R1(cb):
    """
    90 degree clockwise turn of the R face
    """
    new_c = cb.copy()

    new_c[2] = cb[20]
    new_c[5] = cb[23]
    new_c[8] = cb[26]
    new_c[9] = cb[11]
    new_c[10] = cb[10]
    new_c[11] = cb[9]
    new_c[12] = cb[14]
    new_c[13] = cb[13] # R center piece
    new_c[14] = cb[12]
    new_c[15] = cb[17]
    new_c[16] = cb[16]
    new_c[17] = cb[15]
    new_c[20] = cb[29]
    new_c[23] = cb[32]
    new_c[26] = cb[35]
    new_c[29] = cb[51]
    new_c[32] = cb[48]
    new_c[35] = cb[45]
    new_c[45] = cb[8]
    new_c[48] = cb[5]
    new_c[51] = cb[2]

    return new_c

def R2(cb):
    """
    90 degree counterclockwise turn of the R face
    """
    new_c = cb.copy()

    new_c[2] = cb[51]
    new_c[5] = cb[48]
    new_c[8] = cb[45]
    new_c[9] = cb[15]
    new_c[10] = cb[16]
    new_c[11] = cb[17]
    new_c[12] = cb[12]
    new_c[13] = cb[13] # R center piece
    new_c[14] = cb[14]
    new_c[15] = cb[9]
    new_c[16] = cb[10]
    new_c[17] = cb[11]
    new_c[20] = cb[2]
    new_c[23] = cb[5]
    new_c[26] = cb[8]
    new_c[29] = cb[20]
    new_c[32] = cb[23]
    new_c[35] = cb[26]
    new_c[45] = cb[35]
    new_c[48] = cb[32]
    new_c[51] = cb[29]

    return new_c

def R3(cb):
    """
    180 degree turn of the R face
    """
    new_c = cb.copy()

    new_c[2] = cb[29]
    new_c[5] = cb[32]
    new_c[8] = cb[35]
    new_c[9] = cb[17]
    new_c[10] = cb[16]
    new_c[11] = cb[15]
    new_c[12] = cb[14]
    new_c[13] = cb[13] # R center piece
    new_c[14] = cb[12]
    new_c[15] = cb[11]
    new_c[16] = cb[10]
    new_c[17] = cb[9]
    new_c[20] = cb[51]
    new_c[23] = cb[48]
    new_c[26] = cb[45]
    new_c[29] = cb[2]
    new_c[32] = cb[5]
    new_c[35] = cb[8]
    new_c[45] = cb[26]
    new_c[48] = cb[23]
    new_c[51] = cb[20]

    return new_c

def F1(cb):
    """
    90 degree clockwise turn of the F face
    """
    new_c = cb.copy()

    new_c[6] = cb[44]
    new_c[7] = cb[41]
    new_c[8] = cb[38]
    new_c[9] = cb[6]
    new_c[12] = cb[7]
    new_c[15] = cb[8]
    new_c[18] = cb[24]
    new_c[19] = cb[21]
    new_c[20] = cb[18]
    new_c[21] = cb[25]
    new_c[22] = cb[22] # F center piece
    new_c[23] = cb[19]
    new_c[24] = cb[26]
    new_c[25] = cb[23]
    new_c[26] = cb[20]
    new_c[27] = cb[15]
    new_c[28] = cb[12]
    new_c[29] = cb[9]
    new_c[38] = cb[27]
    new_c[41] = cb[28]
    new_c[44] = cb[29]

    return new_c

def F2(cb):
    """
    90 degree counterclockwise turn of the F face
    """
    new_c = cb.copy()

    new_c[6] = cb[9]
    new_c[7] = cb[12]
    new_c[8] = cb[15]
    new_c[9] = cb[29]
    new_c[12] = cb[28]
    new_c[15] = cb[27]
    new_c[18] = cb[20]
    new_c[19] = cb[23]
    new_c[20] = cb[26]
    new_c[21] = cb[19]
    new_c[22] = cb[22]  # F center piece
    new_c[23] = cb[25]
    new_c[24] = cb[18]
    new_c[25] = cb[21]
    new_c[26] = cb[24]
    new_c[27] = cb[38]
    new_c[28] = cb[41]
    new_c[29] = cb[44]
    new_c[38] = cb[8]
    new_c[41] = cb[7]
    new_c[44] = cb[6]

    return new_c

def F3(cb):
    """
    180 degree turn of the F face
    """
    new_c = cb.copy()

    new_c[6] = cb[29]
    new_c[7] = cb[28]
    new_c[8] = cb[27]
    new_c[9] = cb[44]
    new_c[12] = cb[41]
    new_c[15] = cb[38]
    new_c[18] = cb[26]
    new_c[19] = cb[25]
    new_c[20] = cb[25]
    new_c[21] = cb[23]
    new_c[22] = cb[22]  # F center piece
    new_c[23] = cb[21]
    new_c[24] = cb[20]
    new_c[25] = cb[19]
    new_c[26] = cb[18]
    new_c[27] = cb[8]
    new_c[28] = cb[7]
    new_c[29] = cb[6]
    new_c[38] = cb[15]
    new_c[41] = cb[12]
    new_c[44] = cb[9]

    return new_c

def D1(cb):
    """
    90 degree clockwise turn of the D face
    """
    new_c = cb.copy()

    new_c[15] = cb[24]
    new_c[16] = cb[25]
    new_c[17] = cb[26]
    new_c[24] = cb[42]
    new_c[25] = cb[43]
    new_c[26] = cb[44]
    new_c[27] = cb[33]
    new_c[28] = cb[30]
    new_c[29] = cb[27]
    new_c[30] = cb[34]
    new_c[31] = cb[31] # D center piece
    new_c[32] = cb[28]
    new_c[33] = cb[35]
    new_c[34] = cb[32]
    new_c[35] = cb[29]
    new_c[42] = cb[51]
    new_c[43] = cb[52]
    new_c[44] = cb[53]
    new_c[51] = cb[15]
    new_c[52] = cb[16]
    new_c[53] = cb[17]

    return new_c

def D2(cb):
    """
    90 degree counterclockwise turn of the D face
    """
    new_c = cb.copy()

    new_c[15] = cb[51]
    new_c[16] = cb[52]
    new_c[17] = cb[53]
    new_c[24] = cb[15]
    new_c[25] = cb[16]
    new_c[26] = cb[17]
    new_c[27] = cb[29]
    new_c[28] = cb[32]
    new_c[29] = cb[35]
    new_c[30] = cb[28]
    new_c[31] = cb[31] # D center piece
    new_c[32] = cb[34]
    new_c[33] = cb[27]
    new_c[34] = cb[30]
    new_c[35] = cb[33]
    new_c[42] = cb[24]
    new_c[43] = cb[25]
    new_c[44] = cb[26]
    new_c[51] = cb[42]
    new_c[52] = cb[43]
    new_c[53] = cb[44]

    return new_c

def D3(cb):
    """
    180 degree turn of the D face
    """
    new_c = cb.copy()

    new_c[15] = cb[42]
    new_c[16] = cb[43]
    new_c[17] = cb[44]
    new_c[24] = cb[51]
    new_c[25] = cb[52]
    new_c[26] = cb[53]
    new_c[27] = cb[35]
    new_c[28] = cb[34]
    new_c[29] = cb[33]
    new_c[30] = cb[32]
    new_c[31] = cb[31] # D center piece
    new_c[32] = cb[30]
    new_c[33] = cb[29]
    new_c[34] = cb[28]
    new_c[35] = cb[27]
    new_c[42] = cb[15]
    new_c[43] = cb[16]
    new_c[44] = cb[17]
    new_c[51] = cb[24]
    new_c[52] = cb[25]
    new_c[53] = cb[26]

    return new_c

def L1(cb):
    """
    90 degree clockwise turn of the L face
    """
    new_c = cb.copy()

    new_c[0] = cb[53]
    new_c[3] = cb[50]
    new_c[6] = cb[47]
    new_c[18] = cb[0]
    new_c[21] = cb[3]
    new_c[24] = cb[6]
    new_c[27] = cb[18]
    new_c[30] = cb[21]
    new_c[33] = cb[24]
    new_c[36] = cb[42]
    new_c[37] = cb[39]
    new_c[38] = cb[36]
    new_c[39] = cb[43]
    new_c[40] = cb[40] # L center piece
    new_c[41] = cb[37]
    new_c[42] = cb[44]
    new_c[43] = cb[41]
    new_c[44] = cb[38]
    new_c[47] = cb[33]
    new_c[50] = cb[30]
    new_c[53] = cb[27]

    return new_c

def L2(cb):
    """
    90 degree counterclockwise turn of the L face
    """
    new_c = cb.copy()

    new_c[0] = cb[18]
    new_c[3] = cb[21]
    new_c[6] = cb[24]
    new_c[18] = cb[27]
    new_c[21] = cb[30]
    new_c[24] = cb[33]
    new_c[27] = cb[53]
    new_c[30] = cb[50]
    new_c[33] = cb[47]
    new_c[36] = cb[38]
    new_c[37] = cb[41]
    new_c[38] = cb[44]
    new_c[39] = cb[37]
    new_c[40] = cb[40] # L center piece
    new_c[41] = cb[43]
    new_c[42] = cb[36]
    new_c[43] = cb[39]
    new_c[44] = cb[42]
    new_c[47] = cb[6]
    new_c[50] = cb[3]
    new_c[53] = cb[0]

    return new_c

def L3(cb):
    """
    180 degree turn of the L face
    """
    new_c = cb.copy()

    new_c[0] = cb[27]
    new_c[3] = cb[30]
    new_c[6] = cb[33]
    new_c[18] = cb[53]
    new_c[21] = cb[50]
    new_c[24] = cb[47]
    new_c[27] = cb[0]
    new_c[30] = cb[3]
    new_c[33] = cb[6]
    new_c[36] = cb[44]
    new_c[37] = cb[43]
    new_c[38] = cb[42]
    new_c[39] = cb[41]
    new_c[40] = cb[40] # L center piece
    new_c[41] = cb[39]
    new_c[42] = cb[38]
    new_c[43] = cb[37]
    new_c[44] = cb[36]
    new_c[47] = cb[24]
    new_c[50] = cb[21]
    new_c[53] = cb[18]

    return new_c

def B1(cb):
    """
    90 degree clockwise turn of the B face
    """
    new_c = cb.copy()

    new_c[0] = cb[11]
    new_c[1] = cb[14]
    new_c[2] = cb[17]
    new_c[11] = cb[35]
    new_c[14] = cb[34]
    new_c[17] = cb[33]
    new_c[33] = cb[36]
    new_c[34] = cb[39]
    new_c[35] = cb[42]
    new_c[36] = cb[2]
    new_c[39] = cb[1]
    new_c[42] = cb[0]
    new_c[45] = cb[51]
    new_c[46] = cb[48]
    new_c[47] = cb[45]
    new_c[48] = cb[52]
    new_c[49] = cb[49] # B center piece
    new_c[50] = cb[46]
    new_c[51] = cb[53]
    new_c[52] = cb[50]
    new_c[53] = cb[47]

    return new_c

def B2(cb):
    """
    90 degree counterclockwise turn of the B face
    """
    new_c = cb.copy()

    new_c[0] = cb[42]
    new_c[1] = cb[39]
    new_c[2] = cb[36]
    new_c[11] = cb[0]
    new_c[14] = cb[1]
    new_c[17] = cb[2]
    new_c[33] = cb[17]
    new_c[34] = cb[14]
    new_c[35] = cb[11]
    new_c[36] = cb[33]
    new_c[39] = cb[34]
    new_c[42] = cb[35]
    new_c[45] = cb[47]
    new_c[46] = cb[50]
    new_c[47] = cb[53]
    new_c[48] = cb[46]
    new_c[49] = cb[49] # B center piece
    new_c[50] = cb[52]
    new_c[51] = cb[45]
    new_c[52] = cb[48]
    new_c[53] = cb[51]

    return new_c

def B3(cb):
    """
    180 degree turn of the B face
    """
    new_c = cb.copy()

    new_c[0] = cb[35]
    new_c[1] = cb[34]
    new_c[2] = cb[33]
    new_c[11] = cb[42]
    new_c[14] = cb[39]
    new_c[17] = cb[36]
    new_c[33] = cb[2]
    new_c[34] = cb[1]
    new_c[35] = cb[0]
    new_c[36] = cb[17]
    new_c[39] = cb[14]
    new_c[42] = cb[11]
    new_c[45] = cb[53]
    new_c[46] = cb[52]
    new_c[47] = cb[51]
    new_c[48] = cb[50]
    new_c[49] = cb[49] # B center piece
    new_c[50] = cb[48]
    new_c[51] = cb[47]
    new_c[52] = cb[46]
    new_c[53] = cb[45]

    return new_c

def check_current_cube(cb):
    """
    Check if
    """
    # try:
    #     assert(type(cube_obj) == Cube)
    # except AssertionError:
    #     print("input is not Class Cube, is type %s" % type(cube_obj))

    # cb = cube_obj.cb
    try:
        assert(type(cb) == list)
    except AssertionError:
        print("current cube config must be of type list, is type %s\n"
              % type(cb))

    con_len = len(cb)
    try:
        assert(con_len == 54)
    except AssertionError:
        print("invalid configuration; must have length of 54\n"
              + "currently is length " + str(con_len) + "\n")

    count = [0] * 6  # number of faces
    for i in range(con_len):
        if cb[i] == Cl.U:
            count[Cl.U] += 1

        elif cb[i] == Cl.R:
            count[Cl.R] += 1

        elif cb[i] == Cl.F:
            count[Cl.F] += 1

        elif cb[i] == Cl.D:
            count[Cl.D] += 1

        elif cb[i] == Cl.L:
            count[Cl.L] += 1

        elif cb[i] == Cl.B:
            count[Cl.B] += 1

    if all(elem == 9 for elem in count):  # 9 facelets per face
        return True
    return False

def execute_move(cube_obj, move_list):
    """
    Executes the specified move on the cube cube_obj.
    NOTE: Python does NOT have switch-case functionality; official docs suggest
    using if-elif-...-else but this feels inelegant.
    """
    moves = {
        "U1": U1,
        "U2": U2,
        "U3": U3,
        "R1": R1,
        "R2": R2,
        "R3": R3,
        "F1": F1,
        "F2": F2,
        "F3": F3,
        "D1": D1,
        "D2": D2,
        "D3": D3,
        "L1": L1,
        "L2": L2,
        "L3": L3,
        "B1": B1,
        "B2": B2,
        "B3": B3
    }

    for move in move_list.split():
        if move in moves:
            print("move: %s" % move)
            move_str = moves.get(move, "Invalid move specification.\n")
            move_func = moves[move]
            new_c = move_func(cube_obj.cb)

            try:
                assert(check_current_cube(new_c))
                cube_obj.update_state(new_c)
                print(cube_obj)
                cube_obj.add_move(move)
            except AssertionError:
                print("Move failed!!! %s\n" % move_str)

        else:
            print("invalid move: %s" % move)
            break;

    print("no more moves!")

# # quick unit test
# config1 = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube1 = Cube(config1)
# print(cube1)
# check_current_cube(cube1.cb)
# execute_move(cube1, "U1 U2 F1 F2 D1 D2 L1 L2 B1 B2 R1 R2")
# execute_move(cube1, "U3 U3 F3 F3 D3 D3 L3 L3 B3 B3 R3 R3")