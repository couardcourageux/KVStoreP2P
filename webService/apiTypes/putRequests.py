from pydantic import BaseModel


# from requests import UserId


### SetEntry Family############
class SetEntryBase(BaseModel):
    key: str
    value: str
    public_r: int = 0
    public_w: int = 0

class SetEntry(BaseModel):
    user_id: str
    entry: SetEntryBase
    
    
class SetEntries(BaseModel):
    user_id: str
    entries: list[SetEntryBase]
    
#############################
### delGetEntry Family############
class DelGetEntry(BaseModel):
    key: str
    user_id: str
    