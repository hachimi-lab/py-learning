import datetime
import threading

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.date import DateTrigger


def job_1():
    print("I'm working... job_1")


def job_2():
    print("I'm working... job_2")


def job_3():
    print("I'm working... job_3")


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # 周一到周五每天0点15分执行一次
    scheduler.add_job(job_1, 'cron', day_of_week='mon-fri', hour=0, minute=15, second=0)
    # 每隔2秒执行一次
    scheduler.add_job(job_2, 'interval', seconds=2)
    # 指定运行时间
    scheduler.add_job(job_3, DateTrigger(run_date=datetime.datetime.now() + datetime.timedelta(seconds=5)))

    timer = threading.Timer(10, scheduler.shutdown, [True])
    timer.start()
    scheduler.start()
