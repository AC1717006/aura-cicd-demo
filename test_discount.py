from discount import discount


def test_1500_ke_order_pe_discount_150():
    assert discount(1500) == 150


def test_900_ke_order_pe_discount_zero():
    assert discount(900) == 0
