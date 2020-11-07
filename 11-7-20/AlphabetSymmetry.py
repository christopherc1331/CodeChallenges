import string


def solve(arr):
    alpha = string.ascii_lowercase

    new_arr = [i.lower() for i in arr]

    count_arr = [0] * len(new_arr)

    for i in range(len(new_arr)):
        count = 0
        for x in range(len(new_arr[i])):
            if (x in range(len(alpha))) and (new_arr[i][x] == alpha[x]):
                count += 1
        count_arr[i] = count

    return count_arr
