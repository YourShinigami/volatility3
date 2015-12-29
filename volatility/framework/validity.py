"""
Created on 4 May 2013

@author: mike
"""


class ValidityRoutines(object):
    """Class to hold all validation routines, such as type checking"""

    def _check_type(self, value, valid_type):
        """Checks that value is an instance of valid_type, and returns value if it is, or throws a TypeError otherwise

        :param value: The value of which to validate the type
        :type value: object
        :param valid_type: The type against which to validate
        :type valid_type: type
        """
        assert isinstance(value,
                          valid_type), self.__class__.__name__ + " expected " + valid_type.__name__ + ", not " + type(
            value).__name__
        return value

    def _check_class(self, klass, valid_class):
        """Checks that class is an instance of valid_class, and returns klass if it is, or throws a TypeError otherwise

        :param klass: Class to validate
        :type klass: class
        :param valid_class: Valid class against which to check class validity
        :type valid_class: class
        """
        assert issubclass(klass,
                          valid_class), self.__class__.__name__ + " expected " + valid_class.__name__ + ", not " + klass.__name__
