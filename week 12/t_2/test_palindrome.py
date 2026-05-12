from palindrome import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("level") == True
    
def test_mixed_case_palindrome():
    assert is_palindrome("RaceCar") == True

def test_not_a_palindrome():
    assert not is_palindrome("python") == True
    
def test_single_character():
    assert is_palindrome("a") == True

def test_empty_string():
    assert is_palindrome("") == True