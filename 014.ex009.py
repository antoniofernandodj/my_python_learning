"""
Create a algorithm that reads the price of a product and shows its price with a discount of 5% and with a increase of 5%
"""

price = float(input('How is the price of the product? ')) 

incr = price + price * 5/100
incr = round(incr, 2)

disc = price - price * 5/100
disc = round(disc, 2)

print(f'the discount price is €{disc}, and the increase price is €{incr}')
