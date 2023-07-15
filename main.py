import CX_Library as Library
import schedule
import time
import threading

def scheduled_start():
    current_time = time.localtime()
    target_time = time.strptime("12:00:00", "%H:%M:%S")
    wait_time = (target_time.tm_hour - current_time.tm_hour) * 3600 + (target_time.tm_min - current_time.tm_min) * 60 + (target_time.tm_sec - current_time.tm_sec)
    time.sleep(wait_time)

def job(Library, seatNum):
    Library.submit(seatNum, Library.tomorrow, '09:00', '13:00')
    Library.submit(seatNum, Library.tomorrow, '13:00', '17:00')
    Library.submit(seatNum, Library.tomorrow, '17:00', '21:00')
    Library.submit(seatNum, Library.tomorrow, '21:00', '22:00')

def job1(Library, seatNum):
    Library.submit(seatNum, Library.tomorrow, '12:00', '12:30')

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
    print("hello")