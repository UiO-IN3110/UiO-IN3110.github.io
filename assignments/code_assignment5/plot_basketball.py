import matplotlib.pyplot as plt

teams = {
    "UiO": [
        {
            "name": "Lisa",
            "ppg": 10.0,
        },
        {
            "name": "Vegard",
            "ppg": 9.2,
        },
    ],
    "Simula": [
        {
            "name": "Ingeborg",
            "ppg": 11.2,
        },
        {
            "name": "Min",
            "ppg": 4.5,
        },
    ],
}

# a matplotlib color for each team name (could be a name or a #rrggbb web color string)
color_table = {
    "UiO": "red",
    "Simula": "orange",
}


def plot_NBA_player_statistics(teams):
    """Plot NBA player statistics. In this case, just PPG"""
    count_so_far = 0
    all_names = []

    # iterate through each team and the
    for team, players in teams.items():
        # pick the color for the team, from the table above
        color = color_table[team]
        # collect the ppg and name of each player on the team
        # you'll want to repeat with other stats as well
        ppg = []
        names = []
        for player in players:
            names.append(player["name"])
            ppg.append(player["ppg"])
        # record all the names, for use later in x label
        all_names.extend(names)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players ppg,
        # with the team name as the label
        bars = plt.bar(x, ppg, color=color, label=team)
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # add the legend with the colors  for each team
    plt.legend(loc=0)
    # turn off gridlines
    plt.grid(False)
    # set the title
    plt.title("points per game")
    # save the figure to a file
    plt.savefig("ppg.png")


plot_NBA_player_statistics(teams)
