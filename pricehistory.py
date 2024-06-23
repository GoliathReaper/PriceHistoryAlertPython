import requests
from bs4 import BeautifulSoup


class PriceCheck:
    def __init__(self, url, max_price, proxies=None):
        """
        Initialize the PriceCheck object.

        :param url: URL of the product page to check.
        :param max_price: Maximum acceptable price.
        :param proxies: (Optional) Dictionary of proxies to use for the request.
        """
        self.url = url
        self.max_price = max_price
        self.proxies = proxies
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'
        }

    def fetch_page(self):
        """
        Fetch the webpage content.

        :return: Response text if the request was successful, else None.
        """
        try:
            response = requests.get(self.url, headers=self.headers, proxies=self.proxies)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            return response.text
        except requests.RequestException as e:
            print(f"Failed to retrieve the webpage: {e}")
            return None

    def parse_price(self, html):
        """
        Parse the price from the HTML content.

        :param html: HTML content of the webpage.
        :return: Parsed price as an integer if found, else None.
        """
        soup = BeautifulSoup(html, 'html.parser')
        price_element = soup.find(class_="text-2xl")

        if price_element:
            try:
                price_text = price_element.text.strip('₹').replace(",", "")
                return int(price_text)
            except ValueError:
                print("Error parsing the price")
                return None
        else:
            print("Price not found")
            return None

    def check_price(self):
        """
        Check if the price is within the acceptable range.

        :return: None
        """
        html = self.fetch_page()
        if html:
            price = self.parse_price(html)
            if price is not None:
                print(f"Price: {price}")
                if price <= self.max_price:
                    print("You can buy it!")
                else:
                    print("Price is high")

# Example usage
# proxies = {'http': 'http://proxy.example.com:8080', 'https': 'https://proxy.example.com:8080'}
# checker = PriceCheck("https://example.com/product", 30000, proxies)
# checker.check_price()
