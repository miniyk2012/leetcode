# module/file b.py
import sys
from importlib import reload

print("Hello from b.py!")
# print(sys.modules)
import a
print('---')
reload(a)