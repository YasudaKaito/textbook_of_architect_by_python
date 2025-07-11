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

    @abstractmethod
    def estimate(self, estimation_point: int) -> None:
        ...

    @abstractmethod
    def record(self, actual_point: int) -> None:
        ...


class BugTicket(Ticket):
    ...


class StoryTicket(Ticket):
    ...


class IssueTicket(Ticket):
    def estimate(self, estimation_point: int) -> None:
        raise NotImplementedError("イシューチケットは見積もりを行いません")

    def record(self, actual_point: int) -> None:
        raise NotImplementedError("イシューチケットは実績を記録しません")
