from json import dumps
from typing import Dict, Any

from settings import marginRequirement
from ltdv.domain.types import Expirations


def calc_margin_call(cash: float, share_count: int) -> float:
    return ((-cash * marginRequirement) / (marginRequirement - 1)) / share_count


def turn_to_str(_any: str) -> str:
    return str(_any)


def pretty_print(data: Any):
    print(dumps(data, default=turn_to_str, indent=4))


def calc_share_opportunity_cost(margin_call: float, share_price: float, share_count: int, cashInAccount: float, totalOpenOptionsValue: float):
    mc = margin_call
    mr = marginRequirement
    tp = share_price
    ts = share_count
    ca = cashInAccount
    tov = totalOpenOptionsValue

    return (-mr * tov + mc * ts - mc * mr * ts - mr * ca) / (-mc + mc * mr - mr * tp)





def set_option_premium_by_id(option_id: str, bid_premium: float, option_ids_and_counts) -> None:



