from day16_T3 import main, split_and_sum
import pytest, sys

@pytest.mark.parametrize("values, outputs", [([1, 2, 3, 4], "first: 1, total of rest: 9")
                                            , ([5], "first: 5, total of rest: 0")
                                            , ([5, -3, 3], "first: 5, total of rest: 0")])
def test_split_and_num(values, outputs):
    assert split_and_sum(*values) == outputs

def test_split_and_sum_no_args():
    with pytest.raises(ValueError):
        split_and_sum()

def test_main(monkeypatch):
    fake_argv = ["day16_T3.py", "5", "3", "-3"]
    monkeypatch.setattr(sys, "argv", fake_argv)

    assert main() == "first: 5, total of rest: 0"