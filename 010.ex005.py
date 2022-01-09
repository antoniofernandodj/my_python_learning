"""
Create a script that reads a value in metters and shows the value converted to centimetters, millimetters and kilometters
"""

m = float(input('Input a value in metters: '))
mm = m*1000
cm = m*100
km = m/1000

print(f"\nThe value inputed is {m}m")
print(f"The value {m}m in mm is {mm}mm")
print(f"The value {m}m in cm is {cm}cm")
print(f"The value {m}m in km is {km}km")
