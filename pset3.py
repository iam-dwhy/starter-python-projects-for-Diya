# TODO: solve  the quadratic equation with variables a,b and c are to be given by users

# hints :  
import cmath

num_a = input("what is your value of a ")

num_b = input("what is your value of b")

num_c = input("what is your value of c")

a = int(num_a)

b = int(num_b)

c = int(num_c) 

x = a * c * 4

y = b ** 2

z = y - x

k = cmath.sqrt(z)

j = a * 2

f = -abs(b)

g = f + k

l = f - k

final_result_1 = g/j

final_result_2 = l/j

print(final_result_1)

print(final_result_2)


