def calc_div(num1, num2):
    return num1 / num2


def calc_add(num1, num2):
    return num1 + num2


def calc_sub(num1, num2):
    return num1 - num2



a = 2
b = 3


add_result = calc_add(a, b)

sub_result = calc_sub(a, b)


div_result = calc_div(add_result, sub_result)

print(div_result) 