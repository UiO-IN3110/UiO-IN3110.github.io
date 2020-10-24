from bs4 import BeautifulSoup
import regex as re
​
website = get_html(
    "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
​
soup = BeautifulSoup(website, "html.parser")
# Second argument should be unique identifier for the table we need. Maybe class?
table = soup.find("table", ...)
# Im skipping over the header here, but you are required to use it to find the indices of `event`, `venue` and `type`
rows = table.findAll("tr")[1:]
found_event = None
found_venue = None
# Saving all necessary values in the list under
events = []
for row in rows:
    cells = row.findAll("td")
    # Hard coding indexes (you should find them using the header!)
    event = cells[1]
    # An event seems to always be a 1-3 digit number, so we can check that we have an event with a simple regex
    if re.match(r"\d{1,3}", event.text.strip()):
        found_event = event.text.strip()
    else:
        found_event = None
    # If event is cancelled, the index below might need to be shifted.
    venue = cells[4]
    # A venue seems to always have a span as first child, so we can use it to confirm we are looking at a venue
    if venue.find("span"):
        # We always remember the last venue, since it can span multiple rows (rowspan attribute!), aka don't set it to None
        found_venue = venue.text.strip()
​
    if found_event:
        # Discpline needs to also be found! I would also maybe do a simple regex check for it at the index it occurrs. (2 capital letter and ...)
        events.append((found_event, found_venue, discipline))
​
​
# THE CODE ABOVE IS FAR FROM COMPLETE AND IS ONLY PSEUDOCODE (does not run), ONLY USE IT AS MINOR INSPIRATION.
# The are many other approaches one can take with this task!
# Some further tips:
# When an event is cancelled, you will need to shift the indexes by a value (when event has a colspan attribute)
# Even though an event is cancelled, you might still need to remember the venue! (For the next event)
# USE MAINLY SOUP! regex can be used for simple strings, but majority of this task should be solved with soup!
