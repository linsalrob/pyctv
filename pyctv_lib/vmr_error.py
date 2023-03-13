"""
A general error file for the VMR objects
"""

class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass

class ColorNotFoundError(Error):
    """
    Exception raised for a color not being found.

    :param message: explanation of the error
    """

    def __init__(self, message):
        self.message = message

class VMRBadlyFormatted(Error):
    """
    The VMR file is badly formatted and needs checking
    """

    def __init__(self, message):
        self.message = message