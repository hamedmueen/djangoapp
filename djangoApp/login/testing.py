import time
t = 10
while t:
    mins = t // 60
    secs = t % 60

    timer = '{:02d}:{:02d}'.format(mins, secs)
    time.sleep(1)
    t -= 1
    print(timer)
print('finish')