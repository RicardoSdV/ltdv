from time import sleep

from my_types import OptionChain
from portfolios import portfolios
from utils import get_expiration_index, get_option_index, is_call, get_option_bid_premium_by_index, \
    set_option_premium_by_id, pretty_print, calc_total_option_value, calc_margin_call, calc_share_opportunity_cost
from yf_service_proxy import YFserviceProxy

yf_service = YFserviceProxy()


expiry_dates = {
    '16-01-2026': 250,
    '18-12-2026': 300,
    '18-06-2026': 350
}


def total_option_value():
    pass


while True:
    yf_service.schedule.run_pending()

    last_options = yf_service.last_options
    expirations = yf_service.expirations

    if expirations and last_options:

        """ Calculating total option value for portfolios"""
        for portfolio in portfolios.values():
            portfolio['total_options_value'] = 0.0
            option_ids_and_counts = portfolio['option_ids_and_counts']
            for option_id, option_info in option_ids_and_counts.items():
                expiration_index = get_expiration_index(option_id, expirations)
                option_chain: OptionChain = last_options[expiration_index]
                calls, puts, underlying = option_chain

                if is_call(option_id):
                    option_index = get_option_index(option_id, calls['contractSymbol'])
                    options = calls
                else:
                    option_index = get_option_index(option_id, puts['contractSymbol'])
                    options = puts

                option_bid_premium = get_option_bid_premium_by_index(option_index, options)
                set_option_premium_by_id(option_id, option_bid_premium, option_ids_and_counts)

                portfolio['total_options_value'] += calc_total_option_value(option_info['option_count'], option_bid_premium)
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


    sleep(1)
