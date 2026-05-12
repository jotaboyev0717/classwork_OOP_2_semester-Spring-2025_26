from loyalty import LoyaltyCard
import pytest

@pytest.fixture
def empty_card():
    return LoyaltyCard("Alice")

@pytest.fixture
def funded_card():
    return LoyaltyCard("Bob", 100)



    
