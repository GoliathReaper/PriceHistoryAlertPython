# PriceCheck Bot

This repository contains a Python script to check product prices on Amazon and Flipkart. It fetches product prices from pricehistory.com, compares them to a specified maximum price, and sends alerts if the price is within the acceptable range. Alerts are sent via Telegram.

## Features

- Fetches product prices from Amazon and Flipkart.
- Compares fetched prices with a maximum acceptable price.
- Reads URLs and prices from a CSV file.
- Sends alerts via Telegram.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- A Telegram bot token (get it from [BotFather](https://core.telegram.org/bots#6-botfather) on Telegram)
- A `.env` file with your Telegram bot token and chat ID

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/GoliathReaper/PriceHistoryAlertPython.git
   cd PriceHistoryAlertPython
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File:**

   Create a file named `.env` in the root directory of the project and add the following lines with your Telegram bot token and chat ID:

   ```
   BOT_TOKEN=your-telegram-bot-token
   CHAT_ID=your-telegram-chat-id
   ```

5. **Prepare the CSV File:**

   Create a CSV file named `price_url.csv` in the following format (without headers):

   ```
   url1,max_price1
   url2,max_price2
   ...
   ```

   Example:

   ```
   https://www.amazon.in/example-product,30000
   https://www.flipkart.com/example-product,25000
   ```

### Usage

1. **Run the Script:**

   ```bash
   python pricecheck.py
   ```

### Code Description

1. **PriceCheck Class:**

   - `__init__(self, url, max_price, proxies=None)`: Initializes the PriceCheck object with the product URL, maximum acceptable price, and optional proxies.
   - `fetch_page(self)`: Fetches the webpage content.
   - `parse_price(self, html)`: Parses the price from the HTML content.
   - `check_price(self)`: Checks if the price is within the acceptable range and prints the result.

2. **Reading URLs from CSV:**

   - `read_urls_from_csv(csv_file_path)`: Reads URLs and prices from a CSV file.
   - `check_prices_from_csv(csv_file_path)`: Checks prices for all URLs listed in the CSV file.

3. **Telegram Notifications:**

   - `telegram_message(msg)`: Sends a message to the specified chat on Telegram.

### Example

An example usage of the `PriceCheck` class is provided in the script:

```python
# Example usage
# proxies = {'http': 'http://proxy.example.com:8080', 'https': 'https://proxy.example.com:8080'}
# checker = PriceCheck("https://example.com/product", 30000, proxies)
# checker.check_price()
```

### Running the Main Function

The script contains a `main()` function that reads URLs and prices from a CSV file and checks the prices:

```python
def main():
    csv_file_path = "price_url.csv"
    check_prices_from_csv(csv_file_path)

if __name__ == "__main__":
    main()
```

### Telegram Bot Integration

The script integrates with Telegram to send notifications. The `telegram_message()` function sends a photo with a caption and a button to the specified chat:

```python
def telegram_message(msg):
    global message_count
    message_count += 1
```

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.


---
