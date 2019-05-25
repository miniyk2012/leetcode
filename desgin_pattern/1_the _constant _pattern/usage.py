import calendar

calendar.January = 13
print(calendar.January)

from zipfile import ZIP_FILECOUNT_LIMIT

print(ZIP_FILECOUNT_LIMIT)

from types import FunctionType, LambdaType
print(FunctionType is LambdaType)
print(FunctionType)
print(LambdaType)

from os import environ
print(environ['PATH'])

from multiprocessing.process import _current_process
print(_current_process)
