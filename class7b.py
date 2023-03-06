user_input = int(input("Give me a number: "))

# if user_put is < 0 exit , if it is greater than 100 exit

# if user_input < 0 or user_input > 100:
#     print("Give me a positive number , you can input a negative")
#     exit(0)
while user_input > 0 and user_input < 101:
    print("good user input")
    break

if user_input > 0  and user_input < 101:
    print("You have inputted a correct number now lets start looping")
    for i in range(user_input):

        print('#' * user_input)
    exit(0)



print("Error you have used this program wrongly")























#> 6
#
##
###
####
#####
######