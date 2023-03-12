import requests
import json
from config import keys


class APIExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIExeption(f'Вы хотите конвертировать одинаковые валюты - "{base}"')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIExeption(f'Проверьте правильность ввода валюты - "{base}"')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIExeption(f'Проверьте правильность ввода валюты - "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Проверьте правильность ввода количества валюты - "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]] * amount
        total_base = round(total_base, 3)

        return total_base
