from json import dump, load
from typing import Dict

from ltdv.constants import PORTFOLIOS_PATH
from ltdv.utils import turn_to_str


class PortfoliosRepo:
    @staticmethod
    def save_portfolios_to_json(portfolios: Dict) -> None:
        with open(PORTFOLIOS_PATH, 'w') as json_file:
            dump(portfolios, json_file, default=turn_to_str, skipkeys=True, indent=4)
        print('saved')


    @staticmethod
    def load_portfolios_from_json() -> Dict:
        with open(PORTFOLIOS_PATH, 'r') as json_file:
            portfolios = load(json_file)
        return portfolios
