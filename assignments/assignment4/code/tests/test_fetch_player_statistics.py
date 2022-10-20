from operator import itemgetter
from pathlib import Path

import pytest
from fetch_player_statistics import (
    find_best_players,
    get_player_stats,
    get_players,
    get_teams,
)

playoff_url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"


def test_get_teams():
    teams = get_teams(playoff_url)
    assert isinstance(teams, list)
    assert len(teams) == 8
    assert isinstance(teams[0], dict)
    for team in teams:
        team_keys = set(team.keys())
        assert "name" in team_keys
        assert "url" in team_keys

    teams = sorted(teams, key=itemgetter("name"))
    assert teams == [
        {
            "name": "Boston",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Boston_Celtics_season",
        },
        {
            "name": "Dallas",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Dallas_Mavericks_season",
        },
        {
            "name": "Golden State",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Golden_State_Warriors_season",
        },
        {
            "name": "Memphis",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Memphis_Grizzlies_season",
        },
        {
            "name": "Miami",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Miami_Heat_season",
        },
        {
            "name": "Milwaukee",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Milwaukee_Bucks_season",
        },
        {
            "name": "Philadelphia",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Philadelphia_76ers_season",
        },
        {
            "name": "Phoenix",
            "url": "https://en.wikipedia.org/wiki/2021%E2%80%9322_Phoenix_Suns_season",
        },
    ]


@pytest.mark.parametrize(
    "team_url, n_players, expected_players",
    [
        (
            "https://en.wikipedia.org/wiki/2021–22_Golden_State_Warriors_season",
            17,
            [
                {
                    "name": "Bjelica, Nemanja",
                    "url": "https://en.wikipedia.org/wiki/Nemanja_Bjelica",
                },
                {
                    "name": "Wiseman, James",
                    "url": "https://en.wikipedia.org/wiki/James_Wiseman",
                },
            ],
        ),
        (
            "https://en.wikipedia.org/wiki/2021–22_Philadelphia_76ers_season",
            17,
            [
                {
                    "name": "Bassey, Charles",
                    "url": "https://en.wikipedia.org/wiki/Charles_Bassey",
                },
                {
                    "name": "Thybulle, Matisse",
                    "url": "https://en.wikipedia.org/wiki/Matisse_Thybulle",
                },
            ],
        ),
    ],
)
def test_get_players(team_url, n_players, expected_players):
    players = get_players(team_url)
    assert isinstance(players, list)
    assert len(players) == n_players
    for expected_player in expected_players:
        for player in players:
            if player["name"] == expected_player["name"]:
                assert player["url"] == expected_player["url"]
                break
        else:
            assert False, f"{expected_player} not found in {players}"


@pytest.mark.parametrize(
    "player_url, team, stats",
    [
        (
            "https://en.wikipedia.org/wiki/Giannis_Antetokounmpo",
            "Milwaukee",
            {
                "points": 29.9,
                "assists": 5.8,
                "rebounds": 11.6,
            },
        ),
    ],
)
def test_get_player_stats(player_url, team, stats):
    player_stats = get_player_stats(player_url, team)
    assert isinstance(player_stats, dict)
    for key, value in stats.items():
        assert key in player_stats
        assert player_stats[key] == value


def test_find_best_players(tmpdir):
    tmpdir.chdir()
    find_best_players(playoff_url)

    # make sure we created the plots in the required directory:
    dest_dir = Path("NBA_player_statistics")
    assert dest_dir.exists()
    print(list(dest_dir.iterdir()))
    assert list(dest_dir.glob("points.*"))
    assert list(dest_dir.glob("assists.*"))
    assert list(dest_dir.glob("rebounds.*"))
