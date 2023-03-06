def calc(num1, num2):
    print(num1 + num2)




calc(2, 2)
calc(7, 9)
calc(9,70)


numbs =[]
for i in range(2):

    user_input = int(input("give me a number"))

    numbs.append(user_input)

def calc_subtraction(num1, num2):
    print(num1 - num2)

calc_subtraction(numbs[0], numbs[1])

def calc_division(num1, num2):
    print(num1/num2)

calc_division(numbs[0], numbs[1])


def calc_multiply(num1, num2):
    print(num1 * num2)

calc_multiply(numbs[0], numbs[1])