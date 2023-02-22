import time
status = True
list_time_alarm = (0, 0, 5)     # Tuple for the alarm parameter


# Function to print a message when the time is equal the alarm setting


def alarm(time_alarm):
    if time_alarm == list_time_alarm:
        print("It is time")
    else:
        pass


# Function to print the time every second on the same line and have the other part of the alarm setting


def change_time(new_hour):
    global list_time_alarm
    list_time_alarm = list(list_time_alarm)
    list_new_hour = list(new_hour)

    while status is True:
        list_new_hour[2] += 1
        print("\r", list_new_hour[0], ":", list_new_hour[1], ":", list_new_hour[2], end="")  #Remove the former line for clarity
        if list_new_hour[2] >= 59:
            list_new_hour[1] += 1
            list_new_hour[2] = 0
        if list_new_hour[1] >= 60:
            list_new_hour[0] += 1
            list_new_hour[1] = 0
        if list_new_hour[0] >= 24:
            list_new_hour[0] = 0

        if list_new_hour == list_time_alarm:        # Starts the alarm function if the two list match
            alarm(list_time_alarm)

        time.sleep(1)


change_time((23, 59, 50))


# Display the actual time if no other function is active


def display_time():
    while status is True:
        time_live = time.strftime("%H:%M:%S")
        print("\r", time_live, end="")
        time.sleep(1)


display_time()