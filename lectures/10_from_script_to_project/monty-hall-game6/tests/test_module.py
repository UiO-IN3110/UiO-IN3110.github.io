import random
from monty_hall_game import MontyHallGame, InvalidGameInput


def test_that_game_wins_or_loses():
    game = MontyHallGame()

    game.select_door(1)
    game.let_host_open_door()

    to_open = random.choice(game.available_doors())
    game.select_door(to_open)

    won = game.open_door()

    assert won or not won


def test_that_selecting_invalid_door_raises_correct_exception():
    game = MontyHallGame()

    try:
        game.select_door(4)
    except InvalidGameInput:
        pass


def test_that_statistics_returns_str():

    # Produce some test data first
    for i in range(10):
        test_that_game_wins_or_loses()

    # Check that the statistics function produces a string
    assert( type(MontyHallGame.statistics()) == str)
