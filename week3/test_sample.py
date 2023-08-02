from lesson import add_one, division, sum_, is_palindrome,count_factorial


print(add_one(7))

import pytest

# 1
def test_answer():
    assert add_one(4) == 5
    assert add_one(6) == 7



# 2
def test_division():
    assert division(72,9) == 8
    assert division(63,7) == 9



# 3
def test_division2():
    with pytest.raises(ZeroDivisionError):
        division(9,0)



# 4
def test_sum_():
    t = [[1,2,3], [3,4,7], [8,5,13]]
    for i in t:
        assert sum_(i[0], i[1]) == i[2]



# 5
def test_pal():
    test_case = [('dad', True),('nurs', False)]
    for case in test_case:
        assert is_palindrome(case[0]) == case[1]
    assert is_palindrome('Mom') == True



# 6 
def test_c_f():
    from math import factorial
    assert count_factorial(10) == factorial(10)
    



