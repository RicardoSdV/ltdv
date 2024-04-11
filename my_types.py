from typing import Tuple, Dict, List, Union, Any

from pandas import DataFrame

Expirations = Tuple[str, ...]
OptionChainYF = Tuple[DataFrame, DataFrame, Dict]
OptionChainsYF = List[OptionChainYF]

OptionChains = List[List[Union[Dict, Any]]]
