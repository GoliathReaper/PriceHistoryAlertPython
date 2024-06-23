import csv
from pricehistory import PriceCheck


def read_urls_from_csv(csv_file_path):
    """
    Read URLs and prices from a CSV file.

    :param csv_file_path: Path to the CSV file.
    :return: A list of tuples containing URLs and their corresponding prices.
    """
    urls_and_prices = []
    try:
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            # next(reader)  # Uncomment this line if the CSV has a header row
            for row in reader:
                try:
                    url, price = row
                    urls_and_prices.append((url, int(price)))
                except ValueError:
                    print(f"Error parsing the row: {row}")
    except FileNotFoundError:
        print(f"The file {csv_file_path} does not exist.")
    return urls_and_prices


def check_prices_from_csv(csv_file_path):
    """
    Check prices for all URLs listed in the CSV file.

    :param csv_file_path: Path to the CSV file.
    """
    urls_and_prices = read_urls_from_csv(csv_file_path)
    for url, price in urls_and_prices:
        checker = PriceCheck(url, price)
        checker.check_price()


def main():
    csv_file_path = "price_url.csv"
    check_prices_from_csv(csv_file_path)


if __name__ == "__main__":
    main()
