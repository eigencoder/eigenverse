import json

# MOVE THIS TO A BASE CLASS
class CommMixin(object):

    @property
    def serialized(self):
        """
        Must only contain types that can be encoded (see https://docs.python.org/2/library/json.html#json.JSONEncoder)
        :return: a structure containing all elements necessary to recreate the object.

        """
        return {}

    def encode(self, encoder=None):
        if not encoder:
            encoder = json.JSONEncoder()
        return encoder.encode(self.serialized)

    # Not sure if this is useful
    def decode(self, data, decoder=None):
        if not decoder:
            decoder = json.JSONDecoder()
        return decoder.decode(data)

