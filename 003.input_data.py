name = input('what is your name? ')
age = input('what is your age? ')
weight = input('what is your weight? ')
print(f'name:{name}, age: {age}, weight:{weight}')

# Not a good idea :(

name = input('what is your name? ')
age = input(int('what is your age? '))
weight = input(float('what is your weight? '))
print(f'name: {name}, age: {age}, weight: {weight}')
print(f'name: {name}, age: {age}, weight: {weight}')

# Better :)
