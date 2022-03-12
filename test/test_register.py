"""Test the register module."""
import gym
from gym_reversi.register import register
from gym_reversi.register import retrieve_gym_id


def test_retrieve_gym_id():
    """Test retrieve_gym_id()."""
    assert retrieve_gym_id(6) == "Reversi6x6-v0"
    assert retrieve_gym_id(8) == "Reversi8x8-v0"


def test_register():
    """Test register() and gym.make()."""
    register(board_size=6)
    env = gym.make("Reversi6x6-v0")
    assert env.board_size == 6


def test_gym_make():
    """Test gym.make()."""
    # 8x8 can be made without register.
    env = gym.make("Reversi8x8-v0")
    assert env.board_size == 8
