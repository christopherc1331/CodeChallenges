def say_me_operations(string_numbers):

    def find_operator(num1, num2, num3):
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)

        if num1 + num2 == num3:
            return "addition"
        elif num1 - num2 == num3:
            return "subtraction"
        elif num1 * num2 == num3:
            return "multiplication"
        else:
            return "division"

    return_string = ""

    new_list = string_numbers.split()

    for i in range(len(new_list)):
        if i + 2 < len(new_list):
            if len(return_string) > 0:
                return_string += ", "

            return_string += (find_operator(new_list[i],
                                            new_list[i+1], new_list[i+2]))

    return return_string
