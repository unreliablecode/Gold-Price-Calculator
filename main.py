import requests

# Replace with your actual API keys
METALS_API_KEY = 'your_metals_api_key'
OPEN_EXCHANGE_RATES_API_KEY = 'your_open_exchange_rates_api_key'

def get_gold_price():
    """Fetches the real-time gold price in USD per ounce from Metals-API."""
    url = f"https://metals-api.com/api/latest?access_key={METALS_API_KEY}&base=XAU&symbols=USD"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or 'quote' not in data or 'USD' not in data['quote']:
        raise Exception("Failed to fetch gold price from Metals-API")
    
    return data['quote']['USD']

def get_exchange_rate():
    """Fetches the real-time USD to IDR exchange rate from Open Exchange Rates."""
    url = f"https://openexchangerates.org/api/latest.json?app_id={OPEN_EXCHANGE_RATES_API_KEY}&symbols=IDR"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or 'rates' not in data or 'IDR' not in data['rates']:
        raise Exception("Failed to fetch exchange rate from Open Exchange Rates")
    
    return data['rates']['IDR']

def convert_weight(weight, unit):
    """Converts weight from grams or kilograms to troy ounces."""
    if unit.lower() == 'grams':
        return weight / 31.1034768  # 1 troy ounce = 31.1034768 grams
    elif unit.lower() == 'kilograms':
        return (weight * 1000) / 31.1034768  # 1 troy ounce = 31.1034768 grams
    else:
        raise ValueError("Invalid unit. Please enter 'grams' or 'kilograms'.")

def calculate_total_price(weight, unit, gold_price_usd, exchange_rate):
    """Calculates the total price of gold in IDR."""
    troy_ounces = convert_weight(weight, unit)
    price_usd = troy_ounces * gold_price_usd
    price_idr = price_usd * exchange_rate
    return price_idr

def main():
    try:
        # Get real-time gold price and exchange rate
        gold_price_usd = get_gold_price()
        exchange_rate = get_exchange_rate()
        
        # Get user input
        weight = float(input("Enter the weight of gold (number only): "))
        unit = input("Enter the unit (grams or kilograms): ").strip().lower()
        
        # Validate and calculate
        total_price_idr = calculate_total_price(weight, unit, gold_price_usd, exchange_rate)
        
        # Display the result
        print(f"The total price of {weight} {unit} of gold is approximately {total_price_idr:.2f} IDR.")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
