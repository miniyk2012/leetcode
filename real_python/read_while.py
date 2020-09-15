import sys
from functools import partial
import heapq


f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
    # print(chunk, end='')

print()
RECORD_SIZE = 32
with open('/etc/passwd', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)