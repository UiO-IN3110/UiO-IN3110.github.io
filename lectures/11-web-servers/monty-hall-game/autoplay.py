import json
import random
from pprint import pprint

import requests
from tqdm import tqdm


url = "http://127.0.0.1:8000"

def play(switch):
    r = requests.post(f"{url}/games")
    game_id = r.json()["id"]

    first_choice = random.randint(1, 3)

    r = requests.post(
        f"{url}/games/{game_id}/choose",
        data=json.dumps(
            {
                "door": first_choice,
            }
        ),
    )
    r = requests.post(
        f"{url}/games/{game_id}/choose-again",
        data=json.dumps(
            {
                "switch": switch,
            }
        ),
    )


def autoplay(samples):
    for i in tqdm(range(samples), desc="plays"):
        play(switch=True)
        play(switch=False)

    r = requests.get(f"{url}/statistics")
    stats = r.json()

    stay = stats['not changed']
    stay_rate = sum(stay) / len(stay)
    print(f"stay wins: {sum(stay)} / {len(stay)}: {stay_rate:.0%}")

    switch = stats['changed']
    switch_rate = sum(switch) / len(switch)
    print(f"switch wins: {sum(switch)} / {len(switch)}: {switch_rate:.0%}")


if __name__ == "__main__":
    autoplay(100)
