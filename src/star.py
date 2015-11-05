from point import Point
from random import randint

import logging
logger = logging.getLogger(__name__)


class Star(Point):
    def __new__(cls, **kwargs):
        """
        Based on the Point class to allow for location and distance between objects
        :param cls:
        In order of precedence:
        :param loc: Location
        :param bounds: Maximum
        :param board:

        """
        # If exact location given, set coordinates
        if kwargs.get('coordinates'):
            print kwargs['coordinates']
            return super(Star, cls).__new__(cls, coordinates=kwargs['coordinates'])

        if kwargs.get('board'):
            # Get random position and check if it is available
            raise NotImplementedError

        # If set random location within bounds
        if kwargs.get('bounds'):
            return super(Star, cls).__new__(cls, coordinates=[randint(0, dimension) for dimension in kwargs['bounds']])

        logger.exception("No bounds defined for star with kwargs {kwargs}".format(kwargs=kwargs))
        return None

    def __init__(self, **kwargs):
        super(Star, self).__init__(kwargs)
        self.points_avail = 1
        self.points_max = 1
        # self.regen = 0 # min(self.available * 2, max) # growth vs linear vs none regeneration per [minute]

    @property
    def serialized(self):
        data = super(Star, self).serialized
        data['points_avail'] = self.points_avail
        return data
