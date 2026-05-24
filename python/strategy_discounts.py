from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, amount: float) -> float:
        return amount * (1 - self.percent / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, value: float):
        self.value = value

    def apply(self, amount: float) -> float:
        return max(0.0, amount - self.value)


class Checkout:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self.strategy = strategy

    def total(self, amount: float) -> float:
        return self.strategy.apply(amount)


if __name__ == "__main__":
    checkout = Checkout(NoDiscount())
    base_amount = 100.0

    print(f"Sin descuento: {checkout.total(base_amount):.2f} EUR")

    checkout.set_strategy(PercentageDiscount(20))
    print(f"Con 20% descuento: {checkout.total(base_amount):.2f} EUR")

    checkout.set_strategy(FixedDiscount(15))
    print(f"Con descuento fijo de 15: {checkout.total(base_amount):.2f} EUR")
