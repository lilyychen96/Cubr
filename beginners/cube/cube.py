from facelet import Color as Cl, Corner as Cn, Edge as Ed
from defs import cornerFc, edgeFc, cornerCl, edgeCl
import string

class Cube:
    def __init__(self, config):
        self.c = []

        self.c += [Cl.U] * 9
        self.c += [Cl.R] * 9
        self.c += [Cl.F] * 9
        self.c += [Cl.D] * 9
        self.c += [Cl.L] * 9
        self.c += [Cl.B] * 9
        self.config = config

    def __str__(self):
        return self.cube_to_str()

    def verify_config(self):
        """
        Verifies a string representation of the given cube configuration for
        correct number of facelets for each color/face and converts the string
        representation into a list.
        """
        try:
            assert(type(self.config) == str)
        except AssertionError:
            print("input configuration must be of type string, is type %s"
                  % type(self.config))

        if len(self.config) == 0:
            return False

        config = self.config
        config_len = len(config)

        # either use try/except or just return False?
        try:
            assert(config_len == 54)

            count = [0] * 6  # 6 = number of faces

            for i in range(config_len):
                if config[i] not in "URFDLB":
                    print("invalid character: %s" % config[i])
                    return False

                if config[i].islower():
                    config[i] = config[i].upper()

                if config[i] == 'U':
                    self.c[i] = Cl.U
                    count[Cl.U] += 1

                elif config[i] == 'R':
                    self.c[i] = Cl.R
                    count[Cl.R] += 1

                elif config[i] == 'F':
                    self.c[i] = Cl.F
                    count[Cl.F] += 1

                elif config[i] == 'D':
                    self.c[i] = Cl.D
                    count[Cl.D] += 1

                elif config[i] == 'L':
                    self.c[i] = Cl.L
                    count[Cl.L] += 1

                elif config[i] == 'B':
                    self.c[i] = Cl.B
                    count[Cl.B] += 1

            if all(c == 9 for c in count):  # 9 facelets per face
                return True
            else:
                return False

        except AssertionError:
            print("invalid configuration string; must have length of 54\n"
                  + "currently is length " + str(len(config)))

    def reformat_config(self):
        """
        Reformats the configuration such that printing is easier.
        NOTE: This does not change the cube state.

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
                           |.............|
                 """
                 % tuple(self.reformat_config())
                )

        return s


# # TODO: restructure
# # quick unit tests
# config1 = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
# cube1 = Cube(config1)
# print(cube1)

# config2 = "FUUBUUDRBLBBBRLBLBFDDBFRUURFFDFDDFDUDDRLLLRRLLRLFBURFU"
# cube2 = Cube(config2)
# print(cube2)
