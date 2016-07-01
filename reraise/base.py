import sys
import inspect
from six import exec_

PY2 = sys.version_info[0] == 2


if PY2:
    # because PY3 fails syntax here
    exec_('def reraise_as(tp, value, tb=None):\n'
          '    __traceback_hide__ = True\n'
          '    raise tp, value, tb')
else:
    def reraise_as(tp, value, tb=None):
        __traceback_hide__ = True  # NOQA
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value


def reraise(new_exception_or_type):
    """
    >>> try:
    >>>     do_something_crazy()
    >>> except Exception:
    >>>     reraise(UnhandledException)
    """
    __traceback_hide__ = True  # NOQA

    e_type, e_value, e_traceback = sys.exc_info()

    if inspect.isclass(new_exception_or_type):
        new_type = new_exception_or_type
        new_exception = new_exception_or_type()
    else:
        new_type = type(new_exception_or_type)
        new_exception = new_exception_or_type

    new_exception.__cause__ = e_value

    try:
        reraise_as(new_type, new_exception, e_traceback)
    finally:
        del e_traceback
