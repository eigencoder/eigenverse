from point import Point

class BaseUnit(Point):
    def __init__(self, **kwargs):
        """

        :param kwargs: Required for Point init
        :return:
        """
        super(BaseUnit, self).__init__(kwargs)
        self.hp = 1
        self.dps = 0.1
        #self.speed = 1
        #self.storage = []

    def move(self, vector):
        if not len(v) == self.size:
            logger.error("Attempting to move by a vector of incorrect dimensions")
            return -1
        self += Point(coordinates=vector)

    @property
    def serialized(self):
        data = super(BaseUnit, self).serialized
        data['hp'] = self.hp
        data['dps'] = self.dps
        return data
