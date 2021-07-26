""" Continued logger contract based on "PSR-3 Logger interface" port (see https://www.php-fig.org/psr/psr-3/) """


# Metadata
__version__ = '2.0.0'
__author__ = 'https://md.land/md'
__all__ = (
    # Metadata
    '__version__',
    '__author__',
    # Constants
    'LEVEL_EMERGENCY',
    'LEVEL_ALERT',
    'LEVEL_CRITICAL',
    'LEVEL_ERROR',
    'LEVEL_WARNING',
    'LEVEL_NOTICE',
    'LEVEL_INFO',
    'LEVEL_DEBUG',
    # Contract
    'LoggerInterface',
)


# Constants
LEVEL_EMERGENCY = 'emergency'
LEVEL_ALERT = 'alert'
LEVEL_CRITICAL = 'critical'
LEVEL_ERROR = 'error'
LEVEL_WARNING = 'warning'
LEVEL_NOTICE = 'notice'
LEVEL_INFO = 'info'
LEVEL_DEBUG = 'debug'


# Contract
class LoggerInterface:
    """
    Describes a logger instance.

    The message MUST be a string or object implementing __str__().

    The message MAY contain placeholders in the form: {foo} where foo
    will be replaced by the context data in key "foo".

    The context array can contain arbitrary data, the only assumption that
    can be made by implementors is that if an Exception instance is given
    to produce a stack trace, it MUST be in a key named "exception".
    """

    def emergency(self, message: str, context: dict = None) -> None:
        """ System is unusable. """
        raise NotImplementedError

    def alert(self, message: str, context: dict = None) -> None:
        """
        Action must be taken immediately.

        Example: Entire website down, database unavailable, etc. This should trigger the SMS alerts and wake you up.
        """
        raise NotImplementedError

    def critical(self, message: str, context: dict = None) -> None:
        """
        Critical conditions.

        Example: Application component unavailable, unexpected exception.
        """
        raise NotImplementedError

    def error(self, message: str, context: dict = None) -> None:
        """ Runtime errors that do not require immediate action but should typically be logged and monitored. """
        raise NotImplementedError

    def warning(self, message: str, context: dict = None) -> None:
        """
        Exceptional occurrences that are not errors.

        Example: Use of deprecated APIs, poor use of an API, undesirable things that are not necessarily wrong.
        """
        raise NotImplementedError

    def notice(self, message: str, context: dict = None) -> None:
        """ Normal but significant events. """
        raise NotImplementedError

    def info(self, message: str, context: dict = None) -> None:
        """
        Interesting events.

        Example: User logs in, SQL logs.
        """
        raise NotImplementedError

    def debug(self, message: str, context: dict = None) -> None:
        """ Detailed debug information. """
        raise NotImplementedError

    def log(self, level: str, message: str, context: dict = None) -> None:
        """ Logs with an arbitrary level. """
        raise NotImplementedError
