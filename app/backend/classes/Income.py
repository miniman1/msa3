from Log import Log

class Income(Log):
    def __init__(self, day: int, month: int, year: int, amount: float, notes: str):
        super().__init__(day, month, year, amount, notes)
