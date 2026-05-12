import pytest
from ticket_booth import TicketBooth

@pytest.fixture
def booth():
    return TicketBooth("Rock Night", 100)


def test_initial_state(booth):
    assert booth.remaining == 100
    assert len(booth) == 0
    assert booth.is_sold_out == False


def test_sell_tickets(booth):
    booth.sell(10)
    assert booth.remaining == 90
    assert len(booth) == 10


@pytest.mark.parametrize("amount", [1, 5, 20])
def test_multiple_sales(booth, amount):
    booth.sell(amount)

    assert len(booth) == amount
    assert booth.remaining == 100 - amount


@pytest.mark.parametrize("amount", [0, -1])
def test_invalid_sales(booth, amount):
    with pytest.raises(ValueError):
        booth.sell(amount)


def test_over_sell(booth):
    booth.sell(95)
    with pytest.raises(ValueError):
        booth.sell(10)


def test_sold_out(booth):
    booth.sell(100)
    assert booth.is_sold_out == True
    assert booth.remaining == 0
    with pytest.raises(ValueError):
        booth.sell(1)