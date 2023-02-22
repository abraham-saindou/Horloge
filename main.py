import time


class Horloge:
    def __init__(self):
        self.status = True
        self.change = False
        self.tuple_alarm = (10, 10, 10)

    def run(self):
        self.show_hour()

    def show_hour(self):
        while self.status:
            self.t_time = time.strftime("%H:%M:%S")  # Stores time in hour, minute, second format
            # 1st argument print 2nd argument on same line. 3rd update the variable at same position
            if self.change:
                self.t_time = self.tnewtime
            print(self.t_time)
            print("\r", self.t_time, end="")
            time.sleep(1)

    def change_hour(self, tup=tuple(input("Enter 3 number to make time position : ").split())):
        self.change = True
        t = list(tup)
        for x in t:
            x = str(x)
        tuptime = t[0] + ":" + t[1] + ":" + t[2]
        set_time = time.mktime(time.strptime(tuptime, "%H:%M:%S"))
        while self.status:
            newtime = time.strftime("%H:%M:%S", time.localtime(set_time))
            set_time += 1
            print("\r", newtime, end="")
            time.sleep(1)

    def set_alarm(self, tup=tuple(input("Enter 3 number to create an alarm : ").split())):
        print("DDRRRRRINNNNNNNG, I cannot ring, but it is time !")

    def change_format(self):
        pass

    def pause(self):
        pass


if __name__ == '__main__':
    app = Horloge()
    app.run()
