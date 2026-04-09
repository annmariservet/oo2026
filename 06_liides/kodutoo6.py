from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

class AdultTicket(Ticket):
    def __init__(self, count: int):
        self.price = 10.0
        self.count = count

    def get_price(self) -> float:
        return self.price * self.count

class StudentTicket(Ticket):
    def __init__(self, count: int):
        self.price = 10.0
        self.count = count

    def get_price(self) -> float:
        return self.price * 0.5 * self.count

class ChildTicket(Ticket):
    def __init__(self, count: int):
        self.price = 10.0
        self.count = count

    def get_price(self) -> float:
        return self.price * 0.3 * self.count

def total_price(tickets: list[Ticket]) -> float:
    return sum(ticket.get_price() for ticket in tickets)

tickets = [
    AdultTicket(2),
    StudentTicket(1),
    ChildTicket(3)
]

print("Koguhind:", total_price(tickets))