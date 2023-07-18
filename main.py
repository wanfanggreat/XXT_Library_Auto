import CX_Library as Library
import time
import threading
import datetime
import pytz

def scheduled_start():
    # Get the current time in the network's UTC timezone
    current_time = datetime.datetime.now(pytz.timezone('UTC'))

    # Convert the current time to Beijing timezone
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    current_time_beijing = current_time.astimezone(beijing_timezone)
    print("now time is: {}:{}:{}".format(current_time_beijing.hour, current_time_beijing.minute, current_time_beijing.second))

    # Set the target time in Beijing timezone
    target_time = datetime.datetime.strptime("12:00:00", "%H:%M:%S").time()

    # Calculate the wait time in seconds
    wait_time = (target_time.hour - current_time_beijing.hour) * 3600 + (target_time.minute - current_time_beijing.minute) * 60 + (target_time.second - current_time_beijing.second)

    # Wait for the scheduled start time
    time.sleep(wait_time)

def job(Library, seatNum):
    Library.submit(seatNum, Library.tomorrow, '10:30', '14:30')

if __name__ == '__main__':
    lib1 = Library.Library("111111111111", "111111111", "1")
    lib2 = Library.Library("1111111111", "1111111111", "1")
 
    # 创建线程
    thread1 = threading.Thread(target=job, args=(lib1, "053"))
    thread2 = threading.Thread(target=job, args=(lib2, "056"))

    # 等待指定时间
    scheduled_start()

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程完成
    thread1.join()
    thread2.join()