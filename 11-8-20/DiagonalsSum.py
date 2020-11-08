def sum_diagonals(matrix):
    if len(matrix[0]) == 0:
        return 0
    sum = 0
    pointer_forward = -1
    pointer_back_x = -1
    pointer_back_y = len(matrix)
    for i in range(len(matrix)):
        pointer_forward += 1
        pointer_back_x += 1
        pointer_back_y -= 1
        for x in range(len(matrix)):
            if i == pointer_forward and x == pointer_forward:
                sum += matrix[i][x]
            if i == pointer_back_x and x == pointer_back_y:
                sum += matrix[i][x]
    return sum
    