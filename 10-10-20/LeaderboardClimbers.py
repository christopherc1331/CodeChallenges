def leaderboard_sort(leaderboard, changes):
    cache = {leaderboard[i]:i for i in range(len(leaderboard))}
    print(cache)
    for i in changes:
        name = i.split()[0]
        move_dir = i.split()[1][0]
        move_amt = i.split()[1][1]

        
        if move_dir == "+":
            cache[name] -= int(move_amt)
        else:
            cache[name] += int(move_amt)

    return_list = [0] * len(leaderboard)
    for i in cache.items():

        name = i[0]
        pos = i[1] 
        
        print("name", name)
        print("pos", pos)
        
        return_list[pos] = name
        
    return return_list