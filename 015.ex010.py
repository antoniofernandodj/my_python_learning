"""
Create an algorithm that reads a employee wage and shows his new wage, with an increase of 15%
"""

wage = float(input('Input the employee wage: '))

new_wage = wage * 1.15
new_wage = round(new_wage, 2)

print(
f"the new wage with 15% of increase is ${new_wage}"
)
