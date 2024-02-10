class SolveCubeMethods:
    @staticmethod
    def rotate_face_clockwise(cube, face):
        # Rotate the specified face clockwise
        cube[face] = [list(row) for row in zip(*cube[face][::-1])]

    @staticmethod
    def rotate_face_counterclockwise(cube, face):
        # Rotate the specified face counterclockwise
        cube[face] = [list(row) for row in zip(*cube[face])][::-1]

    @staticmethod
    def rotate_row_clockwise(cube, face, row_index):
        # Rotate the specified row of the specified face clockwise
        cube[face][row_index] = [cube[face][i][row_index] for i in range(2, -1, -1)]

    @staticmethod
    def rotate_row_counterclockwise(cube, face, row_index):
        # Rotate the specified row of the specified face counterclockwise
        cube[face][row_index] = [cube[face][i][row_index] for i in range(3)]

    @staticmethod
    def rotate_column_clockwise(cube, face, col_index):
        # Rotate the specified column of the specified face clockwise
        col = [cube[face][i][col_index] for i in range(2, -1, -1)]
        for i in range(3):
            cube[face][i][col_index] = col[i]

    @staticmethod
    def rotate_column_counterclockwise(cube, face, col_index):
        # Rotate the specified column of the specified face counterclockwise
        col = [cube[face][i][col_index] for i in range(3)]
        for i in range(3):
            cube[face][i][col_index] = col[(i + 1) % 3]

    @staticmethod
    def rotate_cube_clockwise(cube, axis):
        print(cube)
        # Rotate the entire cube clockwise around the specified axis (x, y, or z)
        if axis == 'x':
            # Rotate the entire cube around the x-axis (up and down)
            SolveCubeMethods.rotate_face_clockwise(cube, 'top')
            SolveCubeMethods.rotate_face_counterclockwise(cube, 'bottom')
            temp = cube['front']
            cube['front'] = cube['left']
            cube['left'] = cube['back']
            cube['back'] = cube['right']
            cube['right'] = temp
        elif axis == 'y':
            # Rotate the entire cube around the y-axis (left and right)
            SolveCubeMethods.rotate_face_clockwise(cube, 'front')
            SolveCubeMethods.rotate_face_counterclockwise(cube, 'back')
            temp = [row[0] for row in cube['top']]
            for i in range(3):
                cube['top'][i][0] = cube['left'][i][0]
                cube['left'][i][0] = cube['bottom'][i][0]
                cube['bottom'][i][0] = cube['right'][i][0]
                cube['right'][i][0] = temp[i]
        elif axis == 'z':
            # Rotate the entire cube around the z-axis (clockwise and counterclockwise)
            SolveCubeMethods.rotate_face_clockwise(cube, 'left')
            SolveCubeMethods.rotate_face_counterclockwise(cube, 'right')
            temp = [row[::-1] for row in cube['top']]
            cube['top'] = [list(row) for row in zip(*temp)]
            temp = [row[::-1] for row in cube['bottom']]
            cube['bottom'] = [list(row) for row in zip(*temp)]
        print(cube)

    @staticmethod
    def rotate_cube_counterclockwise(cube, axis):
        # Rotate the entire cube counterclockwise around the specified axis (x, y, or z)
        for _ in range(3):
            SolveCubeMethods.rotate_cube_clockwise(cube, axis)
