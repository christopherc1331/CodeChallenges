def valid_parentheses(string):

    open = 0

    for char in string:
        if open < 0:
            return False
        else:
            if char == "(":
                open += 1
            elif char == ")":
                open -= 1

    return True if open == 0 else False
