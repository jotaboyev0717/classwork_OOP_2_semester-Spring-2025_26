from pizza import slices_per_person

def test_even_split():
    assert slices_per_person(8, 4) == 2

def test_uneven_split():
    assert slices_per_person(10, 3) == 3
    
def test_one_each():
    assert slices_per_person(5, 5) == 1
    