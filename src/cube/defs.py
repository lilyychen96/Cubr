from facelet import Facelet as Fc, Color as Cl


# Corner to cube piece positions
cornerFc = set([
            tuple(sorted([Fc.U9, Fc.R1, Fc.F3])),
            tuple(sorted([Fc.U7, Fc.F1, Fc.L3])),
            tuple(sorted([Fc.U1, Fc.L1, Fc.B3])),
            tuple(sorted([Fc.U3, Fc.B1, Fc.R3])),
            tuple(sorted([Fc.D3, Fc.F9, Fc.R7])),
            tuple(sorted([Fc.D1, Fc.L9, Fc.F7])),
            tuple(sorted([Fc.D7, Fc.B9, Fc.L7])),
            tuple(sorted([Fc.D9, Fc.R9, Fc.B7]))
           ])

# Edge to cube piece positions
edgeFc = set([
            tuple(sorted([Fc.U6, Fc.R2])),
            tuple(sorted([Fc.U8, Fc.F2])),
            tuple(sorted([Fc.U4, Fc.L2])),
            tuple(sorted([Fc.U2, Fc.B2])),
            tuple(sorted([Fc.D6, Fc.R8])),
            tuple(sorted([Fc.D2, Fc.F8])),
            tuple(sorted([Fc.D4, Fc.L8])),
            tuple(sorted([Fc.D8, Fc.B8])),
            tuple(sorted([Fc.F6, Fc.R4])),
            tuple(sorted([Fc.F4, Fc.L6])),
            tuple(sorted([Fc.B4, Fc.R6])),
            tuple(sorted([Fc.B6, Fc.L4]))
         ])

# Corner positions to color
cornerCl = set([
            tuple(sorted([Cl.U, Cl.R, Cl.F])),
            tuple(sorted([Cl.U, Cl.F, Cl.L])),
            tuple(sorted([Cl.U, Cl.L, Cl.B])),
            tuple(sorted([Cl.U, Cl.B, Cl.R])),
            tuple(sorted([Cl.D, Cl.F, Cl.R])),
            tuple(sorted([Cl.D, Cl.L, Cl.F])),
            tuple(sorted([Cl.D, Cl.B, Cl.L])),
            tuple(sorted([Cl.D, Cl.R, Cl.B]))
           ])

# Edge positions to color
edgeCl = set([
            tuple(sorted([Cl.U, Cl.R])),
            tuple(sorted([Cl.U, Cl.F])),
            tuple(sorted([Cl.U, Cl.L])),
            tuple(sorted([Cl.U, Cl.B])),
            tuple(sorted([Cl.D, Cl.R])),
            tuple(sorted([Cl.D, Cl.F])),
            tuple(sorted([Cl.D, Cl.L])),
            tuple(sorted([Cl.D, Cl.B])),
            tuple(sorted([Cl.F, Cl.R])),
            tuple(sorted([Cl.F, Cl.L])),
            tuple(sorted([Cl.B, Cl.R])),
            tuple(sorted([Cl.B, Cl.L]))
         ])
