from enum import Enum
from pathlib import Path

SOURCE_DIR_PATH = Path(__file__).resolve().parent
ROOT_DIR_PATH = SOURCE_DIR_PATH.parent
INFRA_DIR_PATH = SOURCE_DIR_PATH / 'infra'
PORTFOLIOS_DIR_PATH = INFRA_DIR_PATH / 'portfolios'
PORTFOLIOS_PATH = PORTFOLIOS_DIR_PATH / 'portfolios.json'


TESLA_TICKER_NAME = 'TSLA'


class Keys(Enum):
    CASH = 'cash'
    SHARE_COUNT = 'share_count'
    MARGIN_CALL = 'margin_call'
    OPTIONS_VALUE = 'options_value'
    TOTAL_SHARE_OPPORTUNITY_COST = 'total_share_opportunity_cost'

    OPTIONS_INFO = 'options_info'

    class Options(Enum):
        COUNT = 'count'
        BID = 'bid'
        BID_VALUE = 'bid_value'
        SHARE_OPPORTUNITY_COST = 'share_opportunity_cost'
