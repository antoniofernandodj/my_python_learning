"""
Create a script that reads how much money a person have in the wallet in euros and shows up how much they can buy

consider 1 EUR = 1,14 USD
"""

euro = float(input('How much euros does you have? '))

dollar = euro * 1.14
dollar = round(dollar, 2)

print(f"you can buy {dollar} dollars")
