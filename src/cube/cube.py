from facelet import Color as Cl, Corner as Cn, Edge as Ed
from defs import complete, cornerFc, edgeFc, cornerCl, edgeCl

# @TODO: consolidate "unit tests" to different file
# @TODO: eliminate print statements
# @TODO: figure out actual error handling/logging...

class Cube:
    def __init__(self, config, test=False):
        self.cb = []
        self.cb += [Cl.U] * 9
        self.cb += [Cl.R] * 9
        self.cb += [Cl.F] * 9
        self.cb += [Cl.D] * 9
        self.cb += [Cl.L] * 9
        self.cb += [Cl.B] * 9

        self.cubies = dict()

        # input configuration, should not change after assignment
        self.init_state = config
        self.config = config # should change after each move

        self.soln = "" # solution string output
        self.solved = False

        self.test = test

    def __str__(self):
        """
        Calls cube_to_str() to get cube configuration string representation.
        """
        return self.cube_to_str()

    def str_to_cube(self):
        """
        Converts string representation of configuration to list representation.
        Returns the list representation of the cube configuration and cubie piece
        count for each face (should be 9 each). If no list representation is given
        for writing, then start from an empty list.
        """
        try:
            assert(type(self.config) == str)
        except AssertionError:
            print("input configuration must be of type string, is type %s\n"
                  % type(self.config))

        cb = self.cb.copy()
        config = self.config
        con_len = len(config)
        try:
            assert(con_len == 54)
        except AssertionError:
            print("invalid configuration string; must have length of 54\n"
                  + "currently is length " + str(con_len) + "\n")

        count = [0] * 6  # number of faces
        for i in range(con_len):
            if config[i] not in "URFDLB":
                print("invalid character: %s\n" % config[i])
                return False

            if config[i].islower():
                config[i] = config[i].upper()

            if config[i] == 'U':
                cb[i] = Cl.U
                count[Cl.U] += 1

            elif config[i] == 'R':
                cb[i] = Cl.R
                count[Cl.R] += 1

            elif config[i] == 'F':
                cb[i] = Cl.F
                count[Cl.F] += 1

            elif config[i] == 'D':
                cb[i] = Cl.D
                count[Cl.D] += 1

            elif config[i] == 'L':
                cb[i] = Cl.L
                count[Cl.L] += 1

            elif config[i] == 'B':
                cb[i] = Cl.B
                count[Cl.B] += 1

        return (cb, count)

    def check_cubies(self, cnrs, edgs):
        """
        Validates the cube state according to the cubie pieces (8 corners and 
        12 edges).
        """
        corners = False
        edges = False

        # check for all corner cubies
        count = 0
        for k in cnrs:
            if k in cornerCl:
                count += 1

        if count == 8: # expected number of corner cubies
            corners = True

        if corners:
            # check for all edge cubies
            count = 0
            for k in edgs:
                if k in edgeCl:
                    count += 1

            if count == 12: # expected number of edge cubies
                edges = True

        return (corners, edges)

    def update_cubies(self):
        """
        Identifies cubie pieces (8 corners and 12 edges) given a valid cube
        state configuration.
        """
        cbs = dict()
        cb = self.cb

        # corner cubies
        cbs[Cn.URF] = [cb[8], cb[9], cb[20]]
        cbs[Cn.UFL] = [cb[6], cb[18], cb[38]]
        cbs[Cn.ULB] = [cb[0], cb[36], cb[47]]
        cbs[Cn.UBR] = [cb[2], cb[45], cb[11]]
        cbs[Cn.DFR] = [cb[29], cb[26], cb[15]]
        cbs[Cn.DLF] = [cb[27], cb[44], cb[24]]
        cbs[Cn.DBL] = [cb[33], cb[53], cb[42]]
        cbs[Cn.DRB] = [cb[35], cb[17], cb[51]]

        cnrs = set([
            tuple(sorted(cbs[Cn.URF])), tuple(sorted(cbs[Cn.UFL])),
            tuple(sorted(cbs[Cn.ULB])), tuple(sorted(cbs[Cn.UBR])),
            tuple(sorted(cbs[Cn.DFR])), tuple(sorted(cbs[Cn.DLF])),
            tuple(sorted(cbs[Cn.DBL])), tuple(sorted(cbs[Cn.DRB]))
        ])

        # edge cubies
        cbs[Ed.UR] = [cb[5], cb[10]]
        cbs[Ed.UF] = [cb[7], cb[19]]
        cbs[Ed.UL] = [cb[3], cb[37]]
        cbs[Ed.UB] = [cb[1], cb[46]]
        cbs[Ed.DR] = [cb[32], cb[16]]
        cbs[Ed.DF] = [cb[28], cb[25]]
        cbs[Ed.DL] = [cb[30], cb[43]]
        cbs[Ed.DB] = [cb[34], cb[52]]
        cbs[Ed.FR] = [cb[23], cb[12]]
        cbs[Ed.FL] = [cb[21], cb[41]]
        cbs[Ed.BR] = [cb[48], cb[14]]
        cbs[Ed.BL] = [cb[50], cb[39]]
        edgs = set([
            tuple(sorted(cbs[Ed.UR])), tuple(sorted(cbs[Ed.UF])),
            tuple(sorted(cbs[Ed.UL])), tuple(sorted(cbs[Ed.UB])),
            tuple(sorted(cbs[Ed.DR])), tuple(sorted(cbs[Ed.DF])),
            tuple(sorted(cbs[Ed.DL])), tuple(sorted(cbs[Ed.DB])),
            tuple(sorted(cbs[Ed.FR])), tuple(sorted(cbs[Ed.FL])),
            tuple(sorted(cbs[Ed.BR])), tuple(sorted(cbs[Ed.BL]))
        ])

        (corners, edges) = self.check_cubies(cnrs, edgs)

        try:
            assert(corners and edges)
            self.cubies = cbs.copy()

            # update config string
            new_config = ""
            for i in range(len(cb)):
                face = str(cb[i])[-1]
                new_config += face

            self.config = new_config
        except AssertionError:
            print("invalid corner and edge cubies!")

    def update_state(self, new_c):
        """
        Updates the cube state's list and cubie dict representations.
        """
        self.cb = new_c
        self.update_cubies()

    def verify_config(self):
        """
        Verifies a string representation of the given cube configuration for
        correct number of facelets for each color/face and converts the string
        representation into a list through str_to_cube().
        """
        (cb, count) = self.str_to_cube()

        if all(c == 9 for c in count):  # 9 facelets per face
            self.cb = cb
            self.update_cubies()
            return True
        
        return False

    def reformat_config(self):
        """
        Reformats the configuration for ease of printing to command line.
        NOTE: This does NOT change the cube state.

        Before:
                      |.............|
                      |..0...1...2..|
                      |.............|
                      |..3...4...5..|
                      |.............|
                      |..6...7...8..|
        |.............|.............|.............|.............|
        |.36..37..38..|.18..19..20..|..9..10..11..|.45..46..47..|
        |.............|.............|.............|.............|
        |.39..40..41..|.21..22..23..|.12..13..14..|.48..49..50..|
        |.............|.............|.............|.............|
        |.42..43..44..|.24..25..26..|.15..16..17..|.51..52..53..|
        |.............|.............|.............|.............|
                      |.27..28..29..|
                      |.............|
                      |.30..31..32..|
                      |.............|
                      |.33..34..35..|
                      |.............|

        After:
                      |.............|
                      |..0...1...2..|
                      |.............|
                      |..3...4...5..|
                      |.............|
                      |..6...7...8..|
        |.............|.............|.............|.............|
        |..9..10..11..|.12..13..14..|.15..16..17..|.18..19..20..|
        |.............|.............|.............|.............|
        |.21..22..23..|.24..25..26..|.27..28..29..|.30..31..32..|
        |.............|.............|.............|.............|
        |.33..34..35..|.36..37..38..|.39..40..41..|.42..43..44..|
        |.............|.............|.............|.............|
                      |.45..46..47..|
                      |.............|
                      |.48..49..50..|
                      |.............|
                      |.51..52..53..|
                      |.............|
        """
        if len(self.config) != 54:
            return ""

        faces = []
        for i in range(6 * 3):  # 6 faces * 3 rows
            face = self.config[i*3:(i+1)*3]
            faces.append(face)

        # rearrange
        out = faces[0] + faces[1] + faces[2]
        out += faces[12] + faces[6] + faces[3] + faces[15]
        out += faces[13] + faces[7] + faces[4] + faces[16]
        out += faces[14] + faces[8] + faces[5] + faces[17]
        out += faces[9] + faces[10] + faces[11]

        return out

    def cube_to_str(self):
        """
        Prints a string representation of the given cube configuration by
        order of character in configuration list.

                     |............|
                     |..0...1...2.|
                     |............|
                     |..3...4...5.|
                     |............|
                     |..6...7...8.|
        |............|............|............|............|
        |.36..37..38.|.18..19..20.|..9..10..11.|.45..46..47.|
        |............|............|............|............|
        |.39..40..41.|.21..22..23.|.12..13..14.|.48..49..50.|
        |............|............|............|............|
        |.42..43..44.|.24..25..26.|.15..16..17.|.51..52..53.|
        |............|............|............|............|
                     |.27..28..29.|
                     |............|
                     |.30..31..32.|
                     |............|
                     |.33..34..35.|
                     |............|
        As specified in cube state detection module (per standard cube colors):
            Yellow: 0-8 (UP)
            Green: 9-17 (RIGHT)
            Red: 18-26 (FRONT)
            White: 27-35 (DOWN)
            Blue: 36-44 (LEFT)
            Orange: 45-53 (BACK)
        """
        s = ""

        if self.verify_config():
            s = ("""
                           |.............|
                           |..%s...%s...%s..|
                           |.............|
                           |..%s...%s...%s..|
                           |.............|
                           |..%s...%s...%s..|
             |.............|.............|.............|.............|
             |..%s...%s...%s..|..%s...%s...%s..|..%s...%s...%s..|..%s...%s...%s..|
             |.............|.............|.............|.............|
             |..%s...%s...%s..|..%s...%s...%s..|..%s...%s...%s..|..%s...%s...%s..|
             |.............|.............|.............|.............|
             |..%s...%s...%s..|..%s...%s...%s..|..%s...%s...%s..|..%s...%s...%s..|
             |.............|.............|.............|.............|
                           |..%s...%s...%s..|
                           |.............|
                           |..%s...%s...%s..|
                           |.............|
                           |..%s...%s...%s..|
                           |.............|\n
                 """
                 % tuple(self.reformat_config())
                )

        return s

    def get_cb(self):
        """
        Retrieves copy of cubies from cube object
        """
        return self.cb

    def get_solved(self):
        """
        Retrives truth value of cube's solve state.
        """
        return self.solved

    def update_solved(self):
        """
        Checks if the list representation of the cube configuration is fully
        solved and updates the truth value to self.solved.
        """
        if self.get_solved() and not self.test:
            # trimming off excess ending whitespace
            self.soln = self.soln.rstrip()
            return

        if self.verify_config():
            for i in range(len(complete)):
                if self.cb[i] != complete[i]:
                    self.solved = False
                    return
            self.solved = True
            return
        
        self.solved = False

    def add_move(self, move_str):
        """
        Adds string name of move to solution list.
        """
        self.soln += move_str + " "
        self.update_solved()

        if self.get_solved():
            print("SOLVED! solution string: \n%s" % self.soln)

    def is_test(self):
        return self.test


# # TODO: restructure
# # quick unit tests
# config1 = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube1 = Cube(config1)
# print(cube1)
# cube1.verify_config()

# config2 = "FUUBUUDRBLBBBRLBLBFDDBFRUURFFDFDDFDUDDRLLLRRLLRLFBURFU"
# cube2 = Cube(config2)
# print(cube2)
# cube2.verify_config()
