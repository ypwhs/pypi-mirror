import os
import sys
import time
from subprocess import run


def main() -> None:
    interval = os.environ.get('INTERVAL', 3600)

    print(f"Running bandersnatch every {interval}s", file=sys.stderr)
    while True:
        start_time = time.time()
        run(["/usr/bin/bandersnatch", "mirror"])
        run_time = time.time() - start_time
        if run_time < interval:
            sleep_time = interval - run_time
            print(f"Sleeping for {sleep_time}s", file=sys.stderr)
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
