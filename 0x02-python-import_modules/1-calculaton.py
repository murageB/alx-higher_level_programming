#!/usr/bin/python3 
import calculator_1

a = 10
b = 5

add = calculator_1.add(a, b)
print('{} + {} = {}'.format(a, b, add))
sub = calculator_1.sub(a, b)
print('{} - {} = {}'.format(a, b, sub))
mul = calculator_1.mul(a, b)
print('{} * {} = {}'.format(a, b, mul))
div = calculator_1.div(a, b)
print('{} / {} = {}'.format(a, b, div))
