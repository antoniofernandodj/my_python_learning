name = input('what is your name? ')
age = input('what is your age? ')
weight = input('what is your weight? ')
print(f'name: {name}, age: {age}, weight: {weight}')

# Not a good idea :(

name = input('\nwhat is your name? ')
age = int(input('what is your age? '))
weight = float(input('what is your weight? '))

print(
f'name: {name}, age: {age}, weight: {weight}'
)

# Better :)
