from helpers import is_error, is_warning, is_info


def test_error():
    assert is_error("ERROR system crashed")
    assert not is_error("INFO system started")


def test_warning():
    assert is_warning("WARNING low battery")
    assert not is_warning("ERROR system failed")


def test_info():
    assert is_info("INFO system started")
    assert not is_info("WARNING low battery")


test_error()
test_warning()
test_info()

print("All tests passed.")