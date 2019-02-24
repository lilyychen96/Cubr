from cube import Cube as Cb, Color as Cl

# Corner to cube piece positions
cornerCb = [[Cb.U9, Cb.R1, Cb.F3],
            [Cb.U7, Cb.F1, Cb.L3],
            [Cb.U1, Cb.L1, Cb.B3],
            [Cb.U3, Cb.B1, Cb.R7],
            [Cb.D3, Cb.F9, Cb.R3],
            [Cb.D1, Cb.L9, Cb.F7],
            [Cb.D7, Cb.B9, Cb.L7],
            [Cb.D9, Cb.R9, Cb.B7],
            ]

# Edge to cube piece positions
edgeCb = [[Cb.U6, Cb.R4],
          [Cb.U8, Cb.F2],
          [Cb.U4, Cb.L2],
          [Cb.U2, Cb.B2],
          [Cb.D6, Cb.R6],
          [Cb.D2, Cb.F8],
          [Cb.D4, Cb.L8],
          [Cb.D8, Cb.B8],
          [Cb.F6, Cb.R2],
          [Cb.F4, Cb.L6],
          [Cb.B4, Cb.R8],
          [Cb.B6, Cb.L4],
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
