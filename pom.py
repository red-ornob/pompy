import argparse
from curses import echo
from datetime import datetime as dt
from encodings.punycode import T
import threading
import sys
import time

try:
    import chime
except ImportError:
    print("chime module not installed.\n" \
          "Install it with pip, preferably inside a virtual env")
    sys.exit(1)


running = True


def main():
    timer = threading.Thread(target=pom, args=args())
    timer.daemon = True
    reader = threading.Thread(target=interact)
    reader.daemon = True
    
    try:
        timer.start()
        reader.start()
        timer.join()
        reader.join()
    
    except KeyboardInterrupt:
        print("\nTimer interrupted")


def pom(pom_count: int, work_time: int, break_time: int) -> None:
    global running
    
    print(f"Starting the a session of {pom_count} {work_time}/{break_time} poms. {dt.now().strftime("%H:%M")}")
    i = 1
    while i <= pom_count and running:
        
        if i > 1: print(f"Starting pom #{i}, get back to work! {dt.now().strftime("%H:%M")}")
        t = work_time * 60
        while t and running:
            time.sleep(1)
            t -= 1
        chime.success()
        
        print(f"Pom #{i} done, take a break! {dt.now().strftime("%H:%M")}")
        t = break_time * 60
        while t and running:
            time.sleep(1)
            t -= 1
        chime.success()
        
        i += 1
    
    print(f"Completed all {pom_count} poms, good work! {dt.now().strftime("%H:%M")}")
    running = False
    


def args() -> tuple[int, int, int]:
    parser = argparse.ArgumentParser(prog='python pom.py', description='CLI Pomodoro Timer written in Python')
    parser.add_argument('pom_count', type=int, help='Number of poms')
    parser.add_argument('work_time', type=int, help='Work duration in minutes')
    parser.add_argument('break_time', type=int, help='Break duration in minutes')
    
    args = parser.parse_args()
    return (args.pom_count, args.work_time, args.break_time)


def interact() -> None:
    global running
    
    try:
        while True and running:
            match input("> "):
                case "timeleft":
                    ...
                case "pause":
                    ...
                case "break":
                    ...
                case "skip":
                    ...
                case "end":
                    running = False
                case _:
                    pass
    
    except EOFError:
        running = False


if __name__ == "__main__":
    main()
