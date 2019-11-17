"""
A class at the top level that does something
"""


class Core:

    def __init__(self):
        """
        Constructor
        """
        print('__init__')

    @staticmethod
    def do(param1, param2):
        """
        This function will do something with the provided parameters

        :param param1: The first parameter
        :type param1: int
        :param param2: The second parameter
        :type param2: int

        :raises: RuntimeError if the parameters are not ints

        :return: int
        """
        if not isinstance(param1, int):
            raise RuntimeError("param1 must be an int, not {0}".format(type(param1)))
        if not isinstance(param2, int):
            raise RuntimeError("param2 must be an int, not {0}".format(type(param2)))
        return param1+param2
