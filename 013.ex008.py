"""
Create a script that reads the height and width of a wall in metters, comput it area and the necessary amount of ink to paint it, knowing that each L of ink paints 2m² of area
"""

h = float(input('How the measure in height of the wall? '))
d = float(input('How the measure in width of the wall? '))

a = h*d

a = round(a,2)

print(f"the area of the wall is {a}m² and you will need {a/2}L of ink to paint it")
