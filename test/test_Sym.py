import pytest
from code.Sym import Sym

"""
Fixture to setup and teardown sym object for tests.
"""


@pytest.fixture()
def sym_test():
    print("\nSetting up sym object for test")
    sym = Sym()
    yield sym
    print("\nDeleting sym object as a teardown")
    del sym


"""
Class to test Sym.
"""


class TestSym:
    """
    Method to test add method.
    """
    def test_add(self, sym_test):
        sym_test.add('Volume')
        assert sym_test.n == 1
        assert sym_test._has['Volume'] == 1

    """
    Method to test the mid method -- This tests the most frequent column in _has dictionary
    """
    def test_mid(self, sym_test):
        sym_test.add('Volume')
        sym_test.add('Volume')
        sym_test.add('Clndrs')
        assert sym_test.mid(None,None,None) == 'Volume'

    """
    Method to test the div method
    """
    def test_div(self, sym_test):
        sym_test.add('Volume')
        sym_test.add('Volume')
        sym_test.add('Clndrs')
        assert sym_test.div(0,None) == pytest.approx(0.91, 0.08)

    """
    To test add, mid and div methods
    """
    def test_sym(self, sym_test, entropy, mode):
        for i in ['a', 'a', 'a', 'a', 'b', 'b', 'c']:
            sym_test.add(i)
        mode, entropy = sym_test.mid(None, None, None), sym_test.div(0, None)
        entropy = ((1000 * entropy) // 1) / 1000
        assert mode == 'a'
        assert 1.38 >= entropy >= 1.37






