import secrets
import mmh3





#########################################
def create_secret_string(n: int) -> str:
    return secrets.token_hex(n)

def create_agent_id() -> str:
    return create_secret_string(256)


def create_node_id() -> str:
    return create_secret_string(128)
#########################################