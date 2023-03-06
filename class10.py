count = int(input("how many numbers do you want to add? "))

numbers = []


for i in range(count):
    num = int(input("Give me a number "))
    numbers.append(num)



# def sum_numbers(list_num):
#     result = 0
#     for x in list_num:
#         result += x
#     return result

def sum_numbers(list_num):

    result_x = sum(list_num)
    return result_x



result_x = sum_numbers(numbers)

print(result_x)




# i am coming  home

# m cmng hme