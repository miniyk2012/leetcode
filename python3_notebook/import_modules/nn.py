import importlib, sys

z = importlib.import_module('mm')
print(z)
assert 'mm' in sys.modules
assert z == sys.modules['mm']