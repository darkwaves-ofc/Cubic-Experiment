from solve import SolveCubeMethods
class RubiksCube:
    def __init__(self):
        # Define the valid colors for the Rubik's Cube
        self.valid_colors = {'W', 'O', 'G', 'R', 'B', 'Y'}
        self.sides = ['front', 'back', 'top', 'bottom', 'left', 'right']
        self.positions = ['top-left', 'top-center', 'top-right',
                          'center-left', 'center-center', 'center-right',
                          'bottom-left', 'bottom-center', 'bottom-right']
        # Initialize an empty cube
        self.current_cube = {side: {position: None for position in self.positions} for side in self.sides}

    def input_cube(self):
        # Input the current state of the Rubik's Cube
        print("Input the current state of the Rubik's Cube side by side and color by color.")
        print("Use the following color codes: W (White), O (Orange), G (Green), R (Red), B (Blue), Y (Yellow)")

        for side in self.sides:
            print(f'Enter colors for {side}:')
            for position in range(9):
                while True:
                    color_input = input(f"Enter color for {self.positions[position]}: ").strip().upper()
                    if not color_input:
                        print("Input cannot be empty. Please provide a color.")
                    elif color_input in self.valid_colors:
                        self.current_cube[side][position] = color_input
                        break
                    else:
                        print("Invalid color! Please enter a valid color (W, O, G, R, B, Y).")

    def solve_cube(self):
        SolveCubeMethods.rotate_cube_clockwise(self.current_cube,"x")

        # Solve the Rubik's Cube
        pass  # Placeholder for solving logic

    def output_solution(self):
        # Output the solution of the solved cube
        pass  # Placeholder for output logic

def main():
    # Create a Rubik's Cube instance
    cube = RubiksCube()

    # Input the current state of the Rubik's Cube
    cube.input_cube()

    # Solve the Rubik's Cube
    cube.solve_cube()

    # Output the solution
    cube.output_solution()

    print(cube.current_cube)

if __name__ == "__main__":
    main()
