class clockTime:
    def __init__(self, hours, minutes, seconds):  # constructor
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)

    def setHours(self, hours):
        if 0 <= hours <= 23:  # check the time within the range
            self.hours = hours
        else:
            print("Hours must within 0-23")

    def setMinutes(self, minutes):
        if 0 <= minutes <= 60:  # check the time within the range
            self.minutes = minutes
        else:
            print("Minutes must within 0-60")

    def setSeconds(self, seconds):
        if 0 <= seconds <= 60:  # check the time within the range
            self.seconds = seconds
        else:
            print("Seconds must within 0-60")

    def setTime(self, hours, minutes, seconds):
        if 0 <= seconds <= 60 and 0 <= hours <= 23 and 0 <= minutes <= 60:  # check the time within the range
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        else:
            print("Seconds must within 0-60")

    def showTime(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")  # print in formatted, hours:minutes:seconds


hours, minutes, seconds = input("Please enter hours, minutes and seconds seperated by space: ").split(" ")  # take in user input and split into hours, minutes and seconds by space
clock = clockTime.setTime(int(hours), int(minutes),int(seconds))  # creates new object clock and pass hours, minutes and seconds into the clockTime class
clock.showTime()  # calls showTime to print the time.
