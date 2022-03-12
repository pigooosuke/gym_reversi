from gym.envs.registration import register as gym_register


def retrieve_gym_id(board_size: int) -> str:
    """Return the gym id."""
    return f"Reversi{board_size}x{board_size}-v0"


def register(board_size: int) -> None:
    """Register the environment."""
    gym_id = retrieve_gym_id(board_size)

    gym_register(
        id=gym_id,
        entry_point="gym_reversi:ReversiEnv",
        kwargs={
            "player_color": "black",
            "opponent": "random",
            "observation_type": "numpy3c",
            "illegal_place_mode": "lose",
            "board_size": board_size,
        },
    )
