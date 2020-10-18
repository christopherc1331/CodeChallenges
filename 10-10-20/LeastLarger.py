def least_larger(a, i):
    # your code here
    larger_than_given = {}
    larger_vals = []

    for v in range(len(a)):
        if a[v] > a[i]:
            larger_than_given[a[v]] = v
            larger_vals.append(a[v])

    if len(larger_vals) == 0:
        return -1
    elif larger_than_given[min(larger_vals)] > len(a):
        return -1
    else:
        return larger_than_given[min(larger_vals)]
