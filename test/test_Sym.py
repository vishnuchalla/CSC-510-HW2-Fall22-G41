import pytest
from code.Sym import Sym

"""
Fixture to setup and teardown operation object for tests.
"""


@pytest.fixture()
def sym_test():
    print("\nSetting up operation object for test")
    sym = Sym()
    yield sym
    print("\nDeleting operation object as a teardown")
    del sym


"""
Class to test Operation.
"""


class TestSym:
    """
    Method to test add method.
    """
    # def test_add(self, sym_test):
    #     sym_test.add('Volume')
    #     assert sym_test.n == 1
    #     assert sym_test._has['Volume'] == 1

    """
    Method to test the mid method -- This tests the most frequent column in _has dictionary
    """
    # def test_mid(self, sym_test):
    #     sym_test.add('Volume')
    #     sym_test.add('Volume')
    #     sym_test.add('Clndrs')
    #     assert sym_test.mid(None,None,None) == 'Volume'

    """
    Method to test the div method
    """
    def test_div(self, sym_test):
        sym_test.add('Volume')
        sym_test.add('Volume')
        sym_test.add('Clndrs')
        assert sym_test.div(0,None) == pytest.approx(0.91, 0.08)




