import enum

from .srp_after import WorkRecord


class Grade(enum.Enum):
    REGULAR = "regular"
    MANAGER = "manager"

    def hourly_rate(self) -> int:
        match self:
            case Grade.REGULAR:
                return 3000
            case Grade.MANAGER:
                return 5000
            case _:
                raise ValueError("不明なGradeです")


class OvertimePayCalculator:
    """残業代計算クラス"""

    def calc_overtime_pay(
        self,
        work_record: WorkRecord,
        grade: Grade,
    ) -> float:
        match grade:
            case Grade.REGULAR:
                return (
                    work_record.calc_overtime_hours()
                    * grade.hourly_rate()
                    * (1.2 if work_record.is_holiday else 1)
                )  # 休日は2割増
            case Grade.MANAGER:
                return 0  # 管理職は残業代なし
