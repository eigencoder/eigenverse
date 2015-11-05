from point import Point

import logging
logger = logging.getLogger(__name__)


class Player(object):
    def __init__(self, **kwargs):
        """
        
        :param kwargs: Required for Point init 
        :return: 
        """
        self.collected_stars = 0
        self.token = None
        self.units = []  # For now each player will have only one unit, type Unit

    def __repr__(self):
        return str(self.serialized)

    @property
    def serialized(self):
        # data = super(Player, self).serialized
        data = {}
        data['collected_stars'] = self.collected_stars
        data['units'] = [unit.serialized for unit in self.units]
        return data

    def validate(self, token):
        return token == self.token

    # This belongs in Unit
    # def move(self, v):
    #     if not len(v) == self.size:
    #         logger.error("Attempting to move by a vector of incorrect dimensions")
    #         return -1
    #
    #     self += Point(coordinates=v)
