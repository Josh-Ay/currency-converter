import httpx
from bs4 import BeautifulSoup
from httpx import Client

# dict of tested currencies working on the service
SUPPORTED_CURRENCIES = {
    "NGN": "Naira",
    "USD": "United States Dollar",
}

# element containing result
ELEMENT_SELECTOR = 'span.FCUp0c.rQMQod'


class ConvertTool:
    def __init__(self, amount: float, input_currency: str, output_currency: str):
        # creating a new httpx client to mimic an actual browser request
        self.client = Client(
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/62.0.3202.94 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
            },
            follow_redirects=True,
            http2=True,
        )

        self.amount = amount
        self.input_cur = input_currency
        self.output_cur = output_currency
        self.query_string = f'https://google.com/search?q=${input_currency}+rate+to+${output_currency}'

    def get_results_from_web(self) -> dict:

        try:
            # fetching the results from google
            response = self.client.get(self.query_string)

            # failed to fetch results from google
            if response.status_code != 200:
                return {
                    "error": "Failed to fetch data",
                    "code": 408
                }

            # creating soup with the results gotten back
            soup = BeautifulSoup(response.text, "html.parser")

            try:
                # extracting the currency's rate from the span element containing it
                result_text = soup.select_one(ELEMENT_SELECTOR).text
                print(result_text)
                base_value = result_text.split('= ')[1].split(' ')[0] if '=' in result_text else result_text.split(' ')[
                    0]
            except IndexError:
                # extraction was not successful(element was probably not found)
                return {
                    "error": "Result extraction failed. Please try again later",
                    "code": 500
                }

            try:
                base_value_num = float(base_value.replace(',', ''))
            except ValueError:
                return {
                    "error": "Result parsing failed. Please try again later",
                    "code": 500
                }

            return {
                "input_amount": self.amount,
                "value": self.amount * base_value_num,
                "rate": base_value_num,
                "base_currency": self.input_cur,
                "base_currency_name": SUPPORTED_CURRENCIES[f'{self.input_cur}'],
                "result_currency": self.output_cur,
                "result_currency_name": SUPPORTED_CURRENCIES[f'{self.output_cur}'],
            }

        except (httpx.ConnectTimeout, httpx.ConnectError) as e:
            # connection timed out or had an error when trying to fetch results
            return {
                "error": "Request timed out",
                "code": 408
            }
