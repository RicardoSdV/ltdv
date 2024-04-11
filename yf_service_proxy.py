from json import dumps
from typing import Optional

from pandas import DataFrame
from schedule import Scheduler
from yfinance import Ticker

from my_types import OptionChains, Expirations, OptionChainsYF


def _turn_to_str(_any: str) -> str:
    return str(_any)

def pretty_print(data: OptionChains):
    print(dumps(data, default=_turn_to_str, indent=4))


class YFserviceProxy:
    update_options_interval = 10
    ticker_name = 'TSLA'

    def __init__(self) -> None:
        self.schedule = Scheduler()
        self.schedule_periodic_requests()

        self.last_options: Optional[OptionChains] = None
        self.expirations: Optional[Expirations] = None

    def schedule_periodic_requests(self) -> None:
        self.schedule.every(self.update_options_interval).seconds.do(self.update_options)

    def update_options(self) -> None:
        self.expirations = Ticker(self.ticker_name).options

        tesla_ticker = Ticker(self.ticker_name)
        tesla_option_chains: OptionChainsYF = self.__request_options(tesla_ticker)

        serialized_option_chains = self.serialize_yf_option_chains(tesla_option_chains)

        # for outer_list in serialized_option_chains:
        #     for inner_list in outer_list:
        #         pretty_print(inner_list)
        #         input()

        self.last_options = serialized_option_chains

    @staticmethod
    def serialize_yf_option_chains(option_chains: OptionChainsYF) -> OptionChains:
        return [
            [el.to_dict() if isinstance(el, DataFrame) else el for el in option_chain]
            for option_chain in option_chains
            if all(isinstance(el, (DataFrame, dict)) for el in option_chain)
        ]

    def __request_options(self, ticker: Ticker) -> OptionChainsYF:
        options = [ticker.option_chain(exp) for exp in self.expirations]
        return options
