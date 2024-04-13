from json import dumps
from typing import Dict, Any

from settings import marginRequirement
from my_types import OptionChains, Expirations, OptionChain


def calc_margin_call(cash: float, share_count: int) -> float:
    return ((-cash * marginRequirement) / (marginRequirement - 1)) / share_count


def _turn_to_str(_any: str) -> str:
    return str(_any)


def pretty_print(data: Any):
    print(dumps(data, default=_turn_to_str, indent=4))


def calc_share_opportunity_cost(margin_call: float, share_price: float, share_count: int, cashInAccount: float, totalOpenOptionsValue: float):
    mc = margin_call
    mr = marginRequirement
    tp = share_price
    ts = share_count
    ca = cashInAccount
    tov = totalOpenOptionsValue

    return (-mr * tov + mc * ts - mc * mr * ts - mr * ca) / (-mc + mc * mr - mr * tp)


def get_expiration_index(option_id: str, expirations: Expirations) -> int:
    # TSLA240816C00005000
    date = f'20{option_id[4:6]}-{option_id[6:8]}-{option_id[8:10]}'
    return expirations.index(date)


def get_option_index(my_option_id: str, symbols: Dict):
    for index, option_id in symbols.items():
        if my_option_id == option_id:
            return index


def is_call(option_id: str) -> bool:
    return option_id[10] == 'C'


def get_option_bid_premium_by_index(index: int, options: Dict) -> float:
    return options['bid'][index]


def set_option_premium_by_id(option_id: str, bid_premium: float, option_ids_and_counts) -> None:
    option_ids_and_counts[option_id]['last_bid_premium'] = bid_premium


def calc_total_option_value(count: int, premium: float) -> float:
    return count * 100 * premium
