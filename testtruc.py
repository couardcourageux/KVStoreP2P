from dataclasses import dataclass, field
from typing import List

@dataclass
class yolo:
    _truc: str = field(init=False, repr=False, default="yolo")
    _fun: List[str] = field(default_factory=list)
    
    @property
    def truc(self):
        return yolo._truc + "mdr"
    
if __name__ == '__main__':
    # yolo.truc = "thing"
    print(yolo.truc)
    # print(yolo._fun)