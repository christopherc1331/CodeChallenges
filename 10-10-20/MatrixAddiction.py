def matrix_addition(a, b):
    # your code here

    for x in range(len(a)):
        for y in range(len(a)):

            a[x][y] += b[x][y]

    return a
