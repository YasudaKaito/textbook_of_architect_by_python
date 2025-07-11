import datetime


class Grade:
    def hourly_rate(self) -> int:
        """時給を返すメソッド"""
        # ここでは仮の実装として、固定の時給を返す
        return 3000


class WorkRecord:
    """勤怠実績クラス"""

    # コンストラクタ引数からGradeを削除
    # calc_overtime_payメソッドを削除
    # それ以外は修正なし

    STANDARD_WORK_HOURS = 8
    BREAK_TIME = 1

    def __init__(
        self,
        is_holiday: bool,
        clock_in: datetime.datetime,
        clock_out: datetime.datetime,
    ):
        self.is_holiday = is_holiday
        self.clock_in = clock_in
        self.clock_out = clock_out

    def calc_overtime_hours(self) -> int:
        """残業時間計算"""
        # 休憩時間を考慮して勤務時間を計算
        total_hours = (self.clock_out - self.clock_in).total_seconds() / 3600
        hours = int(total_hours - self.BREAK_TIME)

        # 休日はすべて残業とする
        if self.is_holiday:
            return hours

        # 標準労働時間より短い場合は残業なし
        if hours <= self.STANDARD_WORK_HOURS:
            return 0

        # 残業時間を計算
        overtime = max(hours - self.STANDARD_WORK_HOURS, 0)
        return overtime

class OvertimePayCalculator:
    """残業代計算クラス"""

    def calc_overtime_pay(self, overtime_hours: int, grade: Grade) -> int:
        """残業代計算"""
        return overtime_hours * grade.hourly_rate()

