import random
import time

import gevent
from gevent import monkey

monkey.patch_all()


def fn(n):
    for i in range(n):
        print(f'{gevent.getcurrent()} {i}')
        time.sleep(random.random())


g1 = gevent.spawn(fn, 3)
g2 = gevent.spawn(fn, 4)
g3 = gevent.spawn(fn, 5)

# g1.join()
# g2.join()
# g3.join()

gevent.joinall([g1, g2, g3])
