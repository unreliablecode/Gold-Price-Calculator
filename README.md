# Gold Price Calculator

## Overview

The Gold Price Calculator is a Python application that allows users to calculate the total price of gold based on real-time market data. Users can input the weight of gold in either grams or kilograms, and the application fetches the current gold price and exchange rate to provide an accurate price in Indonesian Rupiah (IDR).

## Features

- **Real-time Gold Price:** Fetches the latest gold price in USD per troy ounce from an external API.
- **Currency Conversion:** Converts the total price from USD to IDR using real-time exchange rates.
- **User Input:** Allows users to specify the weight of gold in grams or kilograms.
- **Error Handling:** Gracefully handles user input errors and API request failures.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- API keys from:
  - [Metals-API](https://metals-api.com/)
  - [Open Exchange Rates](https://openexchangerates.org/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/unreliablecode/gold-price-calculator.git
   cd gold-price-calculator
   ```

2. Install the required libraries:
   ```bash
   pip install requests
   ```

3. Obtain API keys from Metals-API and Open Exchange Rates, and replace the placeholders in the code.

## Usage

Run the application using the following command:

```bash
python main.py
```

Follow the prompts to enter the weight of gold and the unit (grams or kilograms). The application will display the total price in IDR.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
