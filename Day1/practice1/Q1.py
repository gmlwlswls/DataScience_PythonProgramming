# Currency Conversion Functions

# Write functions to convert an amount from one currency to another.

### Requirements
# * Define a function `convert_to_usd(krw)`.
# * Define a function `convert_to_krw(usd)`.
# * The functions should return values rounded to two decimal places.
# * Assume the exchange rate is 1 USD = 1300 KRW.
# * Ensure that the functions produce the expected output for the given test cases.

# Define a function to convert KRW to USD

usd_to_krw_rate = 1300

def convert_to_usd(krw):
    # Write your implementation here
    usd = krw / usd_to_krw_rate
    return round(usd, 2)

krw = 12500
print(f"{krw} KRW is {convert_to_usd(krw)} USD.")    

# Define a function to convert USD to KRW
def convert_to_krw(usd):
    # Write your implementation here
    return usd * usd_to_krw_rate
    
usd= 20
print(f"{usd} USD is {convert_to_krw(usd)} KRW")
