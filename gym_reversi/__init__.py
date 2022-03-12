from .register import register
from .register import retrieve_gym_id
from .reversi import ReversiEnv

# Register 8x8 environment by default.
register(board_size=8)

__all__ = [
    "register",
    "retrieve_gym_id",
    "ReversiEnv",
]
