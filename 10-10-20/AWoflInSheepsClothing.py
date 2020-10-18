def warn_the_sheep(queue):

    for index, thing in enumerate(queue[::-1]):
        if thing == "wolf" and index == 0:
            return "Pls go away and stop eating my sheep"
        elif thing == "wolf":
            return f"Oi! Sheep number {index}! You are about to be eaten by a wolf!"
