def remove_duplicate_words(s):
    cache = {}

    new_str = ""

    for i in s.split():
        if i not in cache:
            cache[i] = i
            new_str += i + " "

    return new_str.strip()
