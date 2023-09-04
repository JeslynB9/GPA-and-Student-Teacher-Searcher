from program import is_valid_credit_hour
from unittest.mock import patch

# write your first test here
def test_valid_1():
    with patch("builtins.print"):
    # Positive case
        return is_valid_credit_hour("1") == True

def test_valid_2():
    with patch("builtins.print"):
        # Positive case
        return is_valid_credit_hour("5") == True

def test_valid_3():
    with patch("builtins.print"):
        # Negative case
        return is_valid_credit_hour("0") == False

def test_valid_4():
    with patch("builtins.print"):
        # Negative case
        return is_valid_credit_hour("6") == False

def test_valid_5():
    with patch("builtins.print"):
        # Edge case
        return is_valid_credit_hour("") == False

def test_valid_6():
    with patch("builtins.print"):
        # Edge case
        return is_valid_credit_hour("3.5") == False

'''
Remember, we only print ONCE whether we passed or failed.
We have passed if ALL tests passed.
We have failed if ANY tests failed.
'''
passed = test_valid_1() and test_valid_2() and test_valid_3() and test_valid_4() and test_valid_5() and test_valid_6()
if passed:
    print("is_valid_credit_hour has passed.")
else:
    print("is_valid_credit_hour has failed.")
