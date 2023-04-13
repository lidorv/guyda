from frog_util import FrogUtil

def test_sum():
    assert FrogUtil.sum(1, 2) == 3

def test_greet():
    assert FrogUtil.frogGreet('testing') == 'testing 🐸'