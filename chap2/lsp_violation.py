from abc import ABC, abstractmethod


class Ticket(ABC):
    @abstractmethod
    def estimate(self, point: int) -> None:
        assert point >= 1
        self.point = point


class BugTicket(Ticket):
    ...


class StoryTicket(Ticket):

    FIBONACCI_NUMBERS = {1, 2, 3, 5, 8, 13, 21}

    def estimate(self, point: int):
        assert point in self.FIBONACCI_NUMBERS, "見積もりポイントはフィボナッチ数でなければなりません"
        super().estimate(point)


def estimate_all_tickets(tickets: list[Ticket], estimation_point: int) -> None:
    ####################
    # estimation_point = 4で、チケットがStoryTicketの場合、AssertionErrorが発生
    ####################
    for ticket in tickets:
        ticket.estimate(estimation_point)
