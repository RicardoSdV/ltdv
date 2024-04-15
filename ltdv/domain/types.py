from typing import Tuple, Dict, List, Union, Any

from pandas import DataFrame

PortfolioName = str
OptionId = str


Expirations = Tuple[str, ...]
OptionChainYF = Tuple[DataFrame, DataFrame, Dict]
OptionChainsYF = List[OptionChainYF]

OptionChain = List[Union[Dict, Any]]
OptionChains = List[OptionChain]  # 2 dicts, calls & puts


PortfolioOptionInfo = Dict[str, Union[int, float]]
PortfolioOptionsInfo = Dict[OptionId, PortfolioOptionInfo]
Portfolio = Dict[str, Union[int, float, PortfolioOptionsInfo]]
Portfolios = Dict[PortfolioName, Portfolio]

