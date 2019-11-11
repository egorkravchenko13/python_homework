import re

re_integer = re.compile("^\d*$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    return number

import math
num1 = validator_2("введите сторону a: ")
num2 = validator_2("введите сторону b: ")
num3 = validator_2("введите сторону c: ")
 
res2 = math.acos((num1*num1+num2*num2-num3*num3)/(2*num1*num2))
res1 = math.acos((num1*num1+num3*num3-num2*num2)/(2*num1*num3))
res3 = math.acos((num2*num2+num3*num3-num1*num1)/(2*num2*num3))

print("A: ", res1, math.degrees(res1))
print("B: ", res2, math.degrees(res2))
print("C: ", res3, math.degrees(res3))