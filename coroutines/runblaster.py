# runblaster.py

import subprocess
import time

NPROCS = 3
if __name__ == '__main__':

    start = time.time()

    procs = []
    for i in range(NPROCS):
        p = subprocess.Popen(['python', 'blaster.py'])
        procs.append(p)

    for p in procs:
        p.wait()

    end = time.time()

    print(end - start)
