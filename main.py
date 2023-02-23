import time


class Horloge:
    def __init__(self):
        self.status = True
        self.change = self.format = self.pause = False
        self.t = 1

# Main menu
    def menu_choice(self):  # For choice b and c we create a tuple and assign it to a function.
        print("What do you want to do ?\n a = display hour, b = set and launch custom clock, c = set alarm : ")
        choice = str(input())
        if choice == 'a':
            print("You chose a, it will ask you a format to start a clock and clock will stop after 5 seconds.")
            self.set_format()
            self.show_hour()
        elif choice == 'b':
            print("You chose b, enter three number to create a custom time position : ")
            val1, val2, val3 = input().split()
            tup_time = (val1, val2, val3)
            self.set_hour(tup_time)
        elif choice == 'c':
            print("You chose c, enter three number to create an alarm : ")
            tempus = time.strftime("%H:%M:%S")
            print("\r", tempus, end="")
            val1, val2, val3 = input("\n").split()
            tup_alarm = (val1, val2, val3)
            self.set_alarm(tup_alarm)

    def show_hour(self):
        if self.format:  # Run if format is AM/PM
            while self.status:  # %I = hour from [1-12], %p to see am/pm
                self.t_time = time.strftime("%I:%M:%S%p")  # Stores time in hour, minute, second format
                # 1st argument print 2nd argument on same line. 3rd update the variable at same position
                print("\r", self.t_time, end="")
                time.sleep(1)
                self.pause = True
                self.t += 1  # Increment timer
                if self.t == 5 and self.pause:  # Will trigger pause(), value can be changed for a longer delay before pause.
                    self.pause = False  # set pause as false to avoid looping through pause_clock()
                    self.pause_clock()

        while self.status:  # Run with 24-hour format
            self.t_time = time.strftime("%H:%M:%S")
            print("\r", self.t_time, end="")
            time.sleep(1)
            self.pause = True
            self.t += 1
            if self.t == 5 and self.pause:
                self.pause = False
                self.pause_clock()

    def set_hour(self, tup):
        self.change = True
        tuptime = tup[0] + ":" + tup[1] + ":" + tup[2]  # Create a str parsed in strptime()
        # Return a float to be used create a starting time point
        set_time = time.mktime(time.strptime(tuptime, "%H:%M:%S"))
        while self.status:
            newtime = time.strftime("%H:%M:%S", time.localtime(set_time))  # Set a clock with starting point
            set_time += 1  # Increment newtime to run the clock.
            print("\r", newtime, end="")
            time.sleep(1)

    def set_alarm(self, alarm):
        print(f"Your alarm is set at {alarm[0]}:{alarm[1]}:{alarm[2]}")
        while self.status:
            local = time.strftime("%H:%M:%S")  # Get real-time and print it below
            # Get hour, minute, seconds from time module
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            seconde = time.strftime("%S")

            print("\r", local, end="")
            time.sleep(1)
            if alarm[0] == hour and alarm[1] == minute and alarm[2] == seconde:  # Check user values == real-time values
                print("\nDDRRRRRINNNNNNNG, I cannot ring, but it is time !")

    def set_format(self):  # Allow user to select time format
        print("Which hour format do you want ? \n")
        choice = input("Press a for 12 or b for 24 : ")
        if choice == 'a':
            print("You chose format 12")
            self.format = True
        else:
            print("You chose format 24")

    def pause_clock(self):  # Pause clock with input function
        input("\nClock is paused, press any key to unpause : ")
        self.show_hour()


if __name__ == '__main__':
    app = Horloge()
    app.menu_choice()
