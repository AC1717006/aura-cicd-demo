DISCOUNT_RATE = 0.50  # 10% — badalna ho to bas yahan


def discount(amount):
    if amount > 1000:
        return amount * DISCOUNT_RATE
    return 0
