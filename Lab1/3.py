
import re
re_integer = re.compile("^\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value

def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    return number


num1 = validator_2(input("введите x: "))

if num1 >= -3.5:
	res = 4 * num1 * num1 + 2 * num1 - 19	

	print ("Result 1: ", res)

if num1 < 3.5:
	res1 = (-2*num1)/-4*num1 + 1

	print("Result 2: " , res1)
