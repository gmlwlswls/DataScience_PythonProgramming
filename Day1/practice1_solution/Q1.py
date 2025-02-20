# Currency Conversion Functions

# Write functions to convert an amount from one currency to another.

### Requirements
# * Define a function `convert_to_usd(krw)`.
# * Define a function `convert_to_krw(usd)`.
# * The functions should return values rounded to two decimal places.
# * Assume the exchange rate is 1 USD = 1300 KRW.
# * Ensure that the functions produce the expected output for the given test cases.

def convert_to_usd(krw):
    return round(krw / 1300, 2)

def convert_to_krw(usd):
    return round(usd * 1300, 2)