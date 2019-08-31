import os
import sys
import time
from subprocess import run


def get_env(key, default=None):
    value = os.environ.get(key, default)
    print(f'{key} = {value}')
    return value


def main() -> None:
    interval = get_env('INTERVAL', 3600)
    config_path = get_env('CONFIG', '/data/bandersnatch.conf')
    extra_args = get_env('EXTRA', 'mirror --force-check')

    print(f"Running bandersnatch every {interval}s", file=sys.stderr)
    while True:
        start_time = time.time()
        cmd = ['bandersnatch', '-c', config_path, extra_args.split(' ')]
        run(cmd)
        run_time = time.time() - start_time
        if run_time < interval:
            sleep_time = interval - run_time
            print(f"Sleeping for {sleep_time}s", file=sys.stderr)
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
