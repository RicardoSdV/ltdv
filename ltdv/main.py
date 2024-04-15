from time import sleep

from ltdv.infra.repo import save_portfolios_to_json, load_portfolios_from_json
from ltdv.domain.types import OptionChain
from utils import get_expiration_index, get_option_index, is_call, get_option_bid_premium_by_index, \
    set_option_premium_by_id, calc_total_option_value, calc_margin_call, calc_share_opportunity_cost
from ltdv.domain.yf_service_proxy import YFserviceProxy

yf_service = YFserviceProxy()


expiry_dates = {
    '16-01-2026': 250,
    '18-12-2026': 300,
    '18-06-2026': 350
}




                portfolio['option_ids_and_counts'][option_id]['option_bid_value'] = option_bid_value
                portfolio['total_options_value'] += option_bid_value
                """ ------------------------------------------------------------------------------------------------------ """

    if expirations and last_options:
        for portfolio in portfolios.values():
            share_count = portfolio['share_count']
            cash = portfolio['cash']

            margin_call = calc_margin_call(cash, share_count)
            portfolio['margin_call'] = margin_call

            underlying = last_options[0][2]
            share_opportunity_cost = calc_share_opportunity_cost(
                margin_call,
                underlying['regularMarketPrice'],
                portfolio['share_count'],
                portfolio['cash'],
                portfolio['total_options_value'],
            )

    save_portfolios_to_json(portfolios)


    sleep(1)
