from code.Sym import Sym

"""
Class to test Sym.
"""


class TestSym:
    """
    Method to test add method.
    """
    def test_add(self):
        sym = Sym()
        sym.add('Volume')
        return sym.n == 1 and sym._has['Volume'] == 1

    """
    Method to test the mid method -- This tests the most frequent column in _has dictionary
    """
    def test_mid(self):
        sym = Sym()
        sym.add('Volume')
        sym.add('Volume')
        sym.add('Clndrs')
        return sym.mid(None, None, None) == 'Volume'

    """
    Method to test the div method
    """
    def test_div(self):
        sym = Sym()
        sym.add('Volume')
        sym.add('Volume')
        sym.add('Clndrs')
        return round(sym.div(0, None), 2) == 0.92

    """
    To test add, mid and div methods
    """
    def test_sym(self, entropy=None, mode=None):
        sym = Sym()
        for i in ['a', 'a', 'a', 'a', 'b', 'b', 'c']:
            sym.add(i)
        mode, entropy = sym.mid(None, None, None), sym.div(0, None)
        entropy = ((1000 * entropy) // 1) / 1000
        return mode == 'a' and 1.38 >= entropy >= 1.37



