# Cubr
## Cubr: Cube Puzzle Solver (18-500 CMU ECE Capstone, Spring 2019)
Project website: https://course.ece.cmu.edu/~ece500/projects/s19-teamd6/

The Rubik’s cube is a 3x3x3 3D combination puzzle that can be solved algorithmically. Cubr is a mechanical puzzle cube solver that can solve the cube with the intention of speed and for tutorial purposes. The solver uses computer vision to detect and examine the cube state, and internally store the 3D mapping of the puzzle cube before executing physical solving by turning the faces with 6 bipolar stepper motors. The cube state can be passed into our own implementation of the Beginner’s Method solving algorithms to find a solution string. Cubr can also utilize Kociemba's highly efficient Two-Phase algorithm to find a solution of 20 or less moves for any given cube state. Our hardware module interfaces the resulting solution string through an Arduino to execute the solution string of rotation moves to physically solve the puzzle or make patterns.

# The Team
- JT Aceron
  - https://www.linkedin.com/in/jtaceron
  - https://jaceron.myportfolio.com
  - Firmware, Hardware, + Circuit Design
- Lily Chen
  - https://lilyychen96.github.io/
  - Software Design, Circuit Design and Assembly, + CAD
- Sam Fazel-Sarjui
  - https://www.linkedin.com/in/sam-fazel-sarjui-2b7b19127/
  - https://sfazelsa.github.io/
  - Computer Vision + UI, 3D Printing and Assembly, + Firmware

# Software Dependencies
- Python 3.4+
- Numpy
- OpenCV
- pySerial

# Execution
- To use beginners method, execute %python3 solver.py --solver beginners
- To use twoPhase method, clone twoPhase repo into twoPhase directory, then execute %python3 solver.py
  - https://github.com/hkociemba/RubiksCube-TwophaseSolver
