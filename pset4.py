#create a tipping system where you give 15 percent tip of the total cost to your sales person

# get the data of the full names of a married couple and assign the husband's surname to the wife
# >> name= "ola olamide"
# >>> name
# 'ola olamide'
# >>> name.split(" ")
# ['ola', 'olamide']
# >>> name.split(" ")[0]
# 'ola'

#surname saga

input_husband = input("what is your full name ")

input_wife = input("what is your full name ")

new_surname = input_husband.split(" ")

wife_surname_select = input_wife.split(" ")

old_wife_surname = (wife_surname_select[1])


updated_surname = (new_surname[0])

# new_name = input_wife.replace (old_wife_surname, updated_surname)



print(f"{updated_surname} {old_wife_surname}")




#tipping system

price = input("how much is your total purchase")

int_price = float (price)

tip = int_price * 0.15

total_cost = tip + int_price

print(tip)

print(total_cost)