from typing import Tuple, Dict, List, Union, Any

from pandas import DataFrame

Expirations = Tuple[str, ...]
OptionChainYF = Tuple[DataFrame, DataFrame, Dict]
OptionChainsYF = List[OptionChainYF]

OptionChain = List[Union[Dict, Any]]
OptionChains = List[OptionChain]  # 2 dicts, calls & puts
