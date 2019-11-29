import os
from pathlib import Path

print(os.getcwd())
print(Path.resolve(Path('../')))
# os.chdir(Path('/'))
# print(os.getcwd())


print(Path.home())
print(os.path.expanduser('~'))
print(Path('~/abc').expanduser())

print(Path('__init__.py').stat())

print(Path('/usr/local/etc/mongod.conf').name)
print(Path('/usr/local/etc/mongod.conf').parent)
print(type(Path('/usr/local/etc/mongod.conf').parent))

print(Path('/').joinpath('home', 'yangkai', 'zhihu'))
print(Path.exists(Path('~/lyanna').expanduser() / 'config.py'))
print(Path.exists(Path('~/Documents').expanduser() / 'code' / 'leetcode' / 'README.txt'))

p = Path('/Users/dongweiming/test.txt')
print(p.parent.parent)
print()
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])

print(p.suffix, p.stem)
print(p.suffixes, p.stem)

Path('new.txt').touch()

p = Path('./test.txt')
p.write_text('456\n')
print(p.read_text())

p = Path('/home/gentoo/screenshot/abc.jpg')
print(p.with_suffix('.png'))
print(p.with_name(f'123{p.suffix}'))

Path('1/2/3').mkdir(parents=True, exist_ok=True)
print(Path('1').owner())
