from abc import ABC, abstractmethod


class Ticket(ABC):
    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def assign(self, assignee: str) -> None:
        ...


class Estimatable(ABC):
    @abstractmethod
    def estimate(self, estimation_point: int) -> None:
        ...

    @abstractmethod
    def record(self, actual_point: int) -> None:
        ...


class BugTicket(Ticket, Estimatable):
    ...


class StoryTicket(Ticket, Estimatable):
    ...


class IssueTicket(Ticket):
    ...
