class WeekDayError(Exception):
    pass
	

class Weeker:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = []

    def __init__(self, day):
        if day not in self.days:
            raise WeekDayError("Invalid day")
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        index = self.days.index(self.day)
        index = (index + n) % 7
        self.day = self.days[index]

    def subtract_days(self, n):
        index = self.days.index(self.day)
        index = (index - n) % 7
        self.day = self.days[index]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
