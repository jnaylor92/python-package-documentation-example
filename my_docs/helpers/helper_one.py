"""
Helper Class for doing something
"""


class HelperOne:
    """
    Simple helper class
    """

    def __init__(self, msg):
        """
        Constructor

        :param msg: A message to print
        :type msg: str
        """
        print('__init__')
        self._msg = msg

    def print_it(self):
        """
        Print the message
        """
        print(self._msg)

    def print_something(self, something):
        """
        Print the message and the new something

        :param something: The additional text to print
        :type something: str
        :return: str, the printed string
        """
        ret = self._msg + " " + something
        print(ret)
        return ret
