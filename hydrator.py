import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

current_hour = int(current_time [0:2])
print("current_hour - ", current_hour)

start_hour = 5.5
increment = 1

current_dif = current_hour - start_hour
print(current_dif)

if current_dif >= 0:
    print("drink up")