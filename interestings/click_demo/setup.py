from setuptools import setup

setup(
    name='hl',
    version='0.1',
    py_modules=['hl'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hl=hl:hello
    ''',
)