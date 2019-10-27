# module/file b.py
from importlib import reload

print("Hello from b.py!")
import a
print('---')
reload(a)
print('b end')
