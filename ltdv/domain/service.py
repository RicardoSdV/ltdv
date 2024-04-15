from typing import Dict, Optional

from pandas import DataFrame
from yfinance import Ticker

from ltdv.constants import TESLA_TICKER_NAME, Keys
from ltdv.domain.types import Expirations, OptionChainsYF, OptionChains, PortfolioOptionsInfo, PortfolioOptionInfo, \
    OptionId, Portfolio, Portfolios
from ltdv.infra.repo import PortfoliosRepo


class Service:
    def __init__(self) -> None:
        ticker = self.instantiate_tesla_ticker()

        self.expirations = self.request_expirations(ticker)
        yf_option_chains: OptionChainsYF = self.request_option_chains(ticker, self.expirations)

        self.option_chains: OptionChains = self.serialize_yf_option_chains(yf_option_chains)

        self.portfolios: Portfolios = PortfoliosRepo.load_portfolios_from_json()
        self.portfolio: Optional[Portfolio] = None
        self.portfolio_option_info: Optional[PortfolioOptionInfo] = None
        self.portfolio_options_info: Optional[PortfolioOptionsInfo] = None


    def run(self) -> None:

        for portfolio in self.portfolios.values():
            total_options_value = 0
            portfolio_options = portfolio[Keys.OPTIONS_INFO.value]

    def update_portfolio_options_info(self) -> None:
        for option_id, option_info in self.portfolio_options_info.items():

            expiration_index = self.expiration_index(option_id)
            option_chain = self.option_chains[expiration_index]
            calls, puts, underlying = option_chain

            if self.is_call(option_id):
                option_index = self.option_index(option_id, calls['contractSymbol'])
                options = calls
            else:
                option_index = self.option_index(option_id, puts['contractSymbol'])
                options = puts

            bid = self.option_bid(option_index, options)
            option_info[option_id]['bid'] = bid
            option_bid_value = round(self.calc_option_value(self.option_count(option_id), bid), 2)

    def option_count(self, option_id: OptionId) -> int:
        count = self.portfolio_option_info[option_id][Keys.Options.COUNT.value]
        assert isinstance(count, int)
        return count

    @staticmethod
    def loop_though_portfolio_options(portfolio_options: Dict, expirations: Expirations) -> None:
        pass


    @staticmethod
    def instantiate_tesla_ticker() -> Ticker:
        return Ticker(TESLA_TICKER_NAME)

    @staticmethod
    def request_expirations(ticker: Ticker) -> Expirations:
        return ticker.options

    @staticmethod
    def request_option_chains(ticker: Ticker, expirations: Expirations) -> OptionChainsYF:
        return [ticker.option_chain(exp) for exp in expirations]

    @staticmethod
    def serialize_yf_option_chains(option_chains: OptionChainsYF) -> OptionChains:
        return [
            [el.to_dict() if isinstance(el, DataFrame) else el for el in option_chain]
            for option_chain in option_chains
            if all(isinstance(el, (DataFrame, dict)) for el in option_chain)
        ]

    @staticmethod
    def is_call(option_id: str) -> bool:
        return option_id[10] == 'C'

    def expiration_index(self, option_id: str) -> int:
        return self.expirations.index(f'20{option_id[4:6]}-{option_id[6:8]}-{option_id[8:10]}')

    @staticmethod
    def option_index(my_option_id: str, symbols: Dict):
        for index, option_id in symbols.items():
            if my_option_id == option_id:
                return index

    @staticmethod
    def option_bid(index: int, options: Dict) -> float:
        return options['bid'][index]

    @staticmethod
    def calc_option_value(count: int, premium: float) -> float:
        return count * 100 * premium

