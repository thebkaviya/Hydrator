import time

#get current system time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

current_hour = int(current_time [0:2]) #get the current hour
print("current_hour - ", current_hour)

start_hour = 8
increment = 1

current_dif = current_hour - start_hour
print(current_dif)

if current_dif >= 0:
    print("drink up")
