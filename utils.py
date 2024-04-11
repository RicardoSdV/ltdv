from settings import marginRequirement
from my_types import OptionChains, Expirations


def calc_margin_call(cashInAccount: float, teslaShares: int) -> float:
    return ((-cashInAccount * marginRequirement) / (marginRequirement - 1)) / teslaShares

def calc_shares_opportunity_cost(marginCall: float, teslaSharePrice: float, teslaShares: int, cashInAccount: float, totalOpenOptionsValue: float):
    mc = marginCall
    mr = marginRequirement
    tp = teslaSharePrice
    ts = teslaShares
    ca = cashInAccount
    tov = totalOpenOptionsValue

    return (-mr * tov + mc * ts - mc * mr * ts - mr * ca) / (-mc + mc * mr - mr * tp)


def get_expiration_index(option_id: str, expirations: Expirations) -> int:
    date = f'{option_id[:2]}20{option_id[2:4]}-{option_id[4:6]}'
    return expirations.index(date)




def calc_total_open_options_value(option_ids_and_counts, last_options: OptionChains, expirations: Expirations):
    total_options_value = 0
    for option_id, count in option_ids_and_counts.items():
        option_value = count * 100 *

