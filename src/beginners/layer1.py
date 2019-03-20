# front edges
# front corners

def front_edges(cube_state):
    """
    Outputs the moves list for solving the front face edge pieces according to
    the initial cube state. Must check if the pieces at 19, 21, 23, and 25
    match piece 22 (F center piece).
    NOTE: cube_state would be the c list of the Cube object
        example: cb = cube.Cube(config); cube_state = cb.c
    """
    # TODO: type checking and such
    # WAIT: need to identify cubie pieces so solving is much easier...

    try:
        assert(cube_state[22] == Cl.F)
    except AssertionError:
        # should never reach here lol
        print("Initial cube state is not correct (?)")

    if cube_state[19] == Cl.F:
        pass
    if cube_state[21] == Cl.F:
        pass
    if cube_state[23] == Cl.F:
        pass
    if cube_state[25] == Cl.F:
        pass
