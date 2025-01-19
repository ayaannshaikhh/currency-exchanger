
# Currency Exchanger

A Python application that fetches live currency exchange rates using the [ExchangeRate-API](https://www.exchangerate-api.com/). This program allows users to convert between two currencies and provides real-time exchange rates.

## Features

- Fetches the latest currency exchange rates.
- Allows users to input a base currency and target currency.
- Displays the conversion rate and equivalent value for $1 in the base currency.

## Prerequisites

- Python 3.6 or higher
- `requests` library for making HTTP requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ayaannshaikhh/currency-exchanger.git
   cd currency-exchanger
   ```

2. Install dependencies:
   If using a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install requests
   ```

3. (Optional) Verify the installation:
   ```bash
   python3 -m pip show requests
   ```

## Usage

1. Run the script:
   ```bash
   python3 currency_exchanger.py
   ```

2. Enter the base currency (e.g., `USD`) and the target currency (e.g., `EUR`) when prompted.

3. The script will fetch the latest exchange rate and display the conversion rate and equivalent value.

## Example

```bash
Please enter the base currency: USD
Please enter the target currency: EUR
Exchange rate from USD to EUR: 0.85
$1 in USD = 0.85 EUR
```

## Error Handling

- If the base or target currency is invalid, the program will notify you.
- If there are issues connecting to the API, an error message will be displayed.

## Limitations

- Requires an active internet connection to fetch exchange rates.
- The API key is hardcoded, which may limit its usage if the API key expires or rate limits are reached.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ExchangeRate-API](https://www.exchangerate-api.com/) for providing exchange rate data.
