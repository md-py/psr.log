""" PSR-3 Logger interface port (see https://www.php-fig.org/psr/psr-3/) """


# Metadata
__version__ = '1.0.0'
__all__ = (
    # Metadata
    '__version__',
    # Contract
    'LoggerInterface',
    'LogLevel',
    'LoggerAwareInterface',
)


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

    See https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md
    for the full interface specification.
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


class LogLevel:
    """ Describes log levels. """
    EMERGENCY = 'emergency'
    ALERT = 'alert'
    CRITICAL = 'critical'
    ERROR = 'error'
    WARNING = 'warning'
    NOTICE = 'notice'
    INFO = 'info'
    DEBUG = 'debug'


class LoggerAwareInterface:
    """ Describes a logger-aware instance. """

    def set_logger(self, logger: LoggerInterface) -> None:
        """ Sets a logger instance on the object. """
        raise NotImplementedError
