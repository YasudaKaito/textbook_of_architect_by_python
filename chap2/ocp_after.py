from abc import ABC, abstractmethod
from .ocp_before import Grade
from .srp_after import WorkRecord


class OvertimePayPolicy(ABC):
    """残業代ポリシーの基底クラス"""

    @abstractmethod
    def payment_rate(self) -> float:
        ...


class RegularGradeOvertimePolicy(OvertimePayPolicy):
    def __init__(self, is_holiday: bool) -> None:
        self.is_holiday = is_holiday

    def payment_rate(self):
        return 1.2 if self.is_holiday else 1  # 休日は2割増


class ManagerGradeOvertimePolicy(OvertimePayPolicy):
    def __init__(self, is_holiday: bool) -> None:
        self.is_holiday = is_holiday

    def payment_rate(self):
        ####################
        # 仕様変更時、この箇所を修正するだけで済む
        ####################
        return 1 if self.is_holiday else 0  # 管理職でも休日残業は支払われる


class OvertimePayPolicyFactory:
    """残業代ポリシーのファクトリクラス"""

    @staticmethod
    def of(is_holiday: bool, grade: Grade) -> OvertimePayPolicy:
        match grade:
            case Grade.REGULAR:
                return RegularGradeOvertimePolicy(is_holiday)
            case Grade.MANAGER:
                return ManagerGradeOvertimePolicy(is_holiday)


class OvertimePayCalculator:
    """残業代計算クラス"""

    def calc_overtime_pay(
        self,
        work_record: WorkRecord,
        grade: Grade,
    ) -> float:
        policy = OvertimePayPolicyFactory.of(
            is_holiday=work_record.is_holiday,
            grade=grade,
        )
        return (
            work_record.calc_overtime_hours()
            * grade.hourly_rate()
            * policy.payment_rate()
        )
