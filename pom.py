import chime
from datetime import datetime as dt
import sys
import time


def pom(work_time: int, break_time: int, pom_count: int) -> None:
    print(f"Starting the a session of {pom_count} {work_time}/{break_time}poms. {dt.now().strftime("%H:%M")}")
    for i in range(pom_count):
        if i > 1: print(f"Starting pom #{i}, get back to work! {dt.now().strftime("%H:%M")}")
        time.sleep(work_time * 60)
        chime.success()
        print(f"Pom #{i} done, take a break! {dt.now().strftime("%H:%M")}")
        time.sleep(break_time * 60)
        chime.success()
    print(f"Completed all {pom_count} poms, good work! {dt.now().strftime("%H:%M")}")

def main():
    if len(sys.argv) == 4:
        pom(*[int(i) for i in sys.argv[1:]])


if __name__ == "__main__":
    main()
