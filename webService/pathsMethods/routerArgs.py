from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import typing


### SetEntry Family############
@dataclass
class PutEntryDtc:
    key: str
    val: str
    user_id: str
    rights: Tuple[int, int]
    
@dataclass
class PutEntriesDtc:
    putEntries: List[PutEntryDtc]
##############################
### delEntry Family############
@dataclass
class DelGetEntryDtc:
    key:str
    user_id: str
###############################


