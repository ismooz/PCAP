class Timer:
    def __init__(self, hours=0, min=0, sec=0):
        self.__hours = hours
        self.__min = min
        self.__sec = sec

    def __str__(self):
        hour = f"{self.__hours:02}:{self.__min:02}:{self.__sec:02}"
        return hour.zfill(2)

    def next_second(self):
        self.__sec += 1
        if self.__sec > 59:
            self.__sec = 0
            self.__min += 1
        if self.__min > 59:
            self.__min = 0
            self.__hours += 1
            if self.__hours > 23:
                self.__hours = 0

    def prev_second(self):
        self.__sec -= 1
        if self.__sec < 0:
            self.__sec = 59
            self.__min -= 1
        if self.__min < 0:
            self.__min = 59
            self.__hours -= 1
        if self.__hours < 0:
            self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
