import time

class Event(object):

    def __init__(self):
        self.id = 0
        self.time = time.time()
        self.player = None

    def serialize(self):
        """

        :return: JSON object
        """
        return ''