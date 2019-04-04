# Based on hkoceimba's cube implementation
# https://github.com/hkociemba/RubiksCube-TwophaseSolver/blob/master/enums.py

from enum import IntEnum


class Facelet(IntEnum):
    """
    The names of the facelet pieces positions of the cube:
        U(p), R(ight), F(ront), D(own), L(eft), B(ack)
                 |............|
                 |.U1..U2..U3.|
                 |............|
                 |.U4..U5..U6.|
                 |............|
                 |.U7..U8..U9.|
    |............|............|............|............|
    |.L1..L2..L3.|.F1..F2..F3.|.R1..R2..R3.|.B1..B2..B3.|
    |............|............|............|............|
    |.L4..L5..L6.|.F4..F5..F6.|.R4..R5..R6.|.B4..B5..B6.|
    |............|............|............|............|
    |.L7..L8..L9.|.F7..F8..F9.|.R7..R8..R9.|.B7..B8..B9.|
    |............|............|............|............|
                 |.D1..D2..D3.|
                 |............|
                 |.D4..D5..D6.|
                 |............|
                 |.D7..D8..D9.|
                 |............|
    The order of the pieces of the cube are as follows:
        U1, U2, U3, U4, U5, U6, U7, U8, U9,
        R1, R2, R3, R4, R5, R6, R7, R8, R9,
        F1, F2, F3, F4, F5, F6, F7, F8, F9,
        D1, D2, D3, D4, D5, D6, D7, D8, D9,
        L1, L2, L3, L4, L5, L6, L7, L8, L9,
        B1, B2, B3, B4, B5, B6, B7, B8, B9
    """
    U1 = 0
    U2 = 1
    U3 = 2
    U4 = 3
    U5 = 4   # U center piece
    U6 = 5
    U7 = 6
    U8 = 7
    U9 = 8
    R1 = 9
    R2 = 10
    R3 = 11
    R4 = 12
    R5 = 13  # R center piece
    R6 = 14
    R7 = 15
    R8 = 16
    R9 = 17
    F1 = 18
    F2 = 19
    F3 = 20
    F4 = 21
    F5 = 22  # F center piece
    F6 = 23
    F7 = 24
    F8 = 25
    F9 = 26
    D1 = 27
    D2 = 28
    D3 = 29
    D4 = 30
    D5 = 31  # D center piece
    D6 = 32
    D7 = 33
    D8 = 34
    D9 = 35
    L1 = 36
    L2 = 37
    L3 = 38
    L4 = 39
    L5 = 40  # L center piece
    L6 = 41
    L7 = 42
    L8 = 43
    L9 = 44
    B1 = 45
    B2 = 46
    B3 = 47
    B4 = 48
    B5 = 49  # B center piece
    B6 = 50
    B7 = 51
    B8 = 52
    B9 = 53

class Color(IntEnum):
    """
    The six colors of the cube faces, denoted by position relative to the
    front face.
    """
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5

class Corner(IntEnum):
    """
    The names of the corner positions of the cube.
    """
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7

class Edge(IntEnum):
    """
    The names of the edge positions of the cube.
    """
    UR = 8
    UF = 9
    UL = 10
    UB = 11
    DR = 12
    DF = 13
    DL = 14
    DB = 15
    FR = 16
    FL = 17
    BR = 18
    BL = 19

class Move(IntEnum):
    """
    The eighteen types of cube rotation moves. 1 denotes the ordinary rotation,
    2 denotes the reverse rotation, and 3 denotes a 180 degree rotation.
    Note that there are no center rotation moves as they can be executed as two
    moves of the adjacent rows or columns.
    """
    U1 = 0
    U2 = 1
    U3 = 2
    R1 = 3
    R2 = 4
    R3 = 5
    F1 = 6
    F2 = 7
    F3 = 8
    D1 = 9
    D2 = 10
    D3 = 11
    L1 = 12
    L2 = 13
    L3 = 14
    B1 = 15
    B2 = 16
    B3 = 17
