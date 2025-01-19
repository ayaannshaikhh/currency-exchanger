import requests

def fetch_rate(base_currency, target_currency):
    # Define the API URL with the base_currency
    url = f"https://v6.exchangerate-api.com/v6/bcc9a3721549678cbd5fc98f/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200:
            rates = data.get("conversion_rates", {})
            
            if target_currency in rates:
                exchange_rate = rates[target_currency]
                exchange_value = 1 * exchange_rate
                print(f"Exchange rate from {base_currency} to {target_currency}: {exchange_rate}")
                print(f"$1 in {base_currency} = ${exchange_value} {target_currency}")
            else:
                print(f"Target currency '{target_currency}' not found.")
        else:
            print(f"Error - Failed to retrieve data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    base_currency = input("Please enter the base currency: ").upper()
    target_currency = input("Please enter the target currency: ").upper()
    fetch_rate(base_currency, target_currency)
