import argparse
from datetime import datetime as dt
import sys
import time

try:
    import chime
except ImportError:
    print("chime module not installed.\n" \
          "Install it with pip, preferably inside a virtual env")
    sys.exit(1)


def main():
    pom(*args())


def pom(pom_count: int, work_time: int, break_time: int) -> None:
    print(f"Starting the a session of {pom_count} {work_time}/{break_time}poms. {dt.now().strftime("%H:%M")}")
    for i in range(pom_count):
        if i > 1: print(f"Starting pom #{i}, get back to work! {dt.now().strftime("%H:%M")}")
        time.sleep(work_time * 60)
        chime.success()
        print(f"Pom #{i} done, take a break! {dt.now().strftime("%H:%M")}")
        time.sleep(break_time * 60)
        chime.success()
    print(f"Completed all {pom_count} poms, good work! {dt.now().strftime("%H:%M")}")


def args() -> tuple[int, int, int]:
    parser = argparse.ArgumentParser(prog='python pom.py', description='CLI Pomodoro Timer written in Python')
    parser.add_argument('pom_count', type=int, help='Number of poms')
    parser.add_argument('work_time', type=int, help='Work duration in minutes')
    parser.add_argument('break_time', type=int, help='Break duration in minutes')
    args = parser.parse_args()
    return (args.pom_count, args.work_time, args.break_time)


if __name__ == "__main__":
    main()
