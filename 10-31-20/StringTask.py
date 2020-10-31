def string_task(s):

    vowels = ["a", "e", "i", "o", "u", "y"]

    new_str = ""

    for char in s:
        if char.lower() not in vowels:
            new_str += "." + char.lower()

    return new_str
