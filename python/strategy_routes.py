from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, origin: str, destination: str) -> str:
        pass


class CarRouteStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> str:
        return f"Ruta en coche de {origin} a {destination}: autopista A-5, 18 min"


class BikeRouteStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> str:
        return f"Ruta en bici de {origin} a {destination}: carril bici central, 27 min"


class WalkRouteStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> str:
        return f"Ruta a pie de {origin} a {destination}: parque + calles peatonales, 40 min"


class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: RouteStrategy) -> None:
        self.strategy = strategy

    def route(self, origin: str, destination: str) -> str:
        return self.strategy.build_route(origin, destination)


if __name__ == "__main__":
    navigator = Navigator(CarRouteStrategy())

    print(navigator.route("Casa", "Universidad"))

    navigator.set_strategy(BikeRouteStrategy())
    print(navigator.route("Casa", "Universidad"))

    navigator.set_strategy(WalkRouteStrategy())
    print(navigator.route("Casa", "Universidad"))
