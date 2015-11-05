from star import Star


class Board(object):
    def __init__(self, bounds, star_count=10):
        self.size = bounds
        self.stars = {}
        self._generate(star_count, bounds)

    def _generate(self, star_count, bounds=(10, 10)):
        """

        :param board_limits: size of the board in each dimensions
        :param star_count: how many stars should appear on the board
        :return:
        """
        self.size = bounds

        # Initialize the stars locations
        # Could make star_num a uuid
        for star_num in xrange(star_count):
            self.stars[star_num] = Star(bounds=bounds)

