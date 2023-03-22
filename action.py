
""" doc string module """

def func(num: int):
    """ doc string function"""
    return num + 1

def test_answer( pys : int ):
    """ doc string function"""
    assert func(pys) == 5

test_answer(4)

