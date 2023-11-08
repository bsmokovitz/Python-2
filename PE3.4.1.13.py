class WeekDayError(Exception):
    pass

class WeekDay:
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if self.day not in week:
            raise WeekDayError
        else:
            self.day = week[(week.index(self.day) + n) % 7]

    def subtract_days(self, n):
        week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if self.day not in week:
            raise WeekDayError
        else:
            self.day = week[(week.index(self.day) - n) % 7]

try:
    day = WeekDay('Mon')
    print(day)
    day.add_days(15)
    print(day)
    day.subtract_days(23)
    print(day)
    day = WeekDay('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")