import datetime
import calendar

class Time:
    def __init__(self):
        self._currentYear = self.getCurrentYear()
        self._currentMonth = self.getCurrentMonth()
        self._currentMonthName = self.getCurrentMonthName()
        self._currentDay = self.getCurrentDay()
        pass

    def getCurrentDay(self) -> int:
        return datetime.datetime.now().day

    def getCurrentMonth(self) -> int:
        return datetime.datetime.now().month

    def getCurrentYear(self) -> int:
        return datetime.datetime.now().year

    def getCurrentMonthName(self) -> str:
        return datetime.datetime.now().strftime("%B")
    
    def getMonthName(self, month: int) -> str:
        return datetime.date(1900, month, 1).strftime("%B")
    
    def getDayName(self, year: str, month: str, day: str) -> str:
        return datetime.date(year, month, day).strftime("%A")

    def getDaysAmountInMonth(self, month: int, year: int) -> int:
        return calendar.monthrange(year, month)[1]
    
    def getCurrentDate(self, format: str="%d.%m.%Y") -> str:
        return datetime.datetime.now().strftime(format)

    def getTimeStamp(self, format: str="%d.%m.%Y %H:%M:%S") -> str:
        '''Returns a timestamp in the given format. Example standart format: 01.01.2021 00:00:00'''
        return datetime.datetime.now().strftime(format)
    
my_Time = Time()