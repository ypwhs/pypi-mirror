import os
import sys
import time
from subprocess import run


def get_env(key, default=None):
    value = os.environ.get(key, default)
    print(f'{key} = {value}')
    return value


def main() -> None:
    interval = int(get_env('INTERVAL', 3600))
    cmd = get_env('CMD', 'bandersnatch -c bandersnatch.conf mirror')
    cmd = cmd.split(' ')
    print(f'CMD: {cmd}', file=sys.stderr)
    print(f"Running bandersnatch every {interval}s", file=sys.stderr)
    while True:
        start_time = time.time()
        run(cmd)
        run_time = time.time() - start_time
        if run_time < interval:
            sleep_time = interval - run_time
            print(f"Sleeping for {sleep_time}s", file=sys.stderr)
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
