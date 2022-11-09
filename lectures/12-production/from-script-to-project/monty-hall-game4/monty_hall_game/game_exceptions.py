class InvalidGameInput(Exception):
    """This exception should be thrown if invalid input is provided to the
    game. An example is to finish the game before selecting a door."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "A InvalidGameInput Exception occurred: {}".format(self.message)
