from facelet import Facelet as Fc, Color as Cl

# Corner to cube piece positions
cornerFc = [[Fc.U9, Fc.R1, Fc.F3],
            [Fc.U7, Fc.F1, Fc.L3],
            [Fc.U1, Fc.L1, Fc.B3],
            [Fc.U3, Fc.B1, Fc.R3],
            [Fc.D3, Fc.F9, Fc.R7],
            [Fc.D1, Fc.L9, Fc.F7],
            [Fc.D7, Fc.B9, Fc.L7],
            [Fc.D9, Fc.R9, Fc.B7],
            ]

# Edge to cube piece positions
edgeFc = [[Fc.U6, Fc.R2],
          [Fc.U8, Fc.F2],
          [Fc.U4, Fc.L2],
          [Fc.U2, Fc.B2],
          [Fc.D6, Fc.R8],
          [Fc.D2, Fc.F8],
          [Fc.D4, Fc.L8],
          [Fc.D8, Fc.B8],
          [Fc.F6, Fc.R4],
          [Fc.F4, Fc.L6],
          [Fc.B4, Fc.R6],
          [Fc.B6, Fc.L4],
         ]

# Corner positions to color
cornerCl = [[Cl.U, Cl.R, Cl.F],
            [Cl.U, Cl.F, Cl.L],
            [Cl.U, Cl.L, Cl.B],
            [Cl.U, Cl.B, Cl.R],
            [Cl.D, Cl.F, Cl.R],
            [Cl.D, Cl.L, Cl.F],
            [Cl.D, Cl.B, Cl.L],
            [Cl.D, Cl.R, Cl.B],
            ]

# Edge positions to color
edgeCl = [[Cl.U, Cl.R],
          [Cl.U, Cl.F],
          [Cl.U, Cl.L],
          [Cl.U, Cl.B],
          [Cl.D, Cl.R],
          [Cl.D, Cl.F],
          [Cl.D, Cl.L],
          [Cl.D, Cl.B],
          [Cl.F, Cl.R],
          [Cl.F, Cl.L],
          [Cl.B, Cl.R],
          [Cl.B, Cl.L],
         ]
