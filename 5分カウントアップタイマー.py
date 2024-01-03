from time import sleep

target_time = 5
def countup_timer(mins):
    for x in range(0,mins):
        print(x)
        sleep(60)
    print("休憩終了です")

countup_timer(target_time)

