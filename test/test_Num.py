import pytest
from code.Num import Num

"""
Fixture to setup and teardown Num object for tests.
"""


@pytest.fixture()
def num_test():
    print("\nSetting up num object for test")
    num = Num()
    yield num
    print("\nDeleting num object as a teardown")
    del num


"""
Class to test Num.
"""