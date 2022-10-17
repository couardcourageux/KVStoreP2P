
from dataclasses import dataclass


class KeyNotFound(Exception):
    """Used to specify that there is no entry for this key

    :param str Exception: the key in question
    """
    
    def __init__(self, key: str) -> None:
        self.key = key
        self.message = f"key {key} not found"
        super().__init__(self.message)
        
class UnauthorizedReading(Exception):
    """Used to specify that the user cannot access this entry

    :param str Exception: the key in question
    :param indent Exception: the the user id
    """
    def __init__(self, key: str, ident: str) -> None:
        self.key = key
        self.id = ident
        self.message = f"user {ident} have no read access over the key {key}"
        super().__init__(self.message)
        
class UnauthorizedWriting(Exception):
    """Used to specify that the user cannot write this entry

    :param str Exception: the key in question
    :param indent Exception: the the user id
    """
    def __init__(self, key: str, ident: str) -> None:
        self.key = key
        self.id = ident
        self.message = f"user {ident} have no write access over the key {key}"
        super().__init__(self.message)


a = KeyNotFound("22")
print(a, type(a))