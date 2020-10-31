def parts_sums(ls):
    new_arr = [0]

    if not ls:
        return new_arr

    for i in range(len(ls)):
        new_arr.insert(0, sum((ls[(-i)-1:-1])) + ls[-1])

    return new_arr
