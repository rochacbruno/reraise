import reraise
from unittest import TestCase


def an_error():
    raise NotImplementedError('foo bar')


class ReraiseAsTest(TestCase):
    def test_simple_without_value(self):
        try:
            try:
                an_error()
            except NotImplementedError:
                reraise(ValueError)
            else:
                self.fail('NotImplementedError was not raised')
        except ValueError as exc:
            assert str(exc) == ''
            assert str(exc.__cause__) == 'foo bar'
            assert isinstance(exc.__cause__, NotImplementedError)
            assert isinstance(exc, ValueError)
        else:
            self.fail('ValueError was not re-raised')

    def test_simple_with_value(self):
        try:
            try:
                an_error()
            except NotImplementedError:
                reraise(ValueError('biz baz'))
            else:
                self.fail('NotImplementedError was not raised')
        except ValueError as exc:
            assert str(exc) == 'biz baz'
            assert str(exc.__cause__) == 'foo bar'
            assert isinstance(exc.__cause__, NotImplementedError)
            assert isinstance(exc, ValueError)
        else:
            self.fail('ValueError was not re-raised')
