from datetime import date, datetime
from time import sleep
import subprocess
from threading import Thread


class UseUnlimited:
    def __init__(self, start_time: datetime, endtime: datetime) -> None:
        self.start_time: datetime = start_time
        self.endtime: datetime = endtime
        self.program: subprocess.Popen = None

    def run(self):
        print("Started runner")
        while datetime.now() < self.start_time:
            sleep(60)
        print("opening program")
        self.program = subprocess.Popen(args=["transmission-gtk"])

    def watch(self):
        print("Started watcher")
        while datetime.now() < self.endtime:
            sleep(60)
        print("terminating program")
        self.program.terminate()

    def execute(self):
        runner = Thread(target=self.run, args=[])
        runner.start()
        watcher = Thread(target=self.watch, args=[])
        watcher.start()


if __name__ == "__main__":
    start_time: datetime = datetime.now().replace(
        hour=4, minute=0, second=0, microsecond=0
    )
    endtime: datetime = datetime.now().replace(
        hour=8, minute=0, second=0, microsecond=0
    )
    use_unlimited: UseUnlimited = UseUnlimited(start_time, endtime)
    use_unlimited.execute()
