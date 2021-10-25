from bs4 import BeautifulSoup

from requesting_urls import get_html


def extract_teams():
    """Extract team names and urls from the NBA Playoff 'Bracket' section table.

    Returns:
        team_names (list): A list of team names that made it to the conference
            semifinals.
        team_urls (list): A list of absolute Wikipedia urls corresponding to team_names.

    """

    # get html using for example get_html from requesting_urls
    html = get_html(url)

    # create soup
    soup = BeautifulSoup(html, "html.parser")
    # find bracket we are interested in
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")

    # create list of teams
    team_list = []

    for i in range(1, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]

        # Filter out the cells that are empty
        cells_text = [cell for cell in cells_text if cell]

        # Find the rows that contain seeding, team name and games won
        if len(cells_text) > 1:
            YOUR_CODE

    # Filter out the teams that appear more than once, which means they made it
    # to the conference semifinals
    team_list_filtered = YOUR_CODE

    # create lists of team names and urls to the team website
    team_names = []
    team_urls = []

    # your code

    return team_names, team_urls


def extract_players(team_url):
    """Extract players that played for a specific team in the NBA playoffs.

    Args:
        team_url (str): URL to the Wikipedia article of the season of a given
            team.

    Returns:
        player_names (list): A list of players names corresponding to the team whos URL was passed.
            semifinals.
        player_urls (list): A list of Wikipedia URLs corresponding to
            player_names of the team whos URL was passed.

    """

    # keep base url
    base_url = "https://en.wikipedia.org"

    # get html for each page using the team url you extracted before
    html = get_html(team_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # get the header of the Roster
    roster_header = soup.find(id="Roster")
    # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # prepare lists for player names and urls
    player_names = []
    player_urls = []

    for i in range(0, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]

        if len(cells_text) == 7:
            rel_url = cells[2].find_next("a").attrs["href"]
            # Use e.g. regex to remove information in parenthesis following the name
            YOUR_CODE
            # create urls to each player
            # need to create absolute urls combining the base and the relative url
            player_urls.append(base_url + rel_url)

    return player_names, player_urls


def extract_player_statistics(player_url):
    """Extract player statistics for NBA player.

    # Note: Make yourself familiar with the 2020-2021 player statistics wikipedia page and adapt the code accordingly.

    Args:
        player_url (str): URL to the Wikipedia article of a player.

    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.

    """
    # As some players have incomplete statistics/information, you can set a default score, if you want.

    ppg = 0.0
    bpg = 0.0
    rpg = 0.0

    # get html
    html = get_html(player_url)

    # make soup
    soup = BeautifulSoup(html.text, "html.parser")

    # find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")

    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")

    try:
        # find regular season header
        # You might want to check for different spellings, e.g. capitalization
        # You also want to take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season")

        # next we should identify the table
        nba_table = regular_season_header.find_next("table")

    except:
        try:
            # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")

        except:
            return ppg, bpg, rpg

    # find nba table header and extract rows
    table_header = nba_table.find_all("th")
    # YOUR CODE

    # find the columns for the different categories
    ppg_column = YOUR_CODE_HERE
    # YOUR CODE HERE

    # Extract the scores from the different categories
    scores = YOUR_CODE

    # Convert the scores extracted to floats
    # Note: In some cases the scores are not defined but only shown as '-'. In such cases you can just set the score to zero or not defined.
    try:
        scores[i] = float(scores[i])
    except ValueError:
        scores[i] = 0.0

    return ppg, bpg, rpg
