from time import *

for t in range(30, -1, -1):
    minutes = t/60
    seconds = t % 60
    print "%20d" % (seconds)
    sleep(2.0)
