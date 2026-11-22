def delivery_fee(order_total: int) -> int:
    if order_total >= 2_000:
        return 0
    return 250

def test_delivery_fee_below() -> None:
    assert delivery_fee(1_999) == 250

def test_delivery_fee_higher() -> None:
    assert delivery_fee(2_000) == 0
